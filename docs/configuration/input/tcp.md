# Input over TCP
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">url</span>
        <span class="cmd-flag">-gt</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>

    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gt</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">protocol</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gt</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
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
| URL | string | - | Full connection URL including protocol, host, port, etc |
| PROTOCOL | enum | "RTLTCP" | Connection protocol (RTLTCP, MQTT, GPSD, WS, WSMQTT, TXT, NONE) |
| HOST | string | - | Remote host address |
| PORT | string | - | Remote port number |
