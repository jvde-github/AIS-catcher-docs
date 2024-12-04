# Command Line Usage

## Overview

This guide provides step-by-step instructions for using AIS-Catcher, from verifying installation to a first run with some basic output.

## Basic usage

Check if AIS-Catcher is correctly installed with built-in support for your hardware:
```bash
AIS-catcher -L
```
List the available connected hardware:
```bash
AIS-catcher -l
```

### The First Run

Start AIS decoding with occasional statistics (every 10 seconds):
```bash
AIS-catcher -v 10
```
If you have multiple devices connected, specify the device using:
```bash
AIS-catcher -d:0
```
Alternatively, use the serial number of the device:
```bash
AIS-catcher <serial number>
```

Successful setup will display AIS messages in NMEA format on the screen.

### Output to screen

Control the format of the AIS message output using the `-o` option:

- No output: `-o 0` or `-q`
- Plain NMEA: `-n` or `-o 1`
- NMEA with metadata (default): `-o 2`
- Full JSON decoding: `-o 5`

For example show full content of the AIS messages in JSON format:
```bash
AIS-catcher -o 5
```
The full JSON format for decoded AIS messages is documented [here](../references/JSON-decoding.md). 

To suppress all NMEA messages on the screen:
```bash
AIS-catcher -q
```

## Activating the Web Viewer

Create a web viewer accessible from your local network to visualize AIS data:

```bash
AIS-catcher -N 8100
```

The web viewer will be available at `http://localhost:8100`. It can also be accessed from any device on the same network using the machine's IP address annd defined port number.

Customization options for the web viewer are available in the [configuration settings](../configuration/output/web-viewer.md).


### Sharing your data

#### Community Feed

