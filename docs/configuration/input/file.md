# Input from file and stdin
<div class="command-container">
            <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-r</span>
        <span class="cmd-flag">-ga</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
      
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-r</span>
        <span class="cmd-value">filename</span>
        <span class="cmd-flag">-ga</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
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

## Reading from STDIN
AIS-catcher can read from a file with the switch ``-r`` followed by the filename and with a ``.`` or ``stdin`` it reads from stdin:
```bash
AIS-catcher -r .
```
## Sequencing on the command line
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
Default assumption is that the file is in raw unsigned 8-bit IQ format (CU8). Alternative formats can be set via  the FORMAT setting. 

## NMEA0183 input from file

For a text file with NMEA input, we can use:
```bash
AIS-catcher -r txt nmea-file
```
Or equivalently for illustration purposes:
```bash
AIS-catcher -r -ga FORMAT txt file nmea-file
```

## Summary Settings

<div class="input-table" markdown>

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">SAMPLE_RATE</span> | integer | <span class="cmd-value">1536K</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">BANDWIDTH</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000), 0 = off |
| <span class="cmd-setting">FREQOFFSET</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |  
| <span class="cmd-setting">FORMAT</span> | string | <span class="cmd-value">CU8</span> | Data type for input source |
| Specific Options | | | |
| <span class="cmd-setting">FILE</span> | string | <span class="cmd-value">-</span> | Input file path or "stdin" for standard input |
| <span class="cmd-setting">LOOP</span> | boolean | <span class="cmd-value">false</span> | Enable continuous file looping |

</div>
