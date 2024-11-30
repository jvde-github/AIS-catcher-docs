# HackRF

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-d</span>
        <span class="cmd-value">serial code</span>
        <span class="cmd-flag">-gf</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
</div>

Settings specific for the HackRF can be set on the command line with the ```-gf``` switch, e.g.:

```bash
AIS-catcher -gf lna 16 vga 16 preamp OFF
```
## Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| LNA | integer | 8 | LNA (RF) gain in dB (0-40, rounded to multiples of 8) |
| VGA | integer | 20 | VGA (IF) gain in dB (0-62, rounded to multiples of 2) |
| PREAMP | boolean | false | Enable/disable preamplifier |
