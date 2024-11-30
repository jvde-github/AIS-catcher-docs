##### Serial Port
<div class="command-container">
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-e</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-ge</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-e</span>
        <span class="cmd-value">baudrate</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-ge</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
</div>
Settings specific for reading NMEA lines from a serial port can all be set with the `e` switch fow now, e.g. on Linux:
```bash
AIS-catcher -e 368400 /dev/serial1

```

To dump the raw input from the serial device on-screen use `-`ge print on`.

## Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| BAUDRATE | integer | 38400 | Serial port speed |
| PORT | string | "" | Serial port device path/name |
| PRINT | boolean | false | Enable debug printing of received data |