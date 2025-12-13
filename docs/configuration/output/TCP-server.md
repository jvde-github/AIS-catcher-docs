

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
Use the `JSON` option or `JSON_FULL` option to send data packaged in a JSON object for ease of downstream processing.

## Summary Settings

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">port</span> | integer | <span class="cmd-value">5010</span> | Listen port (0-65535) |
| <span class="cmd-setting">timeout</span> | integer | <span class="cmd-value">-</span> | Connection timeout |
| <span class="cmd-setting">json</span> | boolean | <span class="cmd-value">false</span> | Enable JSON output format |
| <span class="cmd-setting">json_full</span> | boolean | <span class="cmd-value">false</span> | Enable fully decoded JSON output |
</div>