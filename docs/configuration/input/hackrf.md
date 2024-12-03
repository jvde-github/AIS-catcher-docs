# HackRF

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        [<span class="cmd-flag">-d</span> <span class="cmd-value">serial number</span>]
        <span class="cmd-flag">-gf</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

Settings specific for the HackRF can be set on the command line with the ```-gf``` switch, e.g.:

```bash
AIS-catcher -gf lna 16 vga 16 preamp OFF
```
## Summary Settings

<div class="input-table" markdown>

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">6144K</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000, 0=off) |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">CS8</span> | Data type for input source |
| Specific Options | | | |
| <span class="cmd-setting">LNA</span> | integer | <span class="cmd-value">8</span> | LNA (RF) gain in dB (0-40, rounded to multiples of 8) |
| <span class="cmd-setting">VGA</span> | integer | <span class="cmd-value">20</span> | VGA (IF) gain in dB (0-62, rounded to multiples of 2) |
| <span class="cmd-setting">PREAMP</span> | boolean | <span class="cmd-value">false</span> | Enable/disable preamplifier |


</div>