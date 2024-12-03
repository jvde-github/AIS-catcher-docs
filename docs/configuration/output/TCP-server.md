

# TCP Server

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-S</span>
        <span class="cmd-value">port</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]

        ...
    </div>
</div>

You can also set up AIS-catcher as a TCP listener itself for sending NMEA messages, i.e. the program acts as a TCP server where at most 64 clients can connect to and read NMEA lines:
```bash
AIS-catcher -S 5011
```

## Summary Settings

<div class="input-table" markdown>
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">PORT</span> | integer | <span class="cmd-value">5010</span> | Listen port (0-65535) |
| <span class="cmd-setting">TIMEOUT</span> | integer | <span class="cmd-value">-</span> | Connection timeout |
| <span class="cmd-setting">JSON</span> | boolean | <span class="cmd-value">false</span> | Enable JSON output format |
</div>