# JSON Configuration

AIS-catcher (v0.41+) supports extensive configuration through JSON files. This guide describes the JSON structure, key settings, and common patterns.

To start AIS-catcher with a JSON configuration file, use the `-C` option followed by the path to your `config.json` file:

```bash
AIS-catcher -C config.json
```
This loads and applies the settings from the JSON file.

## Basic Structure

A JSON configuration file always starts with the configuration header:
```json
{
    "config": "aiscatcher",
    "version": 1
}
```

Where:

- `config`: Identifies the configuration type. Must be `"aiscatcher"`.
- `version`: Configuration version. Currently, only `1` is supported.


This is the absolute minimal structure (just the first two keys). If no receiver is configured, AIS-catcher will use the default behaviour for selecting an input device.

To select the RTL-SDR as an input device:
```json
{
    "config": "aiscatcher",
    "version": 1,
    "receiver": [
        {
            "input": "rtlsdr"
        }
    ]
}
```


> Note: older configurations allowed receiver selection at the root level (e.g. `input`, `serial`). This is legacy and may disappear in a future release. Prefer defining receivers in the `receiver` array. [^legacy-root-receiver]

## Important Notes

- JSON keys are case-sensitive and must be lowercase.
- CLI setting names are not case-sensitive.
- Define receivers in the `receiver` array (even for a single receiver).
- Device sections (e.g. `rtlsdr`, `airspy`, `hydrasdr`) configure the device, but do not select it. Use `input` (and optionally `serial`) inside each receiver object.
- `active` is optional in any section; if omitted, it is assumed to be `true`.
- Outputs like `udp` are arrays to support multiple output channels.

## Configuration Keys

Configuration keys are grouped below by purpose. The complete list of keys the managed hub edits, with types, defaults and ranges, is on [Configuration Keys](../references/config-keys.md).

### General Overview

General (mostly optional) settings define fundamental aspects of AIS-catcher's operation.

#### Root-level keys

