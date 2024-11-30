### AirSpy Mini/R2

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-d</span>
        <span class="cmd-value">serial code</span>
        <span class="cmd-flag">-gm</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
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
| SENSITIVITY | integer | - | Sensitivity gain mode (0-21) |
| LINEARITY | integer | 17 | Linearity gain mode (0-21) |
| VGA | integer | 10 | VGA gain in Free mode (0-14) |
| MIXER | auto/integer | auto/10 | Mixer gain/AGC in Free mode (0-14 or AUTO) |
| LNA | auto/integer | auto/10 | LNA gain/AGC in Free mode (0-14 or AUTO) |
| BIASTEE | boolean | false | Enable/disable bias tee power |