# What's New?

## Edge Version Features

### Offline Maps
- Support for offline maps in mbtiles format in the Web Viewer
  ```bash
   # include an offline map in mbtiles format
  AIS-catcher -N 8100 MBTILES map.mbtiles
  # or as overlay
  AIS-catcher -N 8100 MBOVERLAY map.mbtiles
  ```
- Debian packages now support RTL SDR V4 (the RTL-SDR library is build from source and statically linked into the executable)

## AIS-catcher for Android

- Option to auto start decoding when USB device is connected when starting the App
- Option to launch a webviewer available at a specified port

## Version 0.61

### MQTT Integration
- **Publishing Messages**
  ```bash
  # Basic MQTT connection
  AIS-catcher -Q mqtt://127.0.0.1:1883

  # WebSocket MQTT connection
  AIS-catcher -Q wsmqtt://127.0.0.1:1883

  # With message format and topic
  AIS-catcher -Q mqtt://127.0.0.1:1883 admin MSGFORMAT JSON_FULL TOPIC data/ais

  # With authentication and client ID
  AIS-catcher -Q mqtt://username:password@127.0.0.1:1883 admin CLIENT aiscatcher
  ```

- **Reading Messages**
  ```bash
  # Read from MQTT broker
  AIS-catcher -t mqtt://username:password@127.0.0.1:1883
  ```

### WebSocket Support
- Text data transmission via WebSockets using `ws://` protocol with `-t` and `-Q` options

### Web Viewer Enhancements
- Default map view on startup
- Optimized color scheme
- Draggable shipcard functionality
- Smart shipcard positioning near vessels
- Automatic vessel track display options: On hover and On selection

### Additional Updates
- Server protocol support:
  - SDR data: `sdr://127.0.0.1:5555`
  - Text over TCP: `txt://127.0.0.1:4001`
  - GPSD: `gpsd://127.0.0.1:4267`
  - RTL_TCP: `rtltcp://127.0.0.1:4099`
  - Raw IQ data: `tcp://127.0.0.1:1313`
- NMEA2000 configuration added to JSON settings
- System daemon restart interval set to 10s