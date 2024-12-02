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

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| HOST | string | empty | Target UDP host address |
| PORT | string | empty | Target UDP port |
| JSON | boolean | false | Enable JSON output format |
| BROADCAST | boolean | false | Enable broadcast mode |
| RESET | integer | -1 | Socket reset interval in minutes (1-1440) |
| UUID | string | empty | Unique identifier (must be valid UUID) |
| GROUPS_IN | integer | - | Number of input groups |
