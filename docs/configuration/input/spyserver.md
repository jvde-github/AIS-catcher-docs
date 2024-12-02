# SpyServer
<div class="command-container">

      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-y</span>
        <span class="cmd-value">url</span>
        <span class="cmd-flag">-gy</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
        <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-y</span>
        <span class="cmd-value">url</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gy</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

For [SpyServer](https://airspy.com/)  use the ``-y`` switch like:
```bash
AIS-catcher -y 192.168.1.235 5555 -gy GAIN 14
```

## Summary Settings


| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">device-specific</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">-</span> | Data type for input source |
| <span class="cmd-setting">URL</span> | string | <span class="cmd-value">-</span> | Full connection URL (sdr://host:port) |
| <span class="cmd-setting">HOST</span> | string | <span class="cmd-value">localhost</span> | SpyServer host address |
| <span class="cmd-setting">PORT</span> | string | <span class="cmd-value">1234</span> | SpyServer port |
| <span class="cmd-setting">GAIN</span> | float | <span class="cmd-value">0.0</span> | Tuner gain (0-50 dB) |
| <span class="cmd-setting">TIMEOUT</span> | integer | <span class="cmd-value">2</span> | Connection timeout in seconds |