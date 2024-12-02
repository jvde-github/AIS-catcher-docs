# SDRPlay RSP1/RSP1A/RSPDX (API 3.x)
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        [<span class="cmd-flag">-d</span> <span class="cmd-value">serial number</span>]
        <span class="cmd-flag">-gs</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

Settings specific for the SDRPlay  can be set on the command line with the ```-gs``` switch, e.g.:
```bash
AIS-catcher -gs lnastate 5
```


## Summary Settings


| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">Device-specific</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">auto</span> | Data type for input source |
| <span class="cmd-setting">AGC</span> | boolean | <span class="cmd-value">false</span> | Enable/disable Automatic Gain Control |
| <span class="cmd-setting">LNASTATE</span> | integer | <span class="cmd-value">0</span> | LNA state/gain (0-9) |
| <span class="cmd-setting">GRDB</span> | integer | <span class="cmd-value">32</span> | RF gain reduction in dB (0-59) |
| <span class="cmd-setting">ANTENNA</span> | char | <span class="cmd-value">'A'</span> | Antenna selection (A/B/C) for RSPdx models |