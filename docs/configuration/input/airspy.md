# AirSpy Mini/R2

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        [<span class="cmd-flag">-d</span> <span class="cmd-value">serial number</span>]
        <span class="cmd-flag">-gm</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

The AirSpy Mini/R2 requires careful gain configuration as described [here](https://airspy.com/quickstart/).  As outlined in that reference there are three different gain modes: linearity, sensitivity and so-called free. These can be set via the ```-gm```switch when using the AirSpy. 

We can activate 'linearity' mode with gain ```10```using the following ```AIS-catcher``` command line:

```bash
AIS-catcher -gm linearity 10
```
Settings can also be provided per stage:
```bash
AIS-catcher -gm lna AUTO vga 12 mixer 12
```
More guidance on setting the gain model and levels can be obtained in the mentioned link.

#### Summary Setings


| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">device-specific</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000, 0=auto) |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">auto</span> | Data type for input source |
| <span class="cmd-setting">SENSITIVITY</span> | integer | <span class="cmd-value">-</span> | Sensitivity gain mode (0-21) |
| <span class="cmd-setting">LINEARITY</span> | integer | <span class="cmd-value">17</span> | Linearity gain mode (0-21) |
| <span class="cmd-setting">VGA</span> | integer | <span class="cmd-value">10</span> | VGA gain in Free mode (0-14) |
| <span class="cmd-setting">MIXER</span> | auto/integer | <span class="cmd-value">auto</span> | Mixer gain/AGC in Free mode (0-14 or AUTO) |
| <span class="cmd-setting">LNA</span> | auto/integer | <span class="cmd-value">auto</span> | LNA gain/AGC in Free mode (0-14 or AUTO) |
| <span class="cmd-setting">BIASTEE</span> | boolean | <span class="cmd-value">false</span> | Enable/disable bias tee power |

