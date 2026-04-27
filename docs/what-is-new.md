# What's New?

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

- **NMEA 4.0 Tag Blocks**: support for NMEA tag blocks (`msgformat nmea_tag` for networking or `-o 7` for screen). Note that when reading the timestamps are overwritten by default which can be switched off with `-go stamp off`

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
