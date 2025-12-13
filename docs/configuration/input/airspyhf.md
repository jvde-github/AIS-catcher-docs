# AirSpy HF+
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        [<span class="cmd-flag">-d</span> <span class="cmd-value">serial number</span>]
        <span class="cmd-flag">-gh</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>
Gain settings specific for the AirSpy HF+ can be set on the command line with the ```-gh``` switch. The following command switches off the preamp:

```bash
AIS-catcher -gh preamp OFF
```

Please note that only AGC mode is supported so there are limited options.

#### Summary Settings

| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">Device-specific</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">format</span> | enum | <span class="cmd-value">Device-specific</span> | Data type for input source |
| Specific Options | | | |
| <span class="cmd-setting">preamp</span> | boolean | <span class="cmd-value">false</span> | Enable/disable preamplifier |
| <span class="cmd-setting">threshold</span> | enum | <span class="cmd-value">LOW</span> | AGC threshold setting ("HIGH" or "LOW") |
