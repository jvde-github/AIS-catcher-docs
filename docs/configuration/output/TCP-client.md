# TCP Client

To send raw NMEA as a TCP Client connecting to a listener:
```bash
AIS-catcher -P 192.168.1.235 4002
```
In this case, AIS-catcher acts as a TCP client and connects to the remote listener at 192.168.1.239 port 4002. 

## Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| HOST | string | empty | Target TCP server host |
| PORT | string | empty | Target TCP server port |
| KEEP_ALIVE | boolean | false | Enable TCP keep-alive |
| JSON | boolean | false | Enable JSON output format |
| PERSIST | boolean | true | Enable persistent connection |
| UUID | string | empty | Unique identifier (must be valid UUID) |
| GROUPS_IN | integer | - | Number of input groups |