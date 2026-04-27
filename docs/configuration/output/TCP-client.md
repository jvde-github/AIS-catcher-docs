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
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">host</span> | string | <span class="cmd-value">-</span> | Target TCP server host |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">-</span> | Target TCP server port |
| <span class="cmd-setting">msgformat</span> | string | <span class="cmd-value">NMEA</span> | Output format (`NMEA`, `JSON_NMEA`, `JSON_FULL`, etc.) |
| <span class="cmd-setting">keep_alive</span> | boolean | <span class="cmd-value">false</span> | Enable TCP keep-alive |
| <span class="cmd-setting">persist</span> | boolean | <span class="cmd-value">true</span> | Keep reconnecting when connection fails |
| <span class="cmd-setting">uuid</span> | string | <span class="cmd-value">-</span> | Unique identifier (must be a valid UUID) |
| <span class="cmd-setting">include_sample_start</span> | boolean | <span class="cmd-value">false</span> | Append sample-start counter to each NMEA line |
| <span class="cmd-setting">json</span> | boolean | <span class="cmd-value">false</span> | **Deprecated** — sets `msgformat` to `JSON_NMEA` |
| <span class="cmd-setting">json_full</span> | boolean | <span class="cmd-value">false</span> | **Deprecated** — sets `msgformat` to `FULL` |
</div>

Filter and routing settings (see [Message Filtering](message-filtering.md)) also apply.