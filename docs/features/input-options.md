# Input Configuration

For specific hardware we can list the connected hardware with:
```bash
AIS-catcher -l
```
To select particular hardware use the `-d` option followed by `:` and the device number in the list or with `-d` followed by the serial number. For selecting input via other input devices use the relevant command line option. For more details see below.


## Input from file and stdin
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

### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| FILE | string | - | Input file path or "stdin" for standard input |
| LOOP | boolean | false | Enable continuous file looping |

## Input over TCP
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">url</span>
        <span class="cmd-flag">-gt</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>

    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gt</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">protocol</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gt</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
</div>

Input over TCP with various protocols can be done with `-t` followed by the URL of the server. As an example, to read raw NMEA from a TCP server we can use:
```bash
AIS-catcher -t txt://192.168.1.120:5011
```

Various protocols are supported as input. The table below lists the available protocols and their descriptions:

| Protocol | Description                                   |
| :------- | :------------------------------------------- |
| `txt`    | Raw NMEA text.                               |
| `gpsd`   | GPSD server input.                           |
| `rtltcp` | Connecting to an RTL-TCP server.             |
| `mqtt`   | MQTT with JSON payload.                      |
| `wsmqtt` | MQTT with JSOP payload over WebSockets.                        |

Use the appropriate protocol based on your server's configuration and data format. 

### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| URL | string | - | Full connection URL including protocol, host, port, etc |
| PROTOCOL | enum | "RTLTCP" | Connection protocol (RTLTCP, MQTT, GPSD, WS, WSMQTT, TXT, NONE) |
| HOST | string | - | Remote host address |
| PORT | string | - | Remote port number |

## Input as UDP server
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-x</span>
        <span class="cmd-value">server</span>
        <span class="cmd-value">port</span>
    </div>
</div>
You can receive NMEA input via a built-in UDP server:
```bash
AIS-catcher -x 192.168.1.235 4002
```

### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| PORT | string | - | UDP server port to listen on |
| SERVER | string | - | UDP server address to bind to |

## Device specific settings

