# Input as UDP server
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-x</span>
        <span class="cmd-value">server</span>
        <span class="cmd-value">port</span>
    </div>
</div>
You can receive NMEA input via a built-in UDP server:
```bash
AIS-catcher -x 192.168.1.235 4002
```

## Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| PORT | string | - | UDP server port to listen on |
| SERVER | string | - | UDP server address to bind to |