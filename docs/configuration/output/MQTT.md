# MQTT Integration

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-Q</span>
        <span class="cmd-value">url</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>


AIS-catcher can push AIS messages via the MQTT protocol (3.1.1) to a broker with the `-Q` switch. An example with all settings:
```bash
AIS-catcher -Q mqtt://username:password@127.0.0.1:1883 CLIENT_ID aiscatcher QOS 0 TOPIC data/ais MSGFORMAT JSON_NMEA
```

## Summary Settings

<div class="input-table" markdown>
| Key | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">URL</span> | string | <span class="cmd-value">-</span> | MQTT broker URL (mqtt[s]://[user:pass@]host[:port]) |
| <span class="cmd-setting">HOST</span> | string | <span class="cmd-value">-</span> | MQTT broker hostname |
| <span class="cmd-setting">PORT</span> | string | <span class="cmd-value">-</span> | MQTT broker port |
| <span class="cmd-setting">USERNAME</span> | string | <span class="cmd-value">-</span> | MQTT username |
| <span class="cmd-setting">PASSWORD</span> | string | <span class="cmd-value">-</span> | MQTT password |
| <span class="cmd-setting">TOPIC</span> | string | <span class="cmd-value">ais/data</span> | MQTT topic |
| <span class="cmd-setting">CLIENT_ID</span> | string | <span class="cmd-value">-</span> | MQTT client identifier |
| <span class="cmd-setting">QOS</span> | integer | <span class="cmd-value">0</span> | MQTT QoS level (0-2) |
| <span class="cmd-setting">MSGFORMAT</span> | string | <span class="cmd-value">NMEA</span> | Output format (NMEA/JSON_NMEA/JSON_FULL) |
| <span class="cmd-setting">PROTOCOL</span> | string | <span class="cmd-value">MQTT</span> | Protocol (MQTT/WS/WSMQTT) |
| | | | |
| WebSocket Options | | | |
| <span class="cmd-setting">PROTOCOLS</span> | string | <span class="cmd-value">mqtt</span> | WebSocket sub-protocols |  
| <span class="cmd-setting">BINARY</span> | boolean | <span class="cmd-value">on</span> | Enable binary WebSocket mode |
</div>
