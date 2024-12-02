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

| Protocol | Description                                   |
| :------- | :------------------------------------------- |
| `txt`    | Raw NMEA text.                               |
| `gpsd`   | GPSD server input.                           |
| `rtltcp` | Connecting to an RTL-TCP server.             |
| `mqtt`   | MQTT with JSON payload.                      |
| `wsmqtt` | MQTT with JSOP payload over WebSockets.                        |

Use the appropriate protocol based on your server's configuration and data format. 

### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">TUNER</span> | auto/float | <span class="cmd-value">auto</span> | Tuner gain/AGC (0-50 dB or AUTO) |
| <span class="cmd-setting">RTLAGC</span> | boolean | <span class="cmd-value">true</span> | Enable/disable RTL2832U AGC |
| <span class="cmd-setting">BIASTEE</span> | boolean | <span class="cmd-value">false</span> | Enable/disable bias tee power |
| <span class="cmd-setting">BUFFER_COUNT</span> | integer | <span class="cmd-value">24</span> | Number of FIFO buffers (1-100) |
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">device-specific</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">-</span> | Data type for input source |
| <span class="cmd-setting">URL</span> | string | <span class="cmd-value">-</span> | Full connection URL including protocol, host, port, etc |
| <span class="cmd-setting">PROTOCOL</span> | enum | <span class="cmd-value">RTLTCP</span> | Connection protocol (RTLTCP, MQTT, GPSD, WS, WSMQTT, TXT, NONE) |
| <span class="cmd-setting">HOST</span> | string | <span class="cmd-value">-</span> | Remote host address |
| <span class="cmd-setting">PORT</span> | string | <span class="cmd-value">-</span> | Remote port number |