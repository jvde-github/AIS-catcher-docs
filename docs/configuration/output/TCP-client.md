# TCP Client

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-P</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

To send raw NMEA as a TCP Client connecting to a listener:
```bash
AIS-catcher -P 192.168.1.235 4002
```
In this case, AIS-catcher acts as a TCP client and connects to the remote listener at 192.168.1.239 port 4002. 

## Summary Settings

<div class="input-table" markdown>
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">HOST</span> | string | <span class="cmd-value">-</span> | Target TCP server host |
| <span class="cmd-setting">PORT</span> | string | <span class="cmd-value">-</span> | Target TCP server port |
| <span class="cmd-setting">KEEP_ALIVE</span> | boolean | <span class="cmd-value">false</span> | Enable TCP keep-alive |
| <span class="cmd-setting">PERSIST</span> | boolean | <span class="cmd-value">true</span> | Keep trying to reconnect when connection fails |
| <span class="cmd-setting">JSON</span> | boolean | <span class="cmd-value">false</span> | Enable JSON output format |
| <span class="cmd-setting">UUID</span> | string | <span class="cmd-value">-</span> | Unique identifier (must be valid UUID) |
</div>