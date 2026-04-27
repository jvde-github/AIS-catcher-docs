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
Settings specific for reading NMEA lines from a serial port can all be set with the `-ge` switch, e.g. on Linux:
```bash
AIS-catcher -e 38400 /dev/serial1
```

To dump the raw input from the serial device on-screen use `-ge dump on`.

## Summary Settings

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">N/A</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000, 0=off) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| Specific Options | | | |
| <span class="cmd-setting">baudrate</span> | integer | <span class="cmd-value">38400</span> | Serial port speed |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">-</span> | Serial port device path/name (Windows `COMx` is auto-prefixed) |
| <span class="cmd-setting">dump</span> | boolean | <span class="cmd-value">false</span> | Print raw bytes received from the serial device |
| <span class="cmd-setting">dump_file</span> | string | <span class="cmd-value">-</span> | Write raw bytes to file (also enables `dump`) |
| <span class="cmd-setting">init_seq</span> | string | <span class="cmd-value">-</span> | Initialization commands sent to the device on open |
| <span class="cmd-setting">flowcontrol</span> | enum | <span class="cmd-value">NONE</span> | Flow control (`NONE`, `HARDWARE`, or `SOFTWARE`) |
| <span class="cmd-setting">print</span> | boolean | <span class="cmd-value">false</span> | **Deprecated** alias for `dump` |
</div>