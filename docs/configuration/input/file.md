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
AIS-catcher can read input in two ways using the -r switch: from a file by specifying a filename, or from standard input by using either a dot (.) or stdin as the argument:
```bash
AIS-catcher -r .
```
## Pipeline example
AIS-catcher can be integrated into command-line processing pipelines for real-time signal processing. For example, you can capture radio signals using rtl_sdr and pipe them directly to AIS-catcher for decoding:
```bash
rtl_sdr -s 288K -f 162M  - | AIS-catcher -r . -s 288K -v
```
You can also perform signal transformations using tools like `sox`. Here's an example of downsampling a signal before processing:
```bash
sox -c 2 -r 1536000 -b 8 -e unsigned -t raw posterholt.raw -t raw -b 16 -e signed -r 96000 - |AIS-catcher -s 96K -r CS16 . -v
```
> As of version 0.36, AIS-catcher includes built-in sox functionality (if compiled with this feature), allowing for
> built-in usage of sox:
 >```bash
>AIS-catcher -s 1536K -r CU8 posterholt.raw -v -go SOXR on
> ```

By default, AIS-catcher expects input files to be in raw unsigned 8-bit IQ format (CU8). You can specify other formats using the FORMAT setting.

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

| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">1536K</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000), 0 = off |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |  
| <span class="cmd-setting">format</span> | string | <span class="cmd-value">CU8</span> | Data type for input source |
| Specific Options | | | |
| <span class="cmd-setting">file</span> | string | <span class="cmd-value">-</span> | Input file path or "stdin" for standard input |
| <span class="cmd-setting">loop</span> | boolean | <span class="cmd-value">false</span> | Enable continuous file looping |

</div>
