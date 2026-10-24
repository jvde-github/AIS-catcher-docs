"""Write docs/api/reference.md and docs/api/openapi.json from the OpenAPI
document a running AIS-catcher serves, so the reference says what the code does.

    python3 scripts/api_reference.py http://127.0.0.1:8110

The server must offer api and system (with a key, set KEY in the environment).
"""
import json, os, sys, urllib.request

here = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(here, "..", "docs", "api")

source = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://127.0.0.1:8110"
if source.startswith("http"):
    req = urllib.request.Request(source + "/api/v1/openapi.json")
    if os.environ.get("KEY"):
        req.add_header("Authorization", "Bearer " + os.environ["KEY"])
    doc = json.load(urllib.request.urlopen(req))
else:
    doc = json.load(open(source))

schemas = doc["components"]["schemas"]
LISTS = {}  # a list schema: the object of its rows and its meta
for name, s in schemas.items():
    props = s.get("properties", {})
    if set(props) == {"data", "meta"}:
        LISTS[name] = (props["data"]["items"]["$ref"].split("/")[-1], props["meta"]["$ref"].split("/")[-1])


def anchor(name):
    return "#" + name.lower()


def link(name):
    return f"[{name}]({anchor(name)})"


def type_of(s):
    if "$ref" in s:
        target = s["$ref"].split("/")[-1]
        return link(target)
    if "const" in s:
        return f"`{s['const']}`"
    if "enum" in s:
        values = [v for v in s["enum"] if v is not None]
        text = "one of " + ", ".join(f"`{v}`" for v in values)
        return text + (", or null" if None in s["enum"] else "")
    t = s.get("type")
    types = t if isinstance(t, list) else [t] if t else []
    nullable = "null" in types
    types = [x for x in types if x != "null"]
    base = types[0] if types else "any"
    if base == "string" and s.get("format") == "date-time":
        base = "time"
    if base == "array":
        items = s.get("items", {})
        base = "list of " + type_of(items)
    elif base == "object" and "additionalProperties" in s and isinstance(s["additionalProperties"], dict):
        base = "object of " + type_of(s["additionalProperties"])
    return base + (" or null" if nullable else "")


def merged(s):
    """The fields of a schema, the members of an allOf added up."""
    if "$ref" in s:
        return merged(schemas[s["$ref"].split("/")[-1]])
    props, required = {}, set(s.get("required", []))
    for part in s.get("allOf", []):
        p, r = merged(part)
        props.update(p)
        required |= r
    props.update(s.get("properties", {}))
    return props, required


def rows(props, prefix=""):
    for name, s in props.items():
        desc = s.get("description", "")
        yield f"| `{prefix}{name}` | {type_of(s)} | {desc} |"
        if s.get("type") in ("object", ["object", "null"]) and "properties" in s:
            yield from rows(s["properties"], prefix + name + ".")
        items = s.get("items", {})
        if isinstance(items, dict) and "properties" in items:
            yield from rows(items["properties"], prefix + name + "[].")


def param_type(p):
    s = p["schema"]
    if s.get("type") == "array":
        items = s["items"]
        if "enum" in items:
            return "one or more of " + ", ".join(f"`{v}`" for v in items["enum"]) + ", separated by commas"
        return items.get("type", "value") + "s separated by commas"
    t = type_of(s)
    bounds = []
    if "minimum" in s and "maximum" in s:
        bounds.append(f"{s['minimum']} to {s['maximum']}")
    if "default" in s:
        bounds.append(f"{s['default']} unless set")
    return t + ("; " + "; ".join(bounds) if bounds else "")


lines = [
    "# API reference",
    "",
    "<!-- Written by scripts/api_reference.py from the OpenAPI document of AIS-catcher "
    + doc["info"]["version"] + ". Do not edit by hand: run the script again. -->",
    "",
    "Every route of `/api/v1` with its parameters, and every object it answers with, field by field. "
    "[The API](overview.md) explains how the lists page and how to follow what changes. "
    "The same, for a client generator or an API tool: [openapi.json](openapi.json), as every server gives it at `/api/v1/openapi.json`.",
    "",
]

ops = []
for path, item in doc["paths"].items():
    op = item["get"]
    ops.append((op["tags"][0], path, op))
tags = [t["name"] for t in doc.get("tags", [])]
for tag in tags:
    group = [o for o in ops if o[0] == tag]
    if not group:
        continue
    description = next(t.get("description", "") for t in doc["tags"] if t["name"] == tag)
    lines += [f"## {tag}", "", description + ("." if description and not description.endswith(".") else ""), ""]
    for _, path, op in group:
        lines += [f"### `GET {path}`", "", op["summary"], ""]
        params = op.get("parameters", [])
        if params:
            lines += ["| Parameter | In | Type | Description |", "|---|---|---|---|"]
            for p in params:
                lines.append(f"| `{p['name']}` | {p['in']} | {param_type(p)} | {p.get('description', '')} |")
            lines.append("")
        content = op["responses"]["200"]["content"]
        answers = []
        for kind, c in content.items():
            ref = c["schema"].get("$ref")
            answers.append(f"{link(ref.split('/')[-1]) if ref else 'the document'} as `{kind}`")
        lines += ["Answers " + " or ".join(answers) + f". Operation `{op['operationId']}`.", ""]

lines += ["## Objects", ""]
for name in schemas:
    s = schemas[name]
    lines += [f"### {name}", ""]
    if name in LISTS:
        row, meta = LISTS[name]
        lines += [f"A list: `data` holds {link(row)} rows, `meta` is {link(meta)}.", ""]
        continue
    if s.get("description"):
        lines += [s["description"] + ".", ""]
    if "allOf" in s:
        bases = [part["$ref"].split("/")[-1] for part in s["allOf"] if "$ref" in part]
        own = {}
        for part in s["allOf"]:
            if "$ref" not in part:
                own.update(merged(part)[0])
        lines += ["Every field of " + " and ".join(link(b) for b in bases) + ", and:", "", "| Field | Type | Description |", "|---|---|---|"]
        lines += list(rows(own))
        lines.append("")
        continue
    props, required = merged(s)
    if props:
        lines += ["| Field | Type | Description |", "|---|---|---|"]
        lines += list(rows(props))
        lines.append("")
    elif s.get("additionalProperties"):
        lines += ["Its fields depend on the kind of output.", ""]

open(os.path.join(out_dir, "reference.md"), "w").write("\n".join(lines).rstrip() + "\n")
with open(os.path.join(out_dir, "openapi.json"), "w") as f:
    json.dump(doc, f, indent=1)
    f.write("\n")
print("wrote reference.md and openapi.json:", len(doc["paths"]), "routes,", len(schemas), "objects")