The command line allows you to set some device-specific parameters. AIS-catcher follows the default settings and naming conventions for the devices as much as possible so that optimal parameters determined by SDR software for signal analysis (e.g. SDR#, SDR++, SDRangel) can be directly copied. Below some examples. Note that these settings are not selecting the device used for decoding itself, this needs to be done via the ``-d`` switch (or `-e/s/r/z`). If a device is not connected or used for decoding any specific settings are simply ignored.

### RTL SDR

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

#### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| TUNER | auto/float | auto/33.0 | Tuner gain/AGC (0-50 dB or AUTO) |
| RTLAGC | boolean | true | Enable/disable RTL2832U AGC |
| BIASTEE | boolean | false | Enable/disable bias tee power |
| BUFFER_COUNT | integer | 24 | Number of FIFO buffers (1-100) |

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

### AirSpy Mini/R2

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-d</span>
        <span class="cmd-value">serial code</span>
        <span class="cmd-flag">-gm</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
</div>

The AirSpy Mini/R2 requires careful gain configuration as described [here](https://airspy.com/quickstart/).  As outlined in that reference there are three different gain modes: linearity, sensitivity and so-called free. These can be set via the ```-gm```switch when using the AirSpy. 

We can activate 'linearity' mode with gain ```10```using the following ```AIS-catcher``` command line:

```bash
AIS-catcher -gm linearity 10
```
Settings can also be provided per stage:
```bash
AIS-catcher -gm lna AUTO vga 12 mixer 12
```
More guidance on setting the gain model and levels can be obtained in the mentioned link.

#### Summary Setings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| SENSITIVITY | integer | - | Sensitivity gain mode (0-21) |
| LINEARITY | integer | 17 | Linearity gain mode (0-21) |
| VGA | integer | 10 | VGA gain in Free mode (0-14) |
| MIXER | auto/integer | auto/10 | Mixer gain/AGC in Free mode (0-14 or AUTO) |
| LNA | auto/integer | auto/10 | LNA gain/AGC in Free mode (0-14 or AUTO) |
| BIASTEE | boolean | false | Enable/disable bias tee power |

### SDRPlay RSP1/RSP1A/RSPDX (API 3.x)
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-d</span>
        <span class="cmd-value">serial code</span>
        <span class="cmd-flag">-gs</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
</div>

Settings specific for the SDRPlay  can be set on the command line with the ```-gs``` switch, e.g.:
```bash
AIS-catcher -gs lnastate 5
```


#### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| AGC | boolean | false | Enable/disable Automatic Gain Control |
| LNASTATE | integer | 0 | LNA state/gain (0-9) |
| GRDB | integer | 32 | RF gain reduction in dB (0-59) |
| ANTENNA | char | 'A' | Antenna selection (A/B/C) for RSPdx models |

### Serial Port
<div class="command-container">
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-e</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-ge</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-e</span>
        <span class="cmd-value">baudrate</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-ge</span>
        <span class="cmd-setting">setting</span>
        <span class="cmd-value">value</span>
        ...
    </div>
</div>
Settings specific for reading NMEA lines from a serial port can all be set with the `e` switch fow now, e.g. on Linux:
```bash
AIS-catcher -e 368400 /dev/serial1

```

To dump the raw input from the serial device on-screen use `-`ge print on`.

#### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| BAUDRATE | integer | 38400 | Serial port speed |
| PORT | string | "" | Serial port device path/name |
| PRINT | boolean | false | Enable debug printing of received data |

### HackRF

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
#### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| LNA | integer | 8 | LNA (RF) gain in dB (0-40, rounded to multiples of 8) |
| VGA | integer | 20 | VGA (IF) gain in dB (0-62, rounded to multiples of 2) |
| PREAMP | boolean | false | Enable/disable preamplifier |

### SpyServer
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

#### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| URL | string | - | Full connection URL (sdr://host:port) |
| HOST | string | "localhost" | SpyServer host address |
| PORT | string | "1234" | SpyServer port |
| GAIN | float | 0.0 | Tuner gain (0-50 dB) |
| TIMEOUT | integer | 2 | Connection timeout in seconds |

### SoapySDR

In general we recommend to use the built-in drivers for supported SDR  devices. However, AIS-catcher also supports a wide variety of other devices via the [SoapySDR library](https://github.com/pothosware/SoapySDR/wiki) which is an independent SDR support library. SoapySDR is not included by default in the standard build. To enable SoapySDR support follow the build instructions below but replace the ```cmake``` call with:
```bash
cmake .. -DSOAPYSDR=ON
```
The result is that AIS-catcher adds a few additional "devices" to the device list (```-l```): a generic SoapySDR device and one device for each receiving channel for each device, e.g. with one RTL-SDR dongle connected this would look like:
```
Found 3 device(s):
0: Realtek, RTL2838UHIDIR, SN: 00000001
1: SOAPYSDR, 1 device(s), SN: SOAPYSDR
2: SOAPYSDR, driver=rtlsdr,serial=00000001, SN: SCH0-00000001
```
To start streaming via Soapy we can use:
```bash
AIS-catcher -d SCH0-00000001
```
Note that the serial number has a prefix of ```SCH0``` (short for SoapySDR Channel 0) to distinguish it from the device accessed via the native SDR library. Alternatively, we can use a device-string to select the device: 
```bash
AIS-catcher -d SOAPYSDR -gu device "serial=00000001,driver=rtlsdr" -s 1536K
```
Stream arguments and gain arguments can be set similarly via ```-gu STREAM``` and ```-gu GAIN``` followed by an argument string (if it contains spaces use ""). Please note that SoapySDR does not signal if the input parameters for the device are not set properly. We therefore added the ```-gu PROBE on``` switch which displays the actual settings used, e.g.
```bash
AIS-catcher -d SOAPYSDR -s 1536K -gu GAIN "TUNER=37.3" PROBE on SETTINGS "biastee=true"
```
To complete the example, this command also sets the tuner gain for the RTL-SDR to 37.3 and switches on the bias-tee via the SETTING command giving access to the device's extra settings.

If the sample rates for a device are not supported by AIS-catcher, the SOXR functionality could be considered (e.g. ```-go SOXR on```). Again, we advise to use the built-in drivers and include resampling functionality where possible.  

#### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| DEVICE | string | "" | SoapySDR device arguments string |
| GAIN | string | - | Gain settings in key=value pairs |
| STREAM | string | - | Stream arguments in key=value pairs |
| SETTING | string | - | Device settings in key=value pairs |
| ANTENNA | string | "" | Antenna selection |
| AGC | boolean | true | Enable/disable Automatic Gain Control |
| PROBE | boolean | false | Print actual device settings |
| CH | integer | 0 | Channel selection (0-32) |
