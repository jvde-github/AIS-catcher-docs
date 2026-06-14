# What's New?

## Edge

### ITU-R M.1371-6 alignment

The JSON output has been aligned with the 2026 ITU-R M.1371-6 spec.

- **Message type 28** (single-slot AtoN report, M.1371-6 §A7-3.26) is now expanded into structured JSON fields. See the [type 28 reference](references/JSON-decoding.md#type-28).
- **Messages 25 and 26**: the addressed/broadcast envelope is now exposed in JSON; when the payload carries a recognised `(dac, fid)` pair the same ASM fields are emitted as for messages 6 and 8.
- **Spec field renames** in messages 1/2/3, 4/11, 9, 18, 19, 21: bits previously labelled `regional`/`reserved` are now exposed under their M.1371-6 names (`power`, `transmission_control`, `alt_sensor`, `aton_status`, …). See the [JSON reference](references/JSON-decoding.md) for the per-message field list.
- **Type 23**: `ship_type` is renamed to `shiptype` and now includes a `shiptype_text` description, matching the convention used elsewhere.
- New ASM decoder for **DAC 366, FID 10** (IALA AtoN monitor; messages 6/8/26).

### New ASM decoders

A range of widely deployed Application-Specific Messages is now expanded into structured JSON fields:

- **IMO Circ.289 (DAC 1)** — FID 17 (VTS-generated targets), FID 19 (marine traffic signal), FID 20 (berthing data / port operations), FID 22 (area notice, broadcast), FID 23 (area notice, addressed), FID 24 (extended ship static), FID 25 (dangerous cargo / IMDG), FID 28 (route addressed), FID 32 (tidal window).
- **Inland AIS — CCNR VTT 1.2 (DAC 200)** — FID 21 (ETA at lock/bridge/terminal), FID 22 (RTA at lock/bridge/terminal), FID 23 (EMMA safety warning), FID 24 (water level gauges, up to four stations), FID 40 (signal station status).
- **Sweden STM (DAC 265, FID 1)** — Sea Traffic Management route messages, with full waypoint reconstruction from the delta-encoded leg chain.
- **Flag-state text telegrams** — DAC 210 (Cyprus), 248 (Malta), 353 (Liberia) FID 0 now decode as text.

### Inland AIS in the web viewer

- **Inland ENI** (European vessel ID number) is now part of ship static data, shown in the ship card and available as an optional sortable column in the ship table.
- Inland-specific FIDs (10/55) and the **blue sign** indicator are surfaced on the map and ship card.
- **Ship-type details** are now reachable from a click popover with the full ITU description, and ERI / inland ship-type tables are complete and labelled correctly.

### Web viewer

- **Box select on the map** — drag a rectangle to show tracks for every vessel inside the area at once.
- **Reset tracks from now** map action — clear historical track points and start fresh from the current time without dropping the vessels themselves.
- **GPS-derived station position** is marked with a blue border and a tooltip so it is visually distinguishable from configured fixed positions.
- **Type 24B transponder details** (vendor, model, serial) are now surfaced in the ship card's tech details.
- **Text telegrams** (safety / broadcast text messages) are now displayed in the web viewer.

### Community feed

- The community ship overlay has been replaced by a **popup pane connected to [aiscatcher.org/livemap](https://aiscatcher.org/livemap)** with two-way view synchronisation (map pan/zoom is shared) and local-vessel push.
- The community-feed icon now indicates **sharing state at a glance**: red = off, orange = anonymous, green = sharing with UUID.

### HTTP API

- **Per-route CORS allow-origin** flag, enabled by default on the `JSON`, `GeoJSON`, `KML`, and `metrics` endpoints so dashboards and external consumers can fetch directly from a browser. CSP also now allows `http`/`ws` schemes so LAN deployments work without a custom policy.

### Input

- **Lossless mode** for file and TCP inputs. `-ga LOSSLESS on/off` (FileRAW) and `-gt LOSSLESS on/off` (RTLTCP) control whether the input blocks or drops samples on overflow. Defaults preserve current behaviour: file replay is lossless (block), live TCP is lossy (drop). The current setting is shown in `-v` output.
- **Simpler inline settings** for input flags. `-t`, `-r`, `-x`, `-z`, `-i`, `-w`, and `-e` now accept trailing key/value pairs after their positional arguments, so you can write `-t HOST PORT lossless on` instead of having to repeat the device subletter via `-gt`.
- New **`sensitivity_high`** config option for SDR input selects the higher-sensitivity ("challenger") decoder model — useful when you want maximum decode rate and CPU headroom allows it.

### Build and packaging

- New CMake option `-DWEBVIEWER=OFF` produces a headless build without `WebDB`/`WebViewer`/`HTTPServer` (~1.5 MB smaller binary). The `-N` flag and the `server` config key are gated when the webviewer is disabled.
- **[`aiscat`](tools/python.md)** — Python bindings for the AIS-catcher NMEA decoder are now published on PyPI. The package exposes a `Decoder` with `decode()` / `from_file` / `from_stdin` / `from_tcp` / `from_udp` helpers, multiple output formats (`dictionary`, `annotated`, `json`, `json_nmea`, `nmea`, `nmea_tag`, `binary`), and ships pre-built wheels including armv7l and Windows ARM64. Free-threaded (3.13t / 3.14t) wheels are also published, plus an additional decoder speedup. See [Tools → Python](tools/python.md) for details.

## Version 0.68

### Web Viewer

- Fixed vessel track polylines drifting ahead of the ship marker due to an incremental merge bug
- Incremental plane updates now support `?since=` with timeout-based cleanup of stale aircraft
- RainViewer refresh interval increased from 2 minutes to 10 minutes
- RainViewer updates pause while the browser tab is hidden
- Removed the clouds overlay layer
- Fixed sticky hover suppression after map moves

### Data and API Fixes

- Fixed MMSI key corruption in path JSON
- Added support for `@filename` response files

### Service and Packaging

- systemd unit no longer uses a `bash -c` subshell

## Version 0.67

### New Features

#### HydraSDR Support

HydraSDR is now a supported input device. See the [HydraSDR input page](../configuration/input/hydrasdr.md) for details.

#### Duplicate Removal

When combining multiple input streams, overlapping reception can result in duplicate messages. To remove duplicates from output channels, use the `unique` option. For example, the following removes duplicates from both console and a UDP stream:

```
AIS-catcher -o 1 unique on -u 127.0.0.1 5012 unique on
```

In JSON, set the `unique` key to `true` (remove duplicates) or `false` (default). Note that this could come at a performance cost that increases with the number of MMSIs so keep an eye on that.

#### Downsampling Options

Two additional options, `position_interval` and `own_interval`, downsample position messages and VDO messages by limiting each MMSI to at most one update per specified interval (in seconds). Both default to `0` or, equivalent, `false` (disabled).

**Example:**
```
AIS-catcher -u 127.0.0.1 5012 position_interval 30
```

Alternatively, these options are available in the Visual Web Control interface:

<img width="909" height="513" alt="image" src="https://github.com/user-attachments/assets/728f4675-ff13-4337-b615-d1ac728e4866" />

Thanks to user Manny for suggesting these options.

> **Note:** These options are intended for users aggregating across multiple receivers to reduce bandwidth, and have not been optimized for large vessel counts.

#### Serial Device Improvements

- `init_seq` now accepts multiple comma-separated commands
- Fixed `init_seq` issues on macOS (and Windows buffer flushing during init)
- Serial devices supporting AIS-catcher format can now relay warning, info, and error messages through the program
- New `flowcontrol` option (`hardware`/`software`/`none`) and `disable_xonoff` switch
- Serial port opened in non-blocking mode to avoid DTR hang on some adapters
- New `dump_file` option to save raw serial bytes for debugging
- DC16H frame format support

#### Zones

Support for tailoring routing of messages from receivers to output channels via zones in JSON configuration and Visual Web Control.

#### Channel Designation (AB/CD)

Channel designation is now configurable via JSON config and is shown in model startup output of the Visual Web Control.

#### Microsecond Timestamps

`rxuxtime` field added to `JSON_FULL` output, providing microsecond-resolution receive timestamps. NMEA 4.0 tag-block timestamps now use microseconds where available.

#### Reboot Watchdog

A systemd `OnFailure` watchdog can automatically reboot the host if AIS-catcher stops repeatedly. Configurable burst/interval parameters with a 5-minute grace period after toggling, controlled via the install script.

### Output and Configuration

- **Receiver index** is now included in output; `-v` applies to all receivers, `-v+` to the last one only
- **`webcontrol_http`** option for the webviewer
- **`ssl_verify`** setting on HTTP outputs to disable TLS certificate verification when needed
- **NMEA 4.0 tag blocks** now include the group ID only for multi-line sentences
- Default `repeat` for message type 27 is now 3
- Aliases: `rssi`/`fo` for `signalpower`/`ppm`; `DESC` for `description`
- Internal settings unified to a key-based API with structured error reporting (`SetKey`); legacy aliases kept for backward compatibility
- Community feed restricted to local SDR hardware only

### Web Viewer

#### Vessel Tracks — Major Overhaul

- **Incremental (delta) loading**: only new path points are fetched on each update
- Tracks capped at 250 points per vessel, consistent between "Show Track" and "Show All Tracks"

#### Multi-Receiver View

A new view in the webviewer lets users see and switch between multiple receivers from a single interface.

#### Realtime and UI Improvements

- Realtime NMEA tab now displays the shipname instead of just MMSI
- Station name passed via `plugins.js` for immediate tab title display
- Community feed gained a binary compact endpoint, sprite-sheet icons, and click-to-livemap
- Dark info panel, darker hover background, fixed truncated SVG flags
- Fixed RainViewer overlay (CORS and API path), MBTiles import, distance charts, "Show all tracks", strict-mode violations, missing planes sprite, ship-shape highlight stuck on hover
- Shrunk `favicon.ico` from 97 KB to 15 KB
- `marked` library now bundled (no CDN runtime dependency)

#### Bug Fixes

- **Signal level charts**: fixed extreme values for UDP/TCP sources
- Static data refreshed correctly when a ship comes back into scope
- HTTP stats fixed under TLS

### Performance

This release contains a substantial performance overhaul of the I/O hot path. Highlights:

- **NMEA parser**: zero-alloc split, SWAR scanning, bulk 6-bit decode, line-aware start detection — ~64% fewer instructions
- **JSON parser**: zero-copy tokenizer, hand-rolled number parsing, flat open-addressing hash table for key lookup, allocation-free steady-state parsing
- **JSON Writer**: replaces legacy `JSONBuilder` and ad-hoc serializers with a `std::string`-backed writer; ~5–10% faster on `-o 0/3/5/7`
- **AIS::Message**: SWAR `getText`/`getUint`, batched 6-bit payload decode (~7–10% faster on `-o 5` / `nmea_refresh`)
- **Lock-free output**: thread-local screen buffers, atomic `ByteCounter`, DB mutex released before downstream `Send` cascade (dual `-N` benchmark: 9.05s → 6.03s)
- POSIX `read()` for stdin, single newline flush per message (replacing per-message `fflush`)

### Stability and Networking

- TCP: try all `addrinfo` entries, connect timeout for blocking mode, guard repeated stop requests
- WebSocket/MQTT: handshake fixes, Windows socket check, max frame drop, `PUBREL` handling, buffer-growth fix
- Logger: fixed circular buffer and mutex issues
- GPS: fixed use-after-free and JSON memory issue, warn-once on bad data, scan limits
- Postgres/N2K: traffic monitoring extended, empty AIS messages handled, filter shadow fixed (settings now apply to the active filter)
- File input, hybrid config, NMEA RMC parsing, NMEA checksum in `-o 6`, timer handling for non-frontend models (NMEA, N2K, ADSB, Export)
- Backup writer wrapped in try/catch with additional diagnostics
- Compiler-warning cleanup across the tree; spellcheck CI added (`typos`)

### Packaging

- Debian packages now store HydraSDR and RTL-SDR libraries as DLLs in `/usr/lib/AIS-catcher` instead of statically linking
- Switched to debhelper — `dh_shlibdeps` auto-resolves correct dependencies per distro/arch
- Fixed several `.deb` packaging issues (`libssl3/t64`, `ETXTBSY`, empty `Depends` field)
- Added CI install test covering the full platform matrix
- New Ubuntu **ARM64** and **ARMhf** packages; **RPM** packages added; Fedora dropped
- Frontend libraries bundled via npm/Vite — no CDN dependencies at runtime. Webassets repo is archived
- Modular CMake dependency management — individual scripts per library
- Install script: parallelized builds, non-root install option, hardened reboot handling, removed Docker support for i386/armel
- Copyright extended to 2026

## Version 0.66

- Improve documentation for configuration via JSON
- Fix chart colors when running web viewer in iframe on Firefox
- Technical details of equipment added to shipcard (press information icon in sender field)
- CS unit for class B is displayed in shipcard of the web viewer if available
- Serial devices can be initialized with an init sequence
- Remodelling of realtime NMEA tab with options to filter on MMSI and share NMEA lines with decoder tab for message parsing
- Option to track NMEA in webviewer for a specific ship or station
- Shortcut to measure distance between two objects or points is now SHIFT-CLICK to select the first point. This should improve behaviour for devices that cannot distinguish between a left and right mouse click.
  
## Version 0.64 - 0.65

Various updates to improve stability, security and minor bug fixes.

## Version 0.63

### Enhanced Features

- **NMEA 4.0 Tag Blocks**: support for NMEA tag blocks (`msgformat nmea_tag` for networking or `-o 7` for screen).

## Version 0.63

### Enhanced Features
- **Data throughput**: significant reduction in data throughput to community hub
- **Online NMEA decoder**: Built-in NMEA decoder in the local webviewer
- **Kiosk Mode**: Full-screen display mode for dedicated monitoring setups
- **MSGFORMAT Configuration**: Flexible output format definitions for customized data presentation. Introduction of msgformat binary_nmea to save on bandwidth
- **Extended Binary Messages**: Additional binary message types now decoded and displayed
- **Verbose JSON Output** (`-o 6`): Enhanced JSON format with detailed field descriptions (WIP)
- **Debian Trixie Support**: Compatibility with Debian 13 (Trixie)
- **Filesystem-based Map Tiles**:
```bash
  # Serve map tiles from filesystem
  AIS-catcher -N 8100 FSTILES /path/to/tiles
  # Filesystem overlay maps
  AIS-catcher -N 8100 FSOVERLAY /path/to/overlay
```

For complete edge changes, see the [commit history](https://github.com/jvde-github/AIS-catcher/commits/main/).

## Version 0.62

### ADSB Integration
Connect to ADSB feeds to visualize aircraft alongside vessels:
```bash
# Beast format
AIS-catcher -t beast localhost 30003 -N 8100

# BaseStation format
AIS-catcher -t basestation localhost 30002 -N 8100
```

### Binary Message Decoding
The WebViewer now decodes and displays regional binary AIS messages (availability varies by location).

### Offline Mapping
```bash
# MBTiles format support
AIS-catcher -N 8100 MBTILES map.mbtiles
# Or as overlay
AIS-catcher -N 8100 MBOVERLAY map.mbtiles
```

### RTL-SDR V4 Support
Debian packages now include statically-linked RTL-SDR library with V4 dongle support.

## AIS-catcher for Android

- Auto-start decoding when USB device connects
- Built-in webviewer on configurable port

## Version 0.61

### MQTT Integration
```bash
# Publish messages
AIS-catcher -Q mqtt://127.0.0.1:1883
AIS-catcher -Q wsmqtt://127.0.0.1:1883
AIS-catcher -Q mqtt://127.0.0.1:1883 admin MSGFORMAT JSON_FULL TOPIC data/ais
AIS-catcher -Q mqtt://username:password@127.0.0.1:1883 admin CLIENT aiscatcher

# Subscribe to messages
AIS-catcher -t mqtt://username:password@127.0.0.1:1883
```

### Protocol Expansion
- WebSocket text transmission (`ws://`)
- SDR data streaming (`sdr://`)
- Text over TCP (`txt://`)
- GPSD integration (`gpsd://`)
- RTL_TCP support (`rtltcp://`)
- Raw IQ data (`tcp://`)

### Web Viewer Improvements
- Map-first default view
- Enhanced color palette
- Draggable ship information cards
- Context-aware card positioning
- Configurable vessel track display (on hover/selection)

### Configuration
- NMEA2000 settings in JSON configuration
- System daemon auto-restart (10s interval)