The next step is to share the data with other programs or services. 
Share your feed with the AIS-Catcher community and view others’ data: 
```bash
AIS-catcher -X <your sharing key>
```
Omitting the sharing key will share data anonymously and a  key can be created at [aiscatcher.org](https://aiscatcher.org/join). 

#### Sharing over UDP
Additionally, for sending the messages via UDP to ports 10110 and 10111,  use the following command:
```bash
AIS-catcher  -u 127.0.0.1 10110 -u 127.0.0.1 10111
```

If successful, NMEA messages will start to come in, appear on the screen and send as raw NMEA  to `127.0.0.1` port `10110` and port `10111`. This is an ideal connection method for visualization in software like OpenCPN or for AIS aggregator websites such as MarineTraffic or VesselFinder.


### Device Specific Settings
For RTL-SDR devices performance can be sensitive to the device settings. In general, a good starting point is the following:
```bash
AIS-catcher -gr RTLAGC on TUNER auto -a 192K
```
It has been reported by several users that adding a bandwidth setting of ``-a 192K`` can be beneficial so it is worthwhile to try with and without this filter. Finding the best settings for your hardware requires some systematic experimentation whereby one parameter is changed at a time, e.g. switch RTLAGC ``on`` or ``off``, set the TUNER to ``auto`` or try fixed tuner gains between 0 and 50. 

The hardware settings available depend on the specific SDR and more details can be found in our [Configuration Section](../configuration/overview.md).

### Performance Considerations
AIS-catcher also supports the 18 Euro RPI Zero W. However, the hardware might not keep up with the high data flow. This can sometimes be resolved by activating **fast downsampling** via:
```bash
AIS-catcher -F
```
Fast downsampling uses approximations and comes at a very small performance degradation, so is not set by default. If your device still struggles, you can try running at a sample rate of 288K (`-s 288K`):
```bash
AIS-catcher -s 288K
```

Reception will be impacted though. Unfortunately, latest feedback seems to be that this is best way to run on the Zero W as this Zero is struggling with the high data throughput and lowering the sample rate is the only option. Another drawback of these lower cost boards is that they can create interference that impacts the radio reception.

### Where to go from here?

For more details on all available settings, [visit](../configuration/overview.md) our detailed coniguration pages.

## Detailed settings

````
AIS-catcher (build Nov 19 2024) v0.60-312-g4f7b402d
(C) Copyright 2021-2024 jvde-github and other contributors
This is free software; see the source for copying conditions.There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
use: AIS-catcher [options]

	[-a xxx - set tuner bandwidth in Hz (default: off)]
	[-b benchmark demodulation models for time - for development purposes (default: off)]
	[-c [AB/CD] - [optional: AB] select AIS channels and optionally the NMEA channel designations]
	[-C [filename] - read configuration settings from file]
	[-D [connection string] - write messages to PostgreSQL database]
	[-e [baudrate] [serial port] - read NMEA from serial port at specified baudrate]
	[-f [filename] write NMEA lines to file]
	[-F run model optimized for speed at the cost of accuracy for slow hardware (default: off)]
	[-h display this message and terminate (default: false)]
	[-H [optional: url] - send messages via HTTP, for options see documentation]
	[-i [interface] - read NMEA2000 data from socketCAN interface - Linux only]
	[-I [interface] - push messages as NMEA2000 data to a socketCAN interface - Linux only]
	[-m xx - run specific decoding model (default: 2), see README for more details]
	[-M xxx - set additional meta data to generate: T = NMEA timestamp, D = decoder related (signal power, ppm) (default: none)]
	[-n show NMEA messages on screen without detail (-o 1)]
	[-N [optional: port][optional settings] - start http server at port, see README for details]
	[-o set output mode (0 = quiet, 1 = NMEA only, 2 = NMEA+, 3 = NMEA+ in JSON, 4 JSON Sparse, 5 JSON Full (default: 2)]
	[-O MMSI - sets the own mmsi of the receiver]
	[-p xxx - set frequency correction for device in PPM (default: zero)]
	[-P xxx.xx.xx.xx yyy - TCP destination address and port (default: off)]
	[-q suppress NMEA messages to screen (-o 0)]
	[-s xxx - sample rate in Hz (default: based on SDR device)]
	[-S xxx - TCP server for NMEA lines at port xxx]
	[-T xx - auto terminate run with SDR after xxx seconds (default: off)]
	[-u xxx.xx.xx.xx yyy - UDP destination address and port (default: off)]
	[-v [option: xx] - enable verbose mode, optional to provide update frequency of xx seconds (default: false)]
	[-X connect to AIS community feed at aiscatcher.org (default: off)]
	[-Q publish data to MQTT server]

	Device selection:

	[-d:x - select device based on index (default: 0)]
	[-d xxxx - select device based on serial number]
	[-e baudrate port - open device at serial port with given baudrate]
	[-l list available devices and terminate (default: off)]
	[-L list supported SDR hardware and terminate (default: off)]
	[-r [optional: yy] filename - read IQ data from file or stdin (.), short for -r -ga FORMAT yy FILE filename
	[-t [[protocol]] [host [port]] - read IQ data from remote RTL-TCP instance]
	[-w filename - read IQ data from WAV file, short for -w -gw FILE filename]
	[-x [server][port] - UDP input of NMEA messages at port on server
	[-y [host [port]] - read IQ data from remote SpyServer]
	[-z [optional [format]] [optional endpoint] - read IQ data from [endpoint] in [format] via ZMQ (default: format is CU8)]

	Device specific settings:

	[-ga RAW file: FILE [filename] FORMAT [CF32/CS16/CU8/CS8] ]
	[-ge Serial Port: PRINT [on/off]
	[-gf HACKRF: LNA [0-40] VGA [0-62] PREAMP [on/off] ]
	[-gh Airspy HF+: TRESHOLD [low/high] PREAMP [on/off] ]
	[-gm Airspy: SENSITIVITY [0-21] LINEARITY [0-21] VGA [0-14] LNA [auto/0-14] MIXER [auto/0-14] BIASTEE [on/off] ]
	[-gr RTLSDRs: TUNER [auto/0.0-50.0] RTLAGC [on/off] BIASTEE [on/off] ]
	[-gs SDRPLAY: GRDB [0-59] LNASTATE [0-9] AGC [on/off] ]
	[-gt RTLTCP: HOST [address] PORT [port] TUNER [auto/0.0-50.0] RTLAGC [on/off] FREQOFFSET [-150-150] PROTOCOL [none/rtltcp] TIMEOUT [1-60] ]
	[-gu SOAPYSDR: DEVICE [string] GAIN [string] AGC [on/off] STREAM [string] SETTING [string] CH [0+] PROBE [on/off] ANTENNA [string] ]
	[-gw WAV file: FILE [filename] ]
	[-gy SPYSERVER: HOST [address] PORT [port] GAIN [0-50] ]
	[-gz ZMQ: ENDPOINT [endpoint] FORMAT [CF32/CS16/CU8/CS8] ]

	Model specific settings:

	[-go Model: AFC_WIDE [on/off] FP_DS [on/off] PS_EMA [on/off] SOXR [on/off] SRC [on/off] DROOP [on/off] ]

````
