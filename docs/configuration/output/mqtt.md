# MQTT Integration

AIS-catcher can push AIS messages via the MQTT protocol (3.1.1) to a broker with the `-Q` switch. An example with all settings:
```bash
AIS-catcher -Q mqtt://username:password@127.0.0.1:1883 CLIENT_ID aiscatcher QOS 0 TOPIC data/ais MSGFORMAT JSON_NMEA
```
We can also read as input from a MQTT broker:
```bash
AIS-catcher -t mqtt://127.0.0.1:1883 -gt TOPIC data/ais USERNAME admin PASSWORD admin
```
