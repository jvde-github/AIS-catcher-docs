# Input as UDP server
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-x</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>
You can receive NMEA input via a built-in UDP server:
```bash
AIS-catcher -x 192.168.1.235 4002
```

## Summary Settings


| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">Device-specific</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">-</span> | Data type for input source |
| Specific Options | | | |
| <span class="cmd-setting">PORT</span> | string | <span class="cmd-value">-</span> | UDP server port to listen on |
| <span class="cmd-setting">SERVER</span> | string | <span class="cmd-value">-</span> | UDP server address to bind to |