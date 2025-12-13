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


## Summary Settimgs

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">host</span> | string | <span class="cmd-value">-</span> | Target UDP host address |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">-</span> | Target UDP port |
| <span class="cmd-setting">json</span> | boolean | <span class="cmd-value">false</span> | Enable JSON output format |
| <span class="cmd-setting">json_full</span> | boolean | <span class="cmd-value">false</span> | Enable fully decoded JSON output |
| <span class="cmd-setting">broadcast</span> | boolean | <span class="cmd-value">false</span> | Enable broadcast mode |
| <span class="cmd-setting">reset</span> | integer | <span class="cmd-value">-1</span> | Socket reset interval in minutes (1-1440) |
| <span class="cmd-setting">uuid</span> | string | <span class="cmd-value">-</span> | Unique identifier (must be valid UUID) |
</div>
