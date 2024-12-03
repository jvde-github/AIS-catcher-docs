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
Most external programs will not be able to accept these JSON-packaged NMEA strings. It is a way to transfer received messages between AIS-catcher instances without losing metadata like the timestamp, ppm correction and signal level. These are not captured in the standard NMEA strings. 
Another option for UDP sending via `-u` is `BROADCAST on/off` to enable sending to broadcast addresses.


## Summary Settimgs

<div class="input-table" markdown>
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">HOST</span> | string | <span class="cmd-value">-</span> | Target UDP host address |
| <span class="cmd-setting">PORT</span> | string | <span class="cmd-value">-</span> | Target UDP port |
| <span class="cmd-setting">JSON</span> | boolean | <span class="cmd-value">false</span> | Enable JSON output format |
| <span class="cmd-setting">BROADCAST</span> | boolean | <span class="cmd-value">false</span> | Enable broadcast mode |
| <span class="cmd-setting">RESET</span> | integer | <span class="cmd-value">-1</span> | Socket reset interval in minutes (1-1440) |
| <span class="cmd-setting">UUID</span> | string | <span class="cmd-value">-</span> | Unique identifier (must be valid UUID) |
</div>
