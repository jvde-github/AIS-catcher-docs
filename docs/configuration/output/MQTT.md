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

More examples:

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

## Topic Templates

AIS-catcher supports template strings for MQTT topics, allowing dynamic topic construction based on AIS message content. This enables more efficient message filtering and targeted subscriptions.

### Template Syntax

Use placeholders in the format `%key%` within your topic string. Available placeholders:

| Placeholder | Description | Example Value |
|-------------|-------------|---------------|
| `%mmsi%` | Vessel MMSI number | `367191000` |
| `%type%` | AIS message type | `1` |
| `%repeat%` | Repeat indicator | `0` |
| `%channel%` | Radio channel (A/B) | `A` |
| `%station%` | Station ID | `0` |
| `%ppm%` | Signal PPM | `-12.5` |
| `%rxtimeux%` | UNIX receive timestamp | `1750955733` |

### Template Examples

```bash
# Organize by vessel MMSI
AIS-catcher -Q mqtt://localhost:1883 TOPIC ais/%mmsi%/data

# Organize by message type and channel
AIS-catcher -Q mqtt://localhost:1883 TOPIC ais/%type%/%channel%/%mmsi%

# Include station and timing information
AIS-catcher -Q mqtt://localhost:1883 TOPIC ais/%station%/%type%/%channel%/%mmsi%

# Simple vessel-specific topics
AIS-catcher -Q mqtt://localhost:1883 TOPIC vessels/%mmsi%
```

### Resulting Topics

With the template `ais/%mmsi%/data`, messages would be published to topics like:
- `ais/367191000/data`
- `ais/210875000/data`  
- `ais/123456789/data`

This allows MQTT clients to subscribe to specific vessels:
```bash
# Subscribe to specific vessel
mosquitto_sub -h localhost -t "ais/367191000/data"

# Subscribe to all vessels using wildcards
mosquitto_sub -h localhost -t "ais/+/data"
```

### Benefits

- **Efficient filtering**: Clients can subscribe only to relevant vessels
- **Reduced bandwidth**: No need to receive and filter all messages
- **Better organization**: Logical topic hierarchy for different use cases
- **Integration friendly**: Works well with IoT and home automation systems


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
