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
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">288K</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| Specific Options | | | |
| <span class="cmd-setting">host</span> | string | <span class="cmd-value">-</span> | Remote host address |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">-</span> | Remote port number |
| <span class="cmd-setting">protocol</span> | string | <span class="cmd-value">rtltcp</span> | Protocol (RTLTCP/MQTT/GPSD/WS/WSMQTT) |
| <span class="cmd-setting">url</span> | string | <span class="cmd-value">-</span> | Complete URL including protocol and credentials |
| | | | |
| TCP Options | | | |
| <span class="cmd-setting">persistent</span> | boolean | <span class="cmd-value">true</span> | Keep connection alive after errors |
| <span class="cmd-setting">keep_alive</span> | boolean | <span class="cmd-value">false</span> | Enable TCP keepalive |
| <span class="cmd-setting">reset</span> | integer | <span class="cmd-value">-1</span> | Reset connection after N minutes (-1=never) |
| <span class="cmd-setting">timeout</span> | integer | <span class="cmd-value">0</span> | Connection timeout in seconds |
| | | | |
| WebSocket Options | | | |
| <span class="cmd-setting">protocols</span> | string | <span class="cmd-value">mqtt</span> | WebSocket sub-protocols |
| <span class="cmd-setting">binary</span> | boolean | <span class="cmd-value">on</span> | Enable binary WebSocket mode |
| <span class="cmd-setting">origin</span> | string | <span class="cmd-value">-</span> | Origin header for WebSocket |
| | | | |
| MQTT Options | | | |
| <span class="cmd-setting">topic</span> | string | <span class="cmd-value">ais/data</span> | MQTT topic |
| <span class="cmd-setting">client_id</span> | string | <span class="cmd-value">-</span> | MQTT client identifier |
| <span class="cmd-setting">username</span> | string | <span class="cmd-value">-</span> | MQTT username |
| <span class="cmd-setting">password</span> | string | <span class="cmd-value">-</span> | MQTT password |
| <span class="cmd-setting">qos</span> | integer | <span class="cmd-value">0</span> | MQTT QoS level (0-2) |
| | | | |
| RTLTCP Options | | | |
| <span class="cmd-setting">tuner</span> | float | <span class="cmd-value">33.0</span> | Tuner gain (0-50, auto) |
| <span class="cmd-setting">rtlagc</span> | boolean | <span class="cmd-value">false</span> | Enable RTL AGC |
| <span class="cmd-setting">frequency</span> | integer | <span class="cmd-value">0</span> | Frequency in Hz |
</div>