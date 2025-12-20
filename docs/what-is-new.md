# What's New?

## Edge version

new additions:

- allow multiple commands in init_seq for serial devices, separate via a comma. Fix issues for MacOS
- messages from serial devices supporting AIS-catcher format can pass on warning/info and error messages via the program
  
### Remove duplicates
When combining multiple input streams, overlapping reception can result in duplicate messages. To remove duplicates from output channels, use the experimental `unique` option. For example, the following removes duplicates from both console and a UDP stream:
```
AIS-catcher -o 1 unique on -u 127.0.0.1 5012 unique on
```

In JSON, set the `unique` key to `true` (remove duplicates) or `false` (default). Note that this could come at a performance cost that increases with the number of MMSIs so keep an eye on that.

### Downsampling Options

Two additional options, `position_interval` and `own_interval`, downsample position messages and VDO messages by limiting each MMSI to at most one update per specified interval (in seconds). Both default to `0` or, equivalent, `false`(disabled).

**Example:**
```
AIS-catcher -u 127.0.0.1 5012 position_interval 30
```

Alternatively, these options are available in the Web GUI:

<img width="909" height="513" alt="image" src="https://github.com/user-attachments/assets/728f4675-ff13-4337-b615-d1ac728e4866" />

Thanks to user Manny for suggesting these options.

> **Note:** These options are intended for users aggregating across multiple receivers to reduce bandwidth, and have not been optimized for large vessel counts.


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