| Key | Type | Description | Documentation |
|-----|------|-------------|---------------|
| **General**  |
| `config` | string | "aiscatcher" | |
| `version` | number | 1 | |
| `sharing` | boolean | Enable community feed sharing | [Community Feed](../configuration/output/community-feed.md) |
| `sharing_key` | string | Community feed key | [Community Feed](../configuration/output/community-feed.md) |
| `screen` | number | Screen output mode (0-5), one for all receivers | [Console Output](../configuration/output/console.md) |
| `verbose_time` | number | Verbose update interval in seconds, one for all receivers | [Console Output](../configuration/output/console.md) |
| **Receiver array** |
| `receiver` | array | List of receiver objects (recommended even for a single receiver) [^legacy-root-receiver] | [Receiver configuration](#receiver-configuration-receiver-array) |
| `stations` | array | Where the antennas stand: a number, name, position and altitude for each, and a vessel or GPS when they move | [Stations](#stations-stations-array) |
| `tracking` | object | How the tracker keeps ships: backup file and interval, history, table size | [Tracking and services](#tracking-and-services-tracking-services) |
| `services` | array | Servers reading the tracker: port, address, what each serves and its filter | [Tracking and services](#tracking-and-services-tracking-services) |
| `webhooks` | array | Addresses each event is posted to | [Webhooks](../api/webhooks.md) |
| `mqtt_state` | object | The station's state on an MQTT broker, for Home Assistant | [Home Assistant](../api/home-assistant.md) |
| **Output channels** |
| `server` | array | Web viewer configuration | [Web Viewer](../configuration/output/web-viewer.md) |
| `udp` | array | UDP output configuration | [UDP Output](../configuration/output/UDP.md) |
| `tcp` | array | TCP output configuration (client) | [TCP Output](../configuration/output/TCP-client.md) |
| `tcp_listener` | array | TCP output configuration (server) | [TCP Output](../configuration/output/TCP-server.md) |
| `http` | array | HTTP output configuration | [HTTP Output](../configuration/output/HTTP.md) |
| `mqtt` | array | MQTT output configuration | [MQTT Output](../configuration/output/MQTT.md) |

#### Receiver configuration (`receiver` array)

The root-level `receiver` key contains an array of receiver objects. This is the recommended structure going forward.

##### Receiver object keys

Each entry in the root-level `receiver` array is a receiver object. These keys live *inside* each receiver object:

| Key | Type | Description | Documentation |
|-----|------|-------------|---------------|
| `input` | string | Selects the input device type for this receiver (e.g. `rtlsdr`, `airspy`, `hydrasdr`, `spyserver`, ...) | [Input Overview](../configuration/input/overview.md) |
| `description` | string | A name for the receiver, shown in the viewer's receiver list and statistics | |
| `station` | number | The number of the station in `stations` whose antenna this receiver uses | [Stations](#stations-stations-array) |
| `lat`, `lon` | number | The receiver's position, when it names no station | [Stations](#stations-stations-array) |
| `serial` | string/number | Receiver identifier (recommended; also used to target per-receiver CLI overrides in some setups) | |
| `verbose` | boolean | Enable verbose output for this receiver | [Console Output](../configuration/output/console.md) |
| `meta` | string | Metadata tags (T/D/M) for this receiver | [Console Output](../configuration/output/console.md) |
| `own_mmsi` | number | Own MMSI of receiver station | |
| `<device section>` | object | Device-specific configuration object matching `input` (e.g. `rtlsdr`, `airspy`, `hydrasdr`, ...). See examples in [Input Device Settings](#input-device-settings). | [Input Overview](../configuration/input/overview.md) |
| `model` | object | Decoder model configuration for this receiver | [Model](../configuration/model.md) |

##### Multi-receiver example

Example with two receivers:
```json
{
    "config": "aiscatcher",
    "version": 1,
    "receiver": [
        {
            "input": "airspy",
            "serial": "airspy",
            "airspy": {
                "sample_rate": "3000K"
            }
        },
        {
            "input": "rtlsdr",
            "serial": "ais",
            "rtlsdr": {
                "bandwidth": "192k"
            }
        }
    ]
}
```

In this example, each receiver selects a device via `input`, is optionally named via `serial`, and is configured via its device section (e.g. `rtlsdr`, `airspy`, `hydrasdr`).

#### Stations (`stations` array)

!!! tip "Step-by-step guide"
    **[Locate your station](https://www.aiscatcher.org/guides/station)** on aiscatcher.org walks through this with screenshots: in the control panel, in the configuration file and on the command line.

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
| `share_loc` | boolean | Whether the station's position may leave this machine. Off unless set: no server, API or map then shows where it is, nor which vessel it rides |

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

In managed mode the **Stations** page edits this list. Its first entry is the default station, always there under number 0, which cannot be deleted; every other station is numbered from 1. An input picks its station from the list on its own page, or creates one there. A file from before the default station was listed keeps working: the panel shows it from the viewer section's `station`, `lat`, `lon`, `share_loc`, `use_gps` and `own_mmsi`, and moves them into `stations` the first time Stations is saved.

**A station that moves.** A receiver on a boat, or one with a GPS attached, does not stay where the file puts it. A station's position comes from one source at a time: the vessel its `mmsi` names, else GPS when `gps` is `true`, else its `lat` and `lon`.

- A station with an `mmsi` rides that vessel: each position the vessel reports, heard by any receiver, moves the station there.
- A station with `"gps": true` moves with the GPS sentences (`$GPRMC`, `$GPGGA` and the like) arriving on the inputs of the receivers that name it. When no receiver names it, GPS on any input moves it.
- The default station, when the file does not list it, moves with GPS on the inputs standing on it unless the viewer's `use_gps` is off; listed, it follows its own `gps` like any other.
- The position in the file is where a moving station starts, until the first fix. Ships are measured from where the station was when it heard them. The last fix is kept in the tracking backup, so a restart does not send a station back to its configured position.

These apply to the stations of the tracker and the services [below](#tracking-and-services-tracking-services), which report each station's position with its source (`configured`, `gps` or `vessel`) and the time of the last fix. The viewer under `server` keeps its own single position, set by `lat`, `lon`, `use_gps` and `own_mmsi` as before.

#### Tracking and services (`tracking`, `services`)

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
| `port` | number | Required; one server per port. Not on the entry marked `main` |
| `main` | boolean | Managed mode (`-E`): the server beside the control panel, on its port, the map always on; one entry, which also takes the viewer's options |
| `active` | boolean | `false` switches the server off: it keeps its settings, which are still checked, but opens no port and keeps no ships. The main server always serves. On unless set |
| `bind` | string | Address to listen on; `127.0.0.1` unless set, so a server is reachable from other machines only when you say so. Beyond this machine, a server with `api`, `mcp` or `system` needs `keys` or `public` |
| `ui` | boolean | The web viewer, on unless set `false`; with it the viewer's own options (`realtime`, `station`, `station_link`, `mbtiles`, …), see [Web Viewer](../configuration/output/web-viewer.md) |
| `api` | boolean | The read API under `/api/v1`: stations, statistics, vessels with their tracks and visits, places with the ships inside and their visits, aircraft, and events. See [API](../api/overview.md). A server limited to some `stations` serves no aircraft, as aircraft are not kept by station |
| `mcp` | boolean | The same for an assistant, at `/mcp` |
| `system` | boolean | Receivers, outputs, health and the log, under `/api/v1/system` |
| `geojson` | boolean | The ships as GeoJSON at `/geojson` |
| `metrics` | boolean | Message counts for Prometheus at `/metrics`; `prome` says the same |
| `station_id` | number or array | The stations this server is about: its `view` shows only them, as `"view": { "stations": [...] }` says it too, and its live streams (NMEA, signal, Prometheus counts) carry only their messages; a `server` section, or `-N`, lists the first from its own station keys where `stations` does not have it |
| `tracking` | object | Ships of the server's own, behind a filter on the messages: the terms of an output's filter (`allow_type`, `block_mmsi`, `stations`, `unique`, …) and `zone` or `groups_in` for the receivers that feed it, with `history` and `track_time` for what it keeps. The backup and the places are the site's. Without it the server reads the site's tracker |
| `keys` | array | The keys the server accepts, each `{ "name", "sha256", "scopes" }`: see [Keys](../api/overview.md#keys) |
| `public` | boolean | Its data is for anyone, without a key; never its `system` |
| `view` | object | Which ships this server shows of what its tracker keeps, and how far back: `stations`, `mmsi_allow`, `mmsi_deny`, `hidden_buckets`, `hidden_classes`, `hidden_statuses`, `speed_min`, `speed_max`, `distance_min`, `distance_max`, `seen` (minutes since heard), `validated`, `repeated`, and `track_time` (seconds of track served, at most what the tracker keeps). What it leaves out no route of the server sends: the map, the API, MCP and GeoJSON. A view never makes a tracker; only a message filter does (`filter` on with its terms, or `zone`, `groups_in`). Leave it out to show all |
| `place_geometry` | boolean | Serve the outlines of places; `false` keeps them on this machine, and places are served with their marker position only. On unless set |

In managed mode (`-E`) the **Services** tab edits these: the built-in viewer beside the control panel first, then each server of `services`, with **Add server** for another. Each server's page switches its services on and off, says whether it listens on this machine or the network, gives its keys (**New key** makes one, shows it once, and keeps only its SHA-256), and, with the viewer on, the viewer's own settings. A saved server whose port another program has is marked as not listening. **Try the API** sends a request to any of them as a program would, made on the station itself, with the key given, and shows the answer and the curl line that repeats it; under **MCP** it lists a server's tools, calls one with its arguments as an assistant would, and gives the line that connects Claude Code to it. How long ships and tracks are kept, and the backup, are under **System › Settings › History & backup**. The built-in viewer is the entry marked `main`: it always serves the map, may switch on `api`, `mcp`, `system`, `geojson` and `metrics`, and takes `keys` and `public` as any server does, following the address the control panel listens on. A saved change to the servers applies at once, also while the receivers are stopped; a server cannot take the control panel's port or the viewer's.

A viewer under `server`, and `-N` on the command line, is read as an entry of `services`: the same server, with the same keys. One without a message filter shows the site's ships, and its `file`, `backup` and `history` are the site's `tracking`; one with `filter` on, or with `zone` or `groups_in`, keeps ships of its own behind that filter, as the viewer always did, while the backup stays the site's. On the command line the switches follow the port: `AIS-catcher -N 8100 api on mcp on`.

**The filter** uses the terms of the viewer's own filter (**Settings → Filter**), under the same names, so a filter you set up in the viewer can be copied here as it stands. It selects from everything the tracker keeps: the server shows nothing outside it, in any list, count or event.

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

[^legacy-root-receiver]: Legacy configurations may use root-level `input` / `serial` to define a single receiver. This still works in some versions, but is discouraged and may be removed in a future release. Prefer putting `input` (and `serial`) inside each receiver object under `receiver`.

## Input Device Settings

AIS-catcher supports various input devices. Each device type has specific configuration options. Below are the supported devices and their respective settings. The documentation of the relevant keys can be found in the [Configuration](../configuration/input/overview.md) sections. Below we provide a few examples.

### RTL-SDR (`rtlsdr`)
<details>
<summary>Example</summary>

```json
{
    "rtlsdr": {
        "active": true,
        "rtlagc": true,
        "tuner": "auto",
        "bandwidth": "192K",
        "sample_rate": "1536K",
        "biastee": false
    }
}
```
</details>
[Full RTL-SDR Documentation](../configuration/input/rtlsdr.md)

### Airspy (`airspy`)
<details>
<summary>Example</summary>
```json
{
    "airspy": {
        "sample_rate": "3000K",
        "linearity": 17,
        "biastee": false
    }
}
```
</details>
[Full Airspy Documentation](../configuration/input/airspy.md)

### HydraSDR (`hydrasdr`)
<details>
<summary>Example</summary>
```json
{
    "hydrasdr": {
        "sample_rate": "3000K",
        "linearity": 17,
        "biastee": false
    }
}
```
</details>
[Full HydraSDR Documentation](../configuration/input/hydrasdr.md)

### Airspy HF+ (`airspyhf`)
<details>
<summary>Example</summary>
```json
{
    "airspyhf": {
        "sample_rate": "192k",
        "threshold": "low",
        "preamp": false
    }
}
```
[Full Airspy HF+ Documentation](../configuration/input/airspyhf.md)
</details>

### HackRF (`hackrf`)
<details>
<summary>Example</summary>
```json
{
    "hackrf": {
        "sample_rate": "6144k",
        "lna": 8,
        "vga": 20,
        "preamp": false
    }
}
```
</details>
[Full HackRF Documentation](../configuration/input/hackrf.md)

### SDRPlay (`sdrplay`)
<details>
<summary>Example</summary>
```json
{
    "sdrplay": {
        "sample_rate": "2304K",
        "agc": true,
        "lnastate": 5,
        "grdb": 40
    }
}
```
</details>
[Full SDRPlay Documentation](../configuration/input/sdrplay.md)

### SoapySDR (`soapysdr`)
<details>
<summary>Example</summary>
```json
{
    "soapysdr": {
        "active": true,
        "device": "driver=rtlsdr",
        "sample_rate": "1536K"
    }
}
```
</details>
[Full SoapySDR Documentation](../configuration/input/soapysdr.md)

### Serial Port Input (`serialport`)
<details>
<summary>Example</summary>
```json
{
    "serialport": {
        "baudrate": 38400,
        "port": "/dev/tty0"
    }
}
```
</details>
[Full Serial Port Documentation](../configuration/input/serial.md)

### NMEA2000 (`nmea2000`)
<details>
<summary>Example</summary>
```json
{
    "nmea2000": {
        "active": true,
        "port": "can0"
    }
}
```
</details>
[Full NMEA2000 Documentation](../configuration/input/NMEA2000.md)

## File Input Settings

### WAV File (`wavfile`)
<details>
<summary>Example</summary>
```json
{
    "wavfile": {
        "active": true,
        "filename": "recording.wav"
    }
}
```
</details>
[Full WAV File Documentation](../configuration/input/wav.md)

### Raw File (`file`)
<details>
<summary>Example</summary>
```json
{
    "file": {
        "active": true,
        "filename": "data.raw"
    }
}
```
</details>
[Full File Documentation](../configuration/input/file.md)

## Network Input Settings

### TCP Client (`rtltcp`)
<details>
<summary>Example</summary>
```json
{
    "rtltcp": {
        "host": "192.168.1.100",
        "port": 12345
    }
}
```
</details>
[Full TCP Documentation](../configuration/input/tcp.md)

### SpyServer (`spyserver`)
<details>
<summary>Example</summary>
```json
{
    "spyserver": {
        "host": "server.example.com",
        "port": 5555
    }
}
```
</details>
[Full SpyServer Documentation](../configuration/input/spyserver.md)

### UDP Server (`udpserver`)
<details>
<summary>Example</summary>
```json
{
    "udpserver": {
        "active": true,
        "port": 10110
    }
}
```
</details>
[Full UDP Documentation](../configuration/input/udp.md)

### ZMQ (`zmq`)
<details>
<summary>Example</summary>
```json
{
    "zmq": {
        "active": true,
        "endpoint": "tcp://localhost:5555"
    }
}
```
</details>
[Full ZMQ Documentation](../configuration/input/tcp.md)

## Output Settings

AIS-catcher supports various output channels. Each output channel has specific configuration options.  The documentation of the relevant keys can be found in the [Configuration](../configuration/output/overview.md) sections with some JSON examples below.

### Web Viewer (`server`)
An entry of `server` is a server of [`services`](#tracking-and-services-tracking-services), written the way the viewer always was.
<details>
<summary>Example</summary>
```json
{
    "server": [
        {
            "active": true,
            "port": 8100,
            "station": "My Station",
            "share_loc": true,
            "lat": 52,
            "lon": 4.3
        }
    ]
}
```
</details>
[Full Web Server Documentation](../configuration/output/web-viewer.md)

### Database Output (`db`)
<details>
<summary>Example</summary>
```json
{
    "db": [
        {
            "active": true,
            "type": "postgres",
            "conn_str": "dbname=ais",
            "station_id": 17,
            "position": true,
            "static": true
        },
        {
            "active": true,
            "type": "csv",
            "conn_str": "/var/log/ais"
        }
    ]
}
```
</details>

[Full Database Documentation](../configuration/output/PSQL.md)

### UDP Output (`udp`)
<details>
<summary>Example</summary>
```json
{
    "udp": [
        {
            "active": true,
            "host": "192.168.1.235",
            "port": 4002,
            "filter": false,
            "allow_type": "1,2,3,5,18,19,24"
        }
    ]
}
```
</details>
[Full UDP Documentation](../configuration/output/UDP.md)

### TCP  Output (Client) (`tcp`)
<details>
<summary>Example</summary>
```json
{
    "tcp": [
        {
            "active": true,
            "host": "5.9.207.224",
            "port": 12,
            "keep_alive": false
        }
    ]
}
```
</details>
[Full TCP Documentation](../configuration/output/TCP-client.md)

### TCP  Output (Server) (`tcp_listener`)
<details>
<summary>Example</summary>
```json
{
    "tcp_listener": [
        {
            "active": true,
            "port": 5012
        }
    ]
}
```
</details>
[Full TCP Documentation](../configuration/output/TCP-server.md)

### HTTP Output (`http`)
<details>
<summary>Example</summary>
```json
{
    "http": [
        {
            "active": true,
            "url": "http://example.com/ais",
            "interval": 10,
            "response": "json"
        }
    ]
}
```
</details>
[Full HTTP Documentation](../configuration/output/HTTP.md)

### MQTT Output (`mqtt`)
<details>
<summary>Example</summary>
```json
{
    "mqtt": [
        {
            "active": true,
            "host": "mqtt.example.com",
            "port": 1883,
            "topic": "ais/messages",
            "username": "user",
            "password": "pass"
        }
    ]
}
```
</details>
[Full MQTT Documentation](../configuration/output/MQTT.md)


