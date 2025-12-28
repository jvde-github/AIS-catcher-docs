# HydraSDR

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        [<span class="cmd-flag">-d</span> <span class="cmd-value">serial number</span>]
        <span class="cmd-flag">-gm</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

The HydraSDR requires careful gain configuration similar to the AirSpy devices.  There are three different gain modes: linearity, sensitivity and so-called free. These can be set via the ```-gm``` switch when using the HydraSDR. 

We can activate 'linearity' mode with gain ```10``` using the following ```AIS-catcher``` command line:

```bash
AIS-catcher -gm linearity 10
```
Settings can also be provided per stage:
```bash
AIS-catcher -gm lna AUTO vga 12 mixer 12
```

On the command line, setting names and boolean-ish values are not case-sensitive (e.g. `LINEARITY 10` equals `linearity 10`). In JSON configuration, keys are case-sensitive and must be lowercase.

#### Summary Settings

<div class="input-table" markdown>

| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">192K</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000, 0=off) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| Specific Options | | | |
| <span class="cmd-setting">sensitivity</span> | integer | <span class="cmd-value">-</span> | Sensitivity gain mode (0-21) |
| <span class="cmd-setting">linearity</span> | integer | <span class="cmd-value">17</span> | Linearity gain mode (0-21) |
| <span class="cmd-setting">vga</span> | integer | <span class="cmd-value">10</span> | VGA gain in Free mode (0-14) |
| <span class="cmd-setting">mixer</span> | auto/integer | <span class="cmd-value">auto</span> | Mixer gain/AGC in Free mode (0-14 or AUTO) |
| <span class="cmd-setting">lna</span> | auto/integer | <span class="cmd-value">auto</span> | LNA gain/AGC in Free mode (0-14 or AUTO) |
| <span class="cmd-setting">biastee</span> | boolean | <span class="cmd-value">false</span> | Enable/disable bias tee power |

</div>
