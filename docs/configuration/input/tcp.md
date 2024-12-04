# Input over TCP
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">url</span>
        <span class="cmd-flag">-gt</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>

    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gt</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">protocol</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gt</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

Input over TCP with various protocols can be done with `-t` followed by the URL of the server. As an example, to read raw NMEA from a TCP server we can use:
```bash
AIS-catcher -t txt://192.168.1.120:5011
```

Various protocols are supported as input. The table below lists the available protocols and their descriptions:

| Protocol | Description                                  | Protocol | Description                                   |
| :------- | :------------------------------------------- |------- | :------------------------------------------- |
| `txt`    |  NMEA0183                               |`mqtt`   | MQTT                       |
| `gpsd`   | GPSD server                            | `wsmqtt` | MQTT over WS                       |
| `rtltcp` | Connecting to an RTL-TCP server           |

Use the appropriate protocol based on your server's configuration and data format. 

### Summary Settings

<div class="input-table" markdown>
| Key | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">288K</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">CU8</span> | Data type for input source |
| Specific Options | | | |
| <span class="cmd-setting">HOST</span> | string | <span class="cmd-value">-</span> | Remote host address |
| <span class="cmd-setting">PORT</span> | string | <span class="cmd-value">-</span> | Remote port number |
| <span class="cmd-setting">PROTOCOL</span> | string | <span class="cmd-value">rtltcp</span> | Protocol (RTLTCP/MQTT/GPSD/WS/WSMQTT) |
| <span class="cmd-setting">URL</span> | string | <span class="cmd-value">-</span> | Complete URL including protocol and credentials |
| | | | |
| TCP Options | | | |
| <span class="cmd-setting">PERSISTENT</span> | boolean | <span class="cmd-value">true</span> | Keep connection alive after errors |
| <span class="cmd-setting">KEEP_ALIVE</span> | boolean | <span class="cmd-value">false</span> | Enable TCP keepalive |
| <span class="cmd-setting">RESET</span> | integer | <span class="cmd-value">-1</span> | Reset connection after N minutes (-1=never) |
| <span class="cmd-setting">TIMEOUT</span> | integer | <span class="cmd-value">0</span> | Connection timeout in seconds |
| | | | |
| WebSocket Options | | | |
| <span class="cmd-setting">PROTOCOLS</span> | string | <span class="cmd-value">mqtt</span> | WebSocket sub-protocols |
| <span class="cmd-setting">BINARY</span> | boolean | <span class="cmd-value">on</span> | Enable binary WebSocket mode |
| <span class="cmd-setting">ORIGIN</span> | string | <span class="cmd-value">-</span> | Origin header for WebSocket |
| | | | |
| MQTT Options | | | |
| <span class="cmd-setting">TOPIC</span> | string | <span class="cmd-value">ais/data</span> | MQTT topic |
| <span class="cmd-setting">CLIENT_ID</span> | string | <span class="cmd-value">-</span> | MQTT client identifier |
| <span class="cmd-setting">USERNAME</span> | string | <span class="cmd-value">-</span> | MQTT username |
| <span class="cmd-setting">PASSWORD</span> | string | <span class="cmd-value">-</span> | MQTT password |
| <span class="cmd-setting">QOS</span> | integer | <span class="cmd-value">0</span> | MQTT QoS level (0-2) |
| | | | |
| RTLTCP Options | | | |
| <span class="cmd-setting">TUNER</span> | float | <span class="cmd-value">33.0</span> | Tuner gain (0-50, auto) |
| <span class="cmd-setting">RTLAGC</span> | boolean | <span class="cmd-value">false</span> | Enable RTL AGC |
| <span class="cmd-setting">FREQUENCY</span> | integer | <span class="cmd-value">0</span> | Frequency in Hz |
</div>