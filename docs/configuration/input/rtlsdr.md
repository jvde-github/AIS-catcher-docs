# RTL SDR

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-d</span>
        <span class="cmd-value">serial code</span>
        <span class="cmd-flag">-gr</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
</div>

Gain and other settings specific to the RTL SDR can be set on the command line with the ```-gr``` switch. For example, the following command sets the tuner gain to +33.3 and switches the RTL AGC on:

```bash
AIS-catcher -gr tuner 33.3 rtlagc ON
```

Settings are not case-sensitive.

## Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| TUNER | auto/float | auto/33.0 | Tuner gain/AGC (0-50 dB or AUTO) |
| RTLAGC | boolean | true | Enable/disable RTL2832U AGC |
| BIASTEE | boolean | false | Enable/disable bias tee power |
| BUFFER_COUNT | integer | 24 | Number of FIFO buffers (1-100) |