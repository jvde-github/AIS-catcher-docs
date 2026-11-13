# Configuration File

A configuration file holds the same settings as the command line, written as JSON. Load it with `-C`:

```bash
AIS-catcher -C config.json
```

`-C` reads the file where it stands on the command line, so other switches can go with it: `AIS-catcher -C config.json -v 10`. To start from a command line you already use, let `-J` write the file for you: see [Command Line](cli.md#from-the-command-line-to-a-file).

## A complete example

One RTL-SDR, a web viewer on port 8100, a UDP output and the community feed:

```json
{
  "config": "aiscatcher",
  "version": 1,
  "sharing": true,
  "receiver": [
    { "input": "rtlsdr", "rtlsdr": { "tuner": "auto", "rtlagc": true } }
  ],
  "server": [
    { "port": 8100, "station": "My station", "lat": 52.1, "lon": 4.3 }
  ],
  "udp": [
    { "host": "192.168.1.20", "port": 10110, "description": "Chart plotter" }
  ]
}
```

Every file starts with `"config": "aiscatcher"` and `"version": 1`. With nothing else, AIS-catcher picks a receiver as it does on the command line.

## The rules

- **Keys are lowercase**, and case-sensitive.
- **Outputs are lists**: `udp`, `tcp`, `http` and the others take one entry per output.
- **`"active": false`** switches a section off and keeps its settings. Leave it out and the section is on.
- **A value can be a number or a string**: `10110` and `"10110"` are the same.

## The main section

| Key | What it holds | Reference |
|-----|---------------|-----------|
| `config`, `version` | `"aiscatcher"` and `1`; required | |
| `receiver` | The receivers, one object each | [below](#receivers-receiver) |
| `stations` | Where the antennas stand | [below](#stations-stations) |
| `sharing`, `sharing_key` | The community feed | [Community Feed](../configuration/output/community-feed.md) |
| `screen`, `verbose`, `verbose_time` | What the screen shows | [Console Output](../configuration/output/console.md) |
| `udp`, `tcp`, `tcp_listener` | UDP, TCP client and TCP server outputs | [UDP](../configuration/output/UDP.md), [TCP client](../configuration/output/TCP-client.md), [TCP server](../configuration/output/TCP-server.md) |
| `http`, `mqtt` | HTTP and MQTT outputs | [HTTP](../configuration/output/HTTP.md), [MQTT](../configuration/output/MQTT.md) |
| `db` | Databases | [Database](../configuration/output/PSQL.md) |
| `server` | Web viewers | [Web Viewer](../configuration/output/web-viewer.md) |
| `tracking`, `services` | The ship tracker and the servers that read it | [below](#tracking-and-services-tracking-services) |
| `webhooks` | Addresses each event is posted to | [Webhooks](../api/webhooks.md) |
| `mqtt_state` | The station's state on an MQTT broker | [Home Assistant](../api/home-assistant.md) |

The generated [Configuration Keys](../references/config-keys.md) list every key with its type, default and values.

## Receivers (`receiver`)

Each entry of `receiver` is one receiver. `input` picks the kind of device, and a section of the same name holds its settings:

```json
{
  "config": "aiscatcher",
  "version": 1,
  "receiver": [
    { "input": "rtlsdr", "serial": "00000001", "description": "Mast" },
    { "input": "rtlsdr", "serial": "00000002", "description": "Mast, long range",
      "channel": "CD", "engines": [ { "type": "v1_high" } ] }
  ]
}
```

| Key | What it does | Reference |
|-----|--------------|-----------|
| `input` | The kind of device: `rtlsdr`, `airspy`, `serialport`, `udpserver` and so on | [Inputs](../configuration/input/overview.md) |
| `serial` | Picks one device of that kind by its serial number | |
| `description` | The receiver's name in the viewer and the statistics | |
| `station` | The number of the station in `stations` it stands at | [Stations](#stations-stations) |
| `lat`, `lon` | Its position, when it names no station | |
| `channel` | `AB`, the standard pair, or `CD`, the long-range pair | [Long Range AIS](../advanced/long-range.md) |
| `sample_rate`, `bandwidth`, `freqoffset` | The settings every SDR has | [Inputs](../configuration/input/overview.md) |
| `engines` | The decoders, each `{ "type": ... }` with optional `settings` | [Decoding](../configuration/model.md), [Engines](../references/config-keys.md#engines) |
| `verbose`, `meta`, `own_mmsi` | Statistics on the screen, extra metadata, the station's own MMSI | [Console Output](../configuration/output/console.md) |
| `rtlsdr`, `airspy`, … | The device section matching `input` | [Inputs](../configuration/input/overview.md) |

A device section configures a device but does not select it: `input` does. A single receiver can also stand in the main section itself, as `-J` writes it: `"rtlsdr": { ... }` at the top level.

## Stations (`stations`)

A station is where an antenna stands. Every ship's distance and bearing, and the range figures, are measured from the station that heard the ship, so receivers at different places each measure from their own. The viewer's own `lat` and `lon` are only used for a receiver that has no position.

Each entry of `stations` has a number and may have a name, a position and an altitude:

| Key | Type | Description |
|-----|------|-------------|
| `id` | number | Unique; what a receiver names in its `station` key. `0` is the **default station**: where every receiver stands that names none |
| `name` | string | Shown in the viewer; `Station <id>` when left out |
| `lat`, `lon` | number | Decimal degrees; both or neither |
| `alt` | number | Height of the antenna in metres |
| `mmsi` | number | The vessel the station is on: it is wherever that vessel last reported, and `gps` does not apply |
| `gps` | boolean | Whether GPS sentences move the station; off unless set to `true`. Its `lat` and `lon` are then where it stands until the first fix |
| `share_loc` | boolean | Whether the station's position may leave this machine, for a server that does not say so itself with its own `share_loc`. Off unless set: no server, API or map then shows where it is, nor which vessel it rides, nor how far or in which direction a vessel it heard lies from it. The station's own range figures (furthest vessel, maximum distance, radar) still go to its owner: a browser on the station itself, or an API key with system scope. Which vessels a station hears still hints at its general area |

A message that names a station itself, as a feed from a hub does in its tag block, counts at that station when `stations` lists it, else at the input's.

Stations are optional. A receiver that names none stands at the default station, 0: list it to give it a name and a position like any other, or leave it out and it is made when the run starts, named after the one receiver standing on it when that has a `description`, else after the viewer's `station`, and placed where a receiver with `lat` and `lon` of its own is, else where the viewer section puts it (`lat`, `lon`, `alt`, `share_loc`, `use_gps`, `own_mmsi`). A receiver may also say `"station": 0`. Once the file has a `stations` list, every message carries the number of its station as `station_id`, 0 included. An engine of a receiver may carry a station of its own (`"settings": { "station": 2 }`, `-go station 2` on the command line), so two decoders of one input are told apart: each then has its own figures, and **Plots → Compare** sets one against the other.

```json
{
    "config": "aiscatcher",
    "version": 1,
    "stations": [
        { "id": 1, "name": "Harbour mast", "lat": 52.10, "lon": 4.27, "alt": 20 }
    ],
    "receiver": [
        { "input": "rtlsdr", "serial": "ab", "station": 1 },
        { "input": "rtlsdr", "serial": "cd", "station": 1, "channel": "CD" },
        { "input": "udpserver", "udpserver": { "port": 10110 }, "description": "Pier" }
    ]
}
```

Here the two dongles share the antenna on the harbour mast, and the UDP input stands at the default station, named after it. The log lists what each receiver became:

```
Receiver 1: station 1 "Harbour mast" at 52.099998, 4.270000
Receiver 2: station 1 "Harbour mast" at 52.099998, 4.270000
Receiver 3: station 0 "Pier", no position
```

**A station that moves.** A receiver on a boat, or one with a GPS attached, does not stay where the file puts it. A station's position comes from one source at a time: the vessel its `mmsi` names, else GPS when `gps` is `true`, else its `lat` and `lon`.

- A station with an `mmsi` rides that vessel: each position the vessel reports, heard by any receiver, moves the station there.
- A station with `"gps": true` moves with the GPS sentences (`$GPRMC`, `$GPGGA` and the like) arriving on the inputs of the receivers that name it. When no receiver names it, GPS on any input moves it.
- The default station, when the file does not list it, moves with GPS on the inputs standing on it unless the viewer's `use_gps` is off; listed, it follows its own `gps` like any other.
- The position in the file is where a moving station starts, until the first fix. Ships are measured from where the station was when it heard them. The last fix is kept in the tracking backup, so a restart does not send a station back to its configured position.

These apply to the stations of the tracker and the services [below](#tracking-and-services-tracking-services), which report each station's position with its source (`configured`, `gps` or `vessel`) and the time of the last fix. The viewer under `server` keeps its own single position, set by `lat`, `lon`, `use_gps` and `own_mmsi` as before.

## Tracking and services (`tracking`, `services`)

AIS-catcher keeps one picture of everything its receivers hear, the **tracker**, and offers it through **services**: a list of servers, each a port and what it serves: the web viewer, the API, MCP, the system service, GeoJSON, Prometheus. The tracker is built when the file has a server; without one nothing is kept. The viewer of `-N` and of a `server` section is such a server too. Both are part of the standard builds; a build made with `cmake -DAPI=OFF` leaves them out and refuses these keys.

```json
{
    "config": "aiscatcher",
    "version": 1,
    "stations": [ { "id": 1, "name": "Harbour mast", "lat": 52.10, "lon": 4.27 } ],
    "receiver": [ { "input": "rtlsdr", "station": 1 } ],
    "tracking": { "file": "/var/lib/ais-catcher/tracking.bin", "backup": 10 },
    "services": [
        { "port": 8110, "api": true },
        { "port": 8111, "bind": "0.0.0.0", "ui": false, "api": true,
          "view": { "hidden_buckets": ["bm", "bs"], "seen": 30, "track_time": 3600 } },
        { "port": 8112, "tracking": { "allow_type": "1,2,3", "history": 3600 } }
    ]
}
```

`tracking`, all optional:

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `file` | string | none | Backup of ships, statistics, events and station fixes, read at start and written on exit. A backup an earlier version wrote (the `file` of `server`, or of `-N`) is copied once to `<file>.before-upgrade`, imported, and from then on written over in this version's format. To go back to the earlier version, rename the copy back to the file's name |
| `backup` | number | 10 | Minutes between backups to `file`; 0 writes only on exit |
| `history` | number | 1800 | Seconds a ship is kept after its last message |
| `track_time` | number | 3600 | Seconds of track kept per ship; 0 is no limit |
| `max_ships` | number | 4096 | Size of the ship table |
| `cutoff` | number | 2500 | Distance in nautical miles beyond which a ship does not count towards range |
| `track_memory` | number | 1024 | Kilobytes of track kept per ship |
| `expire` | boolean | false | Forget a ship's details when it leaves |
| `lat`, `lon` | number | none | Where a message from no known station is measured from |
| `places` | string | none | A directory of [place files](../configuration/output/places.md): the tracker then keeps every ship's visits, as the viewer does with its own `places` |

Each entry of `services`, one server:

| Key | Type | Description |
|-----|------|-------------|
| `port` | number | Required; one server per port |
| `active` | boolean | `false` switches the server off: it keeps its settings, which are still checked, but opens no port and keeps no ships. On unless set |
| `bind` | string | Address to listen on; `127.0.0.1` unless set, so a server is reachable from other machines only when you say so. Beyond this machine, a server with `api`, `mcp` or `system` needs `keys` or `public` |
| `ui` | boolean | The web viewer, on unless set `false`; with it the viewer's own options (`realtime`, `station`, `station_link`, `mbtiles`, …), see [Web Viewer](../configuration/output/web-viewer.md) |
| `api` | boolean | The read API under `/api/v1`: stations, statistics, vessels with their tracks and visits, places with the ships inside and their visits, aircraft, and events. See [API](../api/overview.md). A server limited to some `stations` serves no aircraft, as aircraft are not kept by station |
| `mcp` | boolean | The same for an assistant, at `/mcp` |
| `system` | boolean | Receivers, outputs, health and the log, under `/api/v1/system` |
| `geojson` | boolean | The ships as GeoJSON at `/geojson` |
| `metrics` | boolean | Message counts for Prometheus at `/metrics`; `prome` says the same |
| `share_loc` | boolean | Whether this server shows where the stations are: their positions, each vessel's distance and bearing, and the range. A server that does not say goes by each station's own `share_loc` |
| `limited` | boolean | The short form for whoever asks: lists of 25 rows at most, vessel rows without the station, one vessel in full without its stations, and 25 data calls an hour from one address. Off unless set |
| `tracking` | object | Ships of the server's own, behind a filter on the messages: the terms of an output's filter (`allow_type`, `block_mmsi`, `stations`, `unique`, …) and `zone` or `groups_in` for the receivers that feed it, with `history` and `track_time` for what it keeps. The backup and the places are the site's. Without it the server reads the site's tracker. A server whose filter names stations (`stations`, or `id` on the command line) shows those stations alone: their markers, pages and figures |
| `keys` | array | The keys the server accepts, each `{ "name", "sha256", "scopes" }`: see [Keys](../api/overview.md#keys) |
| `public` | boolean | Its data is for anyone, without a key; never its `system` |
| `view` | object | Which ships this server shows of what its tracker keeps, and how far back: `stations`, `mmsi_allow`, `mmsi_deny`, `hidden_buckets`, `hidden_classes`, `hidden_statuses`, `speed_min`, `speed_max`, `distance_min`, `distance_max`, `seen` (minutes since heard), `validated`, `repeated`, `track_time` (seconds of track served, at most what the tracker keeps), and `place_geometry` (`false` serves places with their marker position only, keeping their outlines on this machine; on unless set). What it leaves out no route of the server sends: the map, the API, MCP and GeoJSON. A view never makes a tracker; only a message filter does (`filter` on with its terms, or `zone`, `groups_in`). Leave it out to show all |

A viewer under `server`, and `-N` on the command line, is read as an entry of `services`: the same server, with the same keys. One without a message filter shows the site's ships, and its `file`, `backup` and `history` are the site's `tracking`; one with `filter` on, or with `zone` or `groups_in`, keeps ships of its own behind that filter, as the viewer always did, while the backup stays the site's. On the command line the switches follow the port: `AIS-catcher -N 8100 api on mcp on`.

**The filter** uses the terms of the web viewer's own filter (**Settings → Filter** on the map), under the same names, so a filter you set up in the viewer can be copied here as it stands. It selects from everything the tracker keeps: the server shows nothing outside it, in any list, count or event.

| Term | Type | Description |
|------|------|-------------|
| `stations` | array | Only ships one of these stations heard in the last hour; `0` is a ship no listed station heard |
| `hidden_buckets` | array | Groups left out: `am`, `as` (class A moving, stationary), `bm`, `bs` (class B), `aton`, `base`, `sarte`, `air` |
| `hidden_classes` | array | Ship classes left out, by number: 2 cargo, 3 class B, 4 passenger, 5 special, 6 tanker, 7 high-speed, 8 fishing, 0 everything else |
| `hidden_statuses` | array | Navigational statuses left out, 0 to 15; 15 is also a status not reported |
| `speed_min`, `speed_max` | number | Knots; a ship without a speed falls outside either |
| `seen` | number | Heard within this many minutes; 0 is any age |
| `distance_min`, `distance_max` | number | Nautical miles from the station that heard the ship |
| `validated` | string | `any`, `yes`, `no` or `pending` |
| `repeated` | string | `any`, `only` (passed on by a repeater) or `never` |
| `mmsi_allow`, `mmsi_deny` | array | Only these MMSIs; never these |

A request to `/api/v1/vessels` takes [filters of its own](../api/overview.md#vessels), named after the fields of a vessel (`?class=cargo,tanker&min_speed_kn=1`). They narrow what the server shows and never widen it.
