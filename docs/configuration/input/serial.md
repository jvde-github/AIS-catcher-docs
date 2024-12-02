##### Serial Port
<div class="command-container">
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-e</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-ge</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-e</span>
        <span class="cmd-value">baudrate</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-ge</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
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
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">device-specific</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000, 0=auto) |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">auto</span> | Data type for input source |
| <span class="cmd-setting">BAUDRATE</span> | integer | <span class="cmd-value">38400</span> | Serial port speed |
| <span class="cmd-setting">PORT</span> | string | <span class="cmd-value">""</span> | Serial port device path/name |
| <span class="cmd-setting">PRINT</span> | boolean | <span class="cmd-value">false</span> | Enable debug printing of received data |