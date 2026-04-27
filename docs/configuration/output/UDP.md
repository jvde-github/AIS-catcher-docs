# UDP 

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-u</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]

        ...
    </div>
</div>


AIS messages can be forwarded between applications over UDP via the `-u` switch and as a TCP Client using `-P`. To send data to a port at a specific server, we can use:
```bash
AIS-catcher -u 192.168.1.235 4002
```
The command accepts additonal parameters, e.g. to send NMEA messages packaged in a JSON object:
```bash
AIS-catcher -u 192.168.1.235 4002 JSON on
```
Most external programs will not be able to accept these JSON-packaged NMEA strings. It is a way to transfer received messages between AIS-catcher instances without losing metadata like the timestamp, ppm correction and signal level. These are not captured in the standard NMEA strings. The option `JSON_FULL` does a full decode of the AIS message.
Another option for UDP sending via `-u` is `BROADCAST on/off` to enable sending to broadcast addresses.


## Summary Settings

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">host</span> | string | <span class="cmd-value">-</span> | Target UDP host address |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">-</span> | Target UDP port |
| <span class="cmd-setting">msgformat</span> | string | <span class="cmd-value">NMEA</span> | Output format (`NMEA`, `JSON_NMEA`, `JSON_FULL`, etc.) |
| <span class="cmd-setting">broadcast</span> | boolean | <span class="cmd-value">false</span> | Enable broadcast mode |
| <span class="cmd-setting">reset</span> | integer | <span class="cmd-value">0</span> | Recreate socket after N minutes (1-1440; 0 = never) |
| <span class="cmd-setting">uuid</span> | string | <span class="cmd-value">-</span> | Unique identifier (must be a valid UUID) |
| <span class="cmd-setting">include_sample_start</span> | boolean | <span class="cmd-value">false</span> | Append sample-start counter to each NMEA line |
| <span class="cmd-setting">json</span> | boolean | <span class="cmd-value">false</span> | **Deprecated** — sets `msgformat` to `JSON_NMEA` |
| <span class="cmd-setting">json_full</span> | boolean | <span class="cmd-value">false</span> | **Deprecated** — sets `msgformat` to `FULL` |
</div>

Filter and routing settings (see [Message Filtering](message-filtering.md)) also apply.
