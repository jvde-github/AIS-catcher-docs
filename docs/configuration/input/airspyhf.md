### AirSpy HF+
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-d</span>
        <span class="cmd-value">serial code</span>
        <span class="cmd-flag">-gh</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
</div>
Gain settings specific for the AirSpy HF+ can be set on the command line with the ```-gh``` switch. The following command switches off the preamp:

```bash
AIS-catcher -gh preamp OFF
```

Please note that only AGC mode is supported so there are limited options.

#### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| PREAMP | boolean | false | Enable/disable preamplifier |
| THRESHOLD/ | enum | "LOW" | AGC threshold setting ("HIGH" or "LOW") |
