# SoapySDR

<div class="command-container">
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-gu</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

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

## Summary Settings

<div class="input-table" markdown>

| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">0</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000, 0=off) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| <span class="cmd-setting">format</span> | string | <span class="cmd-value">CF32</span> | Data type for input source |
| Specific Options | | | |
| <span class="cmd-setting">device</span> | string | <span class="cmd-value">""</span> | SoapySDR device arguments string |
| <span class="cmd-setting">gain</span> | string | <span class="cmd-value">-</span> | Gain settings in key=value pairs |
| <span class="cmd-setting">stream</span> | string | <span class="cmd-value">-</span> | Stream arguments in key=value pairs |
| <span class="cmd-setting">setting</span> | string | <span class="cmd-value">-</span> | Device settings in key=value pairs |
| <span class="cmd-setting">antenna</span> | string | <span class="cmd-value">-</span> | Antenna selection |
| <span class="cmd-setting">agc</span> | boolean | <span class="cmd-value">true</span> | Enable/disable Automatic Gain Control |
| <span class="cmd-setting">probe</span> | boolean | <span class="cmd-value">false</span> | Print actual device settings |
| <span class="cmd-setting">ch</span> | integer | <span class="cmd-value">0</span> | Channel selection (0-32) |

</div>