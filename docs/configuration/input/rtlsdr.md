# RTL SDR

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        [<span class="cmd-flag">-d</span> <span class="cmd-value">serial number</span>]
        <span class="cmd-flag">-gr</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

Gain and other settings specific to the RTL SDR can be set on the command line with the ```-gr``` switch. For example, the following command sets the tuner gain to +33.3 and switches the RTL AGC on:

```bash
AIS-catcher -gr tuner 33.3 rtlagc ON
```

On the command line, setting names and boolean values are not case-sensitive. In JSON configuration, keys are case-sensitive and must be lowercase.

## Specific Settings

<div class="input-table" markdown>

| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">1536K</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">off</span> | Tuner bandwidth in Hz (0-1,000,000, 0=auto) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| Specific Options | | | |
|  <span class="cmd-setting">tuner</span> | auto/float | <span class="cmd-value">auto</span> | Tuner gain/AGC (0-50 dB or AUTO) |
|  <span class="cmd-setting">rtlagc</span> | boolean | <span class="cmd-value">true</span>  | Enable/disable RTL2832U AGC |
|  <span class="cmd-setting">biastee</span> | boolean | <span class="cmd-value">false</span>  | Enable/disable bias tee power |
|  <span class="cmd-setting">buffer_count</span> | integer | <span class="cmd-value">24</span>  | Number of FIFO buffers (1-100) |

</div>