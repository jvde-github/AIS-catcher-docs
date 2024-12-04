# What's new?
**Edge**:
- Support to publish AIS messages to MQTT broker.

Example:
```console
AIS-catcher -Q mqtt://127.0.0.1:1883 
```
or via WebSockets:
```console
AIS-catcher -Q wsmqtt://127.0.0.1:1883 
```
Add `MSGFORMAT` to specify the data send to the Broker (NMEA/JSON_NMEA/JSON_FULL) or provide a `TOPIC`, both are optional:
```console
AIS-catcher -Q mqtt://127.0.0.1:1883 admin MSGFORMAT JSON_FULL TOPIC data/ais
```
Authentication and client can also be easily set if needed:
```console
AIS-catcher -Q mqtt://username:password@127.0.0.1:1883  admin CLIENT aiscatcher
```

To read from a MQTT broker as input use `-t mqtt://` (or `wsmqtt://` for WebSocket communication with the broker):
```console
AIS-catcher -t mqtt://username:password@127.0.0.1:1883 
```

- smaller UI tidy up (e.g. opens default on map and adjusted colors)
- `-y`  now accepts the server location as `sdr://127.0.0.1:5555`
- `-t` now accepts the server location and protocol as `txt://127.0.0.1:4001` for text over TCP, `gpsd://127.0.0.1:4267` for a GPSD server and `rtltcp://127.0.0.1:4099` for a RTL_TCP server and `tcp://127.0.0.1:1313` for raw IQ data over tcp
- `-t` and `-Q` can send text data using WebSockets using `ws://`
- added NMEA2000 settings to the JSON configuration
- Options to automatically show the vessel track when hovering over and/or selecting a vessel
- Fix to system daemon file to restart process after 10s only
- Shipcard is placed near the vessel if the screen dimensions allow for it
- Shipcard is draggable
  
**v0.60** version:
- Option to send fully decoded AIS messages in JSON format via UDP and TCP (similar to screen output with `-o 5`). Add `JSON_FULL on` to `~P/S/u`.
- Bug fix for connecting serial devices in macOS
- Option to select columns in the table (and many more options added):
  
  ![image](https://github.com/user-attachments/assets/a89120dc-9a2b-485c-b6ff-5516385ad8ae)

- Option to use text description in tables for ship type
- Overlay in AIS-catcher webviewer that shows possibility of atmospheric ducting conditions enable long range AIS reception
  
  ![image](https://github.com/jvde-github/AIS-catcher/assets/52420030/d15920f1-d827-42da-9f05-3587fe553feb)

- Added debian packages and installation script


Earlier versions:

- Added a measure tool to measure distance and bearing between two points and/or ships. Start with CTRL-Click or activate the measure tool and press +
- Additional option  for `-f`-switch to either append NMEA lines to file (`-f filename MODE APP` for appending - default) or starting fresh with `-f filename MODE OUT`
- Community feed by running with -X. This will feed the aiscatcher.org server and return data as an extra map layer option in your webviewer.
- Performance improvements when drawing a large number of vessels by switching from Leaflet to Openlayers (notice this might require re-working some plugins). in openlayers it is more straightforward to plot ship icons on the canvas.
- Option to auto terminate the program if no messages received for a while, e.g. after 10 minutes `-T 600 nomsg_ony`. This will help cure network connections for input or devices going stale without an error 
- You can access  geoJSON output of the current ship positions by visiting the web viewer at `/geojson` and for KML output, please navigate to `/kml` (enable with the
switches `-N geojson on` and `-N kml on`). The KML feature facilitates the visualization of ship positions in Google Earth Pro. Be sure to add a network link and configure the auto-refresh rate in GE. A demonstration of the use of GeoJSON is [plotting the vessels on the tar1090 map.](https://github.com/jvde-github/AIS-in-TAR1090)
- Experimenter Mode for NMEA2000 via socketCAN on Linux. [See documentation below](https://github.com/jvde-github/AIS-catcher/blob/main/README.md#nmea2000-input-and-output-via-socketcan).
- Pyssel blog post describes procedure to show offline mbtiles maps [here](https://pysselilivet.blogspot.com/2023/12/ais-receiver-and-dispatcher-best.html)
