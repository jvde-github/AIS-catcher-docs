# Input as WAV-file

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-w</span>
        <span class="cmd-value">filename</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>


## Summary Settings

## Specific Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">FILE</span> | string | <span class="cmd-value">-</span> | WAV file path to read from |
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">From File</span> | Input format (CF32, CU8, CS16) |
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">From file</span> | Sample rate from WAV file |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000), 0=auto |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |