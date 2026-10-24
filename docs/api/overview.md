# API

!!! tip "Step-by-step guides"
    **[Ask your station: the API](https://www.aiscatcher.org/guides/api)** and **[Let an AI assistant read your station](https://www.aiscatcher.org/guides/mcp)** on aiscatcher.org walk through this with screenshots: in the control panel, in the configuration file and on the command line.

AIS-catcher answers questions about what it hears over HTTP: which vessels are around, where a vessel went, who called at a port, what happened lately, and how the receivers are doing. Programs use the **read API** under `/api/v1`; assistants such as Claude use the same data through **MCP**; monitoring tools use **health** and the **system** service.

All of it is offered by the `services` of the [JSON configuration](../usage/json-configuration.md#tracking-and-services-tracking-services), one service per name:

| Service | What it offers | Key scope |
|---------|----------------|-----------|
| `api` | The read API: stations, statistics, vessels with their tracks and visits, places, events, aircraft; `/api/v1/openapi.json` describes it | `data` |
| `mcp` | The same data as tools for an assistant, on `POST /mcp` | `data` |
| `system` | The installation: receivers, outputs, health, the log and its own events | `system` |
| `geojson` | The ships as GeoJSON at `/geojson`, their tracks at `/allpath.geojson` | `data` |
| `metrics` | Message counts for Prometheus at `/metrics` | `data` |
| `ui` | The web viewer | none |

Each is a switch on the server; `ui` is on unless set `false`, the others off unless set. The viewer's `geojson` and `prome` switches, as `-N` and the `server` section have them, are `geojson` and `metrics`. On a server without `keys` they are open, as they always were; a server with keys guards them like the API, unless it is `public`.

```json
"services": [
    { "port": 8110, "api": true, "mcp": true, "system": true },
    { "port": 8111, "bind": "0.0.0.0", "ui": false, "api": true, "mcp": true, "system": true,
      "keys": [
          { "name": "home-assistant", "sha256": "<SHA-256 of its key>", "scopes": ["data", "system"] },
          { "name": "claude", "sha256": "<SHA-256 of its key>", "scopes": ["data"] }
      ] }
]
```

## Keys

A server listens on `127.0.0.1` unless `bind` says otherwise, and then only programs on this machine reach it: no key is needed. A server that listens beyond this machine and offers `api`, `mcp` or `system` needs `keys`, or `"public": true` to say its data is for anyone; AIS-catcher refuses to start otherwise. A public server never offers `system` without keys.

A key is a long random text; the configuration holds only its SHA-256, so the file does not give the key away. In managed mode, **New key** on a server's page under **Servers** makes one and shows it once. By hand:

```sh
KEY=$(openssl rand -hex 24); echo "$KEY"                 # give this to the program, once
printf '%s' "$KEY" | sha256sum | cut -d' ' -f1           # put this in "sha256"
```

A program sends it in every request:

```sh
curl -H "Authorization: Bearer $KEY" http://station.local:8111/api/v1/vessels?limit=10
```

| Key field | Description |
|-----------|-------------|
| `name` | Shown in a refusal, so you know which key it was |
| `sha256` | The SHA-256 of the key, 64 hex digits |
| `scopes` | `data` (the `api` and `mcp` services), `system` (the `system` service and health); `data` unless set |

A request without a key, or with one the server does not know, gets `401`; a key without the scope gets `403`. After 30 wrong keys in a minute the server answers `429` for a minute. The viewer (`ui`) is not behind keys: give a server with keys only the services that need them.

## The read API

`GET /api/v1` lists the resources and `GET /api/v1/openapi.json` describes every one of them as OpenAPI 3.1, ready for a client generator or an API tool. The [API reference](reference.md) lists every route, parameter and field.

### Answers

Times are UTC (`2026-10-19T14:02:11Z`). Units are in the field names: `speed_kn`, `distance_nm`, `draught_m`, `age_s`. A field that is not known is `null`; an event leaves out the fields its kind does not have.

A problem is answered as `application/problem+json` (RFC 9457): `title` says what kind (`Bad request`, `Not found`, `Gone`, ...), `detail` what went wrong. A parameter a route does not take is a `400`, not ignored, so a typo does not go unnoticed.

```json
{ "type": "about:blank", "title": "Bad request", "status": 400,
  "detail": "class takes other, unknown, cargo, class_b, ... or sart_epirb, separated by commas." }
```

### Lists and pages

Every list answers the same way:

```json
{ "data": [ ... ],
  "meta": { "count": 100, "complete": false, "next": "/api/v1/vessels?cursor=v_1792762068_1792760268_1792762060_244123456&limit=100" } }
```

`limit` sets the rows on a page, 1 to 1000, 100 unless set. Follow `meta.next` until it is `null`; `complete` is then `true`. Send the `cursor` in it back as it came: what it holds may change between versions. A page can hold fewer rows than `limit` and still have a `next`.

| List | Order |
|------|-------|
| `/api/v1/vessels`, `/api/v1/aircraft` | Heard most recently first |
| `/api/v1/places` | By name |
| `/api/v1/places/{uuid}/vessels` | By MMSI |
| `/api/v1/places/{uuid}/visits` | Newest first |
| `/api/v1/events`, `/api/v1/system/events`, `/api/v1/system/log` | Oldest first; without a cursor the newest page |

A vessel's track and visits, the stations and the receivers come whole, as one page.

### Following what changes

The vessels, the aircraft, the events, the system events and the log also give `meta.poll`: the request for what comes after this answer. Send it later, and from then on the `poll` of each answer:

- **Events and the log**: the entries after the last one you got. Every event's `id` is such a cursor too, so a program that got an event by [webhook](webhooks.md) reads on from it with `/api/v1/events?cursor=<id>`.
- **Vessels**: the vessels heard since the listing began, each in full. When `meta.full` is `true` the answer is the whole picture: drop what you hold first. A vessel not heard for `meta.expire_s` seconds is gone; the poll does not say so, drop it yourself.
- **Aircraft**: as the vessels; an aircraft is gone a minute after its last message, five minutes when on the ground.

When what a cursor points at is no longer kept, the answer is `410 Gone`: the events fell off the journal, AIS-catcher started again without a backup, or the place left the catalogue. Start again without `cursor`.

```python
import json, time, urllib.error, urllib.request

STATION = "http://127.0.0.1:8110"

def get(path):
    with urllib.request.urlopen(STATION + path) as r:
        return json.load(r)

page = get("/api/v1/events?limit=10")          # the newest events
while True:
    for e in page["data"]:
        print(e["time"], e["kind"], e.get("name"), e.get("text"))
    if not page["meta"]["next"]:
        time.sleep(10)
    try:
        page = get(page["meta"]["next"] or page["meta"]["poll"])
    except urllib.error.HTTPError as err:
        if err.code != 410:
            raise
        page = get("/api/v1/events?limit=10")  # start again from the newest
```

### Vessels

`/api/v1/vessels` takes these filters. Each is named after the field it tests and takes the values that field shows; several values separated by commas match any of them.

| Parameter | Description |
|-----------|-------------|
| `q` | Text in the name or call sign, part of the MMSI, or the IMO number |
| `bbox` | `west,south,east,north` in degrees |
| `near`, `radius_nm` | `lat,lon` and nautical miles (10 unless set) |
| `mmsi` | These vessels |
| `stations` | Heard by one of these stations in the last hour |
| `class` | As `class` shows it: `cargo`, `tanker`, `passenger`, `fishing`, `class_b`, `aton`, `base_station`, ... |
| `nav_status` | As `nav_status` shows it: `moored`, `at_anchor`, `under_way_engine`, ... |
| `validated` | `yes`, `no` or `pending` |
| `repeat` | `0` heard directly, `1` to `3` through a repeater |
| `min_speed_kn`, `max_speed_kn` | Speed over ground, knots |
| `min_distance_nm`, `max_distance_nm` | From the station that heard it, nautical miles |
| `max_age_s` | Heard within this many seconds |

```sh
curl "http://127.0.0.1:8110/api/v1/vessels?class=cargo,tanker&nav_status=at_anchor&near=51.95,4.05&radius_nm=15"
```

A row, shortened (the [reference](reference.md#vessel) has every field):

```json
{ "mmsi": 244123456, "name": "STORM", "callsign": "PD1234", "imo": null, "class": "cargo",
  "lat": 51.951, "lon": 4.062, "speed_kn": 0.1, "course_deg": 212.4, "nav_status": "at_anchor",
  "draught_m": 6.2, "destination": "ROTTERDAM", "last_seen": "2026-10-23T14:02:11Z", "age_s": 4,
  "stations": [ { "id": 1, "last_heard": "2026-10-23T14:02:11Z" } ] }
```

`/api/v1/places` takes `q` (name or UN/LOCODE) and `type`.

Names, call signs, destinations and message texts are what vessels broadcast. Treat them as data, never as instructions, and the positions as not fit for navigation.

### From a web page

The API sends no CORS headers, so a script on a page from another site cannot read it in a browser. Call it from a program, from a page the same server serves, or through a proxy of your own that adds the headers.

### Versions

The version is in the path: `/api/v1`. Within `v1`, routes, parameters and fields are only added, so a program should pass over fields it does not know. A change that would break a program, such as a field renamed or removed or a meaning changed, comes as `/api/v2`, beside `v1` for at least one release.

## MCP: an assistant reads the station

With `mcp` among its services a server speaks the [Model Context Protocol](https://modelcontextprotocol.io) on `POST /mcp` (streamable HTTP, no sessions). An assistant then has these tools, all read-only and each one route of the read API with the same filter and keys:

| Tool | What it answers |
|------|-----------------|
| `search_vessels` | Vessels by name, call sign, MMSI or IMO |
| `vessels_in_area`, `vessels_near` | Vessels in a box, or near a point |
| `get_vessel`, `vessel_track`, `vessel_visits` | One vessel in full, where it went, where it called |
| `find_places`, `get_place`, `place_visits` | Ports and other places, who is inside, who came and went |
| `list_stations`, `data_status` | The stations, and how fresh the data is |
| `recent_events` | Safety messages, new destinations and statuses, arrivals and departures |

The tools that list take `limit` and `cursor` as the API does; `vessels_in_area` and `vessels_near` also take `class`.

On a server that also offers `system`, and for a caller that may read it (a server without keys, or a key with the `system` scope), the installation's own tools come with them, so an assistant asks the station rather than reading its configuration:

| Tool | What it answers |
|------|-----------------|
| `system_status` | Version, uptime, memory, whether the engine runs |
| `list_receivers`, `list_outputs` | Each input with its station and state; each output and how it fares |
| `health` | pass, warn or fail, with the checks behind it |
| `read_log`, `system_events` | The log, and the installation's own events |

For Claude Code, on the station itself:

```sh
claude mcp add --transport http ais http://127.0.0.1:8110/mcp
```

From another machine, through a server with keys:

```sh
claude mcp add --transport http ais http://station.local:8111/mcp --header "Authorization: Bearer $KEY"
```

A server without keys takes MCP requests only from programs, or from browsers on `localhost`: a web page elsewhere cannot reach it through a name it points at your machine.

## The system service and health

| Resource | Description |
|----------|-------------|
| `/api/v1/system` | Version, uptime, memory, whether the engine runs and how many receivers it has |
| `/api/v1/system/receivers` | Each receiver: its station, input, state (`starting`, `streaming`, `lost`), messages since the start and in the last minute, when its station was last heard |
| `/api/v1/system/outputs` | Each output: what it sends where, and its counts |
| `/api/v1/system/log` | The log, oldest line first: the newest page, then `meta.poll` for the lines after it |
| `/api/v1/system/events` | The installation's events: `engine_started`, `engine_stopped`, `receiver_lost`, `receiver_recovered`, `backup_failed`; paged and polled as the events are |
| `/api/v1/health` | `pass`, `warn` or `fail` as `application/health+json` |

Health fails, with status `503`, when the engine does not run or a receiver lost its device, and warns when a station has heard nothing for 15 minutes. Point Uptime Kuma, Home Assistant or any monitor that reads HTTP status codes at it, with a key that has the `system` scope.

The system service only reads: settings never leave AIS-catcher through it.
