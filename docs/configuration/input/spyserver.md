# SpyServer
<div class="command-container">

      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-y</span>
        <span class="cmd-value">url</span>
        <span class="cmd-flag">-gy</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
        <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-y</span>
        <span class="cmd-value">url</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gy</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
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
| URL | string | - | Full connection URL (sdr://host:port) |
| HOST | string | "localhost" | SpyServer host address |
| PORT | string | "1234" | SpyServer port |
| GAIN | float | 0.0 | Tuner gain (0-50 dB) |
| TIMEOUT | integer | 2 | Connection timeout in seconds |