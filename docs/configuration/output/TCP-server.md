

# TCP Server


You can also set up AIS-catcher as a TCP listener itself for sending NMEA messages, i.e. the program acts as a TCP server where at most 64 clients can connect to and read NMEA lines:
```bash
AIS-catcher -S 5011
```

## Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| PORT | integer | 5010 | Listen port (0-65535) |
| TIMEOUT | integer | - | Connection timeout |
| JSON | boolean | false | Enable JSON output format |
| GROUPS_IN | integer | - | Number of input groups |
