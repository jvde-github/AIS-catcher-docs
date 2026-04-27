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
AIS-catcher -Q mqtt://username:password@127.0.0.1:1883 client_id aiscatcher qos 0 topic data/ais msgformat JSON_NMEA
```

More examples:

```bash
# Basic MQTT connection
AIS-catcher -Q mqtt://127.0.0.1:1883

# WebSocket MQTT connection
AIS-catcher -Q wsmqtt://127.0.0.1:1883

# With message format and topic
AIS-catcher -Q mqtt://127.0.0.1:1883 admin msgformat JSON_FULL topic data/ais

# With authentication and client ID
AIS-catcher -Q mqtt://username:password@127.0.0.1:1883 admin client aiscatcher
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

| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">url</span> | string | <span class="cmd-value">-</span> | Broker URL (`mqtt[s]://[user:pass@]host[:port]` or `ws[s]mqtt://...`) |
| <span class="cmd-setting">host</span> | string | <span class="cmd-value">-</span> | Broker hostname |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">-</span> | Broker port |
| <span class="cmd-setting">username</span> | string | <span class="cmd-value">-</span> | MQTT username |
| <span class="cmd-setting">password</span> | string | <span class="cmd-value">-</span> | MQTT password |
| <span class="cmd-setting">topic</span> | string | <span class="cmd-value">ais/data</span> | MQTT topic (supports `%mmsi%`, `%type%`, etc. — see above) |
| <span class="cmd-setting">client_id</span> | string | <span class="cmd-value">-</span> | MQTT client identifier |
| <span class="cmd-setting">qos</span> | integer | <span class="cmd-value">0</span> | MQTT QoS level (0-2) |
| <span class="cmd-setting">msgformat</span> | string | <span class="cmd-value">NMEA</span> | Output format (`NMEA`, `JSON_NMEA`, `JSON_FULL`, etc.) |
| <span class="cmd-setting">protocol</span> | string | <span class="cmd-value">MQTT</span> | Transport (`MQTT`, `MQTTS`, `WSMQTT`, `WSSMQTT`, `WS`, `TCP`, `TLS`, `TXT`) |
| | | | |
| TCP options (forwarded to underlying transport) | | | |
| <span class="cmd-setting">persist</span> | boolean | <span class="cmd-value">true</span> | Keep reconnecting after errors |
| <span class="cmd-setting">keep_alive</span> | boolean | <span class="cmd-value">false</span> | Enable TCP keepalive |
| <span class="cmd-setting">timeout</span> | integer | <span class="cmd-value">0</span> | TCP timeout in seconds (0-3600) |
| <span class="cmd-setting">reset</span> | integer | <span class="cmd-value">0</span> | Reset connection after N minutes (0-3600; 0 = never) |
| | | | |
| WebSocket Options | | | |
| <span class="cmd-setting">protocols</span> | string | <span class="cmd-value">mqtt</span> | WebSocket sub-protocol header |
| <span class="cmd-setting">binary</span> | boolean | <span class="cmd-value">on</span> | Enable binary WebSocket frames |
| <span class="cmd-setting">origin</span> | string | <span class="cmd-value">-</span> | `Origin` header for WebSocket handshake |

</div>
