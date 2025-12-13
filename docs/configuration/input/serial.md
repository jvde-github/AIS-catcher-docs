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

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">N/A</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000, 0=off) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">format</span> | string | <span class="cmd-value">TXT</span> | Data type for input source |
| Specific Options | | | |
| <span class="cmd-setting">baudrate</span> | integer | <span class="cmd-value">38400</span> | Serial port speed |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">0</span> | Serial port device path/name |
| <span class="cmd-setting">print</span> | boolean | <span class="cmd-value">false</span> | Enable debug printing of received data |
</div>