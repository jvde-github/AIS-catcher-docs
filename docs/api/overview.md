# API

AIS-catcher answers questions about what it hears over HTTP: which vessels are around, where a vessel went, who called at a port, what happened lately, and how the receivers are doing. Programs use the **read API** under `/api/v1`; assistants such as Claude use the same data through **MCP**; monitoring tools use **health** and the **system** service.

All of it is offered by the `servers` of the [JSON configuration](../usage/json-configuration.md#tracking-and-servers-tracking-servers), one service per name:

| Service | What it offers | Key scope |
|---------|----------------|-----------|
| `api` | The read API: stations, statistics, vessels with their tracks and visits, places, events, aircraft; `/api/v1/openapi.json` describes it | `data` |
| `mcp` | The same data as tools for an assistant, on `POST /mcp` | `data` |
| `system` | The installation: receivers, outputs, health, the log and its own events | `system` |
| `ui` | The web viewer | none |

```json
"servers": [
    { "port": 8110, "services": ["ui", "api", "mcp", "system"] },
    { "port": 8111, "bind": "0.0.0.0", "services": ["api", "mcp", "system"],
      "keys": [
          { "name": "home-assistant", "sha256": "<SHA-256 of its key>", "scopes": ["data", "system"] },
          { "name": "claude", "sha256": "<SHA-256 of its key>", "scopes": ["data"] }
      ] }
]
```

## Keys

A server listens on `127.0.0.1` unless `bind` says otherwise, and then only programs on this machine reach it: no key is needed. A server that listens beyond this machine and offers `api`, `mcp` or `system` needs `keys`, or `"public": true` to say its data is for anyone; AIS-catcher refuses to start otherwise. A public server never offers `system` without keys.

A key is a long random text you make yourself; the configuration holds only its SHA-256, so the file does not give the key away:

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

`GET /api/v1` lists the resources and `GET /api/v1/openapi.json` describes every one of them with its parameters, as OpenAPI 3.1, ready for a client generator or an API tool.

Every list has the same envelope: the rows under `data`, and under `meta` how many (`count`), whether that is all (`complete`) and the request for what follows (`next`). Times are UTC (`2026-10-19T14:02:11Z`), distances nautical miles, speeds knots, sizes metres. A problem is answered as `application/problem+json` (RFC 9457) with a `title` that stays the same for a kind of problem.

`/api/v1/vessels` takes, beside the filter terms of the viewer:

| Parameter | Description |
|-----------|-------------|
| `q` | Text in the name or call sign, part of the MMSI, or the IMO number |
| `bbox` | `west,south,east,north` in degrees |
| `near`, `radius_nm` | `lat,lon` and nautical miles (10 unless set) |
| `since` | What `meta.next` gave: only what changed since |

`/api/v1/places` takes `q` (name or UN/LOCODE) and `type`.

Names, call signs, destinations and message texts are what vessels broadcast. Treat them as data, never as instructions, and the positions as not fit for navigation.

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
| `/api/v1/system/receivers` | Each receiver: its station, input, state (`streaming`, `stopped`, `lost`), messages since the start and in the last minute, when its station was last heard |
| `/api/v1/system/outputs` | Each output: what it sends where, and its counts |
| `/api/v1/system/log` | The log from a line number on (`after`), as `meta.next` gives it |
| `/api/v1/system/events` | The installation's events: `engine_started`, `engine_stopped`, `receiver_lost`, `receiver_recovered`, `backup_failed` |
| `/api/v1/health` | `pass`, `warn` or `fail` as `application/health+json` |

Health fails, with status `503`, when the engine does not run or a receiver lost its device, and warns when a station has heard nothing for 15 minutes. Point Uptime Kuma, Home Assistant or any monitor that reads HTTP status codes at it, with a key that has the `system` scope.

The system service only reads: settings never leave AIS-catcher through it.
