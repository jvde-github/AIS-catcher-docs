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
|  <span class="cmd-setting">TUNER</span> | auto/float | <span class="cmd-value">auto</span> | Tuner gain/AGC (0-50 dB or AUTO) |
|  <span class="cmd-setting">RTLAGC</span> | boolean | <span class="cmd-value">true</span>  | Enable/disable RTL2832U AGC |
|  <span class="cmd-setting">BIASTEE</span> | boolean | <span class="cmd-value">false</span>  | Enable/disable bias tee power |
|  <span class="cmd-setting">BUFFER_COUNT</span> | integer | <span class="cmd-value">24</span>  | Number of FIFO buffers (1-100) |
