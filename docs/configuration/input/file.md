# Input from file and stdin
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-r</span>
        <span class="cmd-value">filename</span>
        <span class="cmd-flag">-ga</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>

      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-r</span>
        <span class="cmd-value">format</span>
        <span class="cmd-value">filename</span>
        <span class="cmd-flag">-ga</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>

</div>
AIS-catcher can read from a file with the switch ``-r`` followed by the filename and with a ``.`` or ``stdin`` it reads from stdin, e.g. ``-r .``.
```bash
AIS-catcher -r .
```

 The following command records a signal with ```rtl_sdr``` at a sampling rate of 288K Hz and pipes it to AIS-catcher for decoding:
```bash
rtl_sdr -s 288K -f 162M  - | AIS-catcher -r . -s 288K -v
```
The same mechanism can be used to apply other transformations on the signal, e.g. downsampling with ``sox``:
```bash
sox -c 2 -r 1536000 -b 8 -e unsigned -t raw posterholt.raw -t raw -b 16 -e signed -r 96000 - |AIS-catcher -s 96K -r CS16 . -v
```
For reference, as per version 0.36, AIS-catcher has the option to use the internal sox library directly if included in your build:
```bash
AIS-catcher -s 1536K -r CU8 posterholt.raw -v -go SOXR on 
```
Default assumption is that the file is in raw unsigned 8-bit IQ format. Alternative formats can be set via `-gr` (see below) and can even include NMEA strings in text input. 

## Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| FILE | string | - | Input file path or "stdin" for standard input |
| LOOP | boolean | false | Enable continuous file looping |