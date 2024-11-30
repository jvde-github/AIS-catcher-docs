# SDRPlay RSP1/RSP1A/RSPDX (API 3.x)
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-d</span>
        <span class="cmd-value">serial code</span>
        <span class="cmd-flag">-gs</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
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
| AGC | boolean | false | Enable/disable Automatic Gain Control |
| LNASTATE | integer | 0 | LNA state/gain (0-9) |
| GRDB | integer | 32 | RF gain reduction in dB (0-59) |
| ANTENNA | char | 'A' | Antenna selection (A/B/C) for RSPdx models |