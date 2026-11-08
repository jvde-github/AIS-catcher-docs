# Command Line

On the command line, every setting is a switch: a dash and a letter, often followed by values. AIS-catcher does what the switches say and nothing else.

## Check the install

See which receivers this build supports:

```bash
AIS-catcher -L
```

See which receivers are connected:

```bash
AIS-catcher -l
```

## A first run

```bash
AIS-catcher -v 10
```

AIS-catcher starts the first receiver it finds, shows each message on the screen, and prints statistics every 10 seconds. With several receivers connected, pick one by its number in the `-l` list, or by its serial number:

```bash
AIS-catcher -d:1 -v 10
AIS-catcher -d 00000001 -v 10
```

## How a command line is built

A switch takes its values, then any settings as name and value pairs. This sends messages over UDP and names the output:

```bash
AIS-catcher -u 192.168.1.20 10110 description "Chart plotter"
```

- **Switches can repeat.** Two `-u` switches are two UDP outputs.
- **Settings follow their switch.** They apply to the switch before them, until the next switch.
- **Names are not case-sensitive** on the command line: `RTLAGC on` and `rtlagc on` are the same. Put a value with spaces in quotes.
- **An unknown setting stops AIS-catcher** with `unknown setting "..."`, so a typo never goes unnoticed.

Receiver settings go with a `-g` switch, whose second letter names the device:

```bash
AIS-catcher -gr tuner 33.3 rtlagc on
```

| Switch | Device | Switch | Device |
|--------|--------|--------|--------|
| `-gr` | [RTL-SDR](../configuration/input/rtlsdr.md) | `-gt` | [RTL-TCP](../configuration/input/tcp.md) |
| `-gm` | [Airspy](../configuration/input/airspy.md) | `-gy` | [SpyServer](../configuration/input/spyserver.md) |
| `-gh` | [Airspy HF+](../configuration/input/airspyhf.md) | `-gz` | [ZMQ](../configuration/input/tcp.md) |
| `-gd` | [HydraSDR](../configuration/input/hydrasdr.md) | `-ge` | [Serial port](../configuration/input/serial.md) |
| `-gf` | [HackRF](../configuration/input/hackrf.md) | `-ga` | [Raw file](../configuration/input/file.md) |
| `-gs` | [SDRplay](../configuration/input/sdrplay.md) | `-gw` | [WAV file](../configuration/input/wav.md) |
| `-gu` | [SoapySDR](../configuration/input/soapysdr.md) | `-go` | [The decoding model](../configuration/model.md) |

Every switch and setting is in the reference: [inputs](../configuration/input/overview.md), [decoding](../configuration/model.md) and [outputs](../configuration/output/overview.md).

## From the command line to a file

`-J` writes the command line as a [configuration file](json-configuration.md) instead of running it:

```bash
AIS-catcher -gr tuner 33.3 -u 192.168.1.20 10110 -J config.json
```

Without a file name, it prints the configuration on the screen. `-C` reads a file back, and can be combined with other switches:

```bash
AIS-catcher -C config.json -v 10
```

## Every switch

`AIS-catcher -h` prints this list:

````
use: AIS-catcher [options]

	[-a xxx - set tuner bandwidth in Hz (default: off)]
	[-b benchmark demodulation models for time - for development purposes (default: off)]
	[-c [AB/CD] - [optional: AB] select AIS channels and optionally the NMEA channel designations]
	[-C [filename] - read configuration settings from file]
	[-D [connection string] - write messages to a database: libpq string, sqlite:[file] or csv:[directory]]
	[-e [baudrate] [serial port] - read NMEA from serial port at specified baudrate]
	[-E [config file] [bind address:port] [TLS_CERT file TLS_KEY file] - managed mode: engine run from config file with control server, must be only option (defaults: config.json, control port 8118, viewer on control port + 1, local access without password; use 0.0.0.0:port for LAN access with password)]
	[-f [filename] write NMEA lines to file]
	[-F run model optimized for speed at the cost of accuracy for slow hardware (default: off)]
	[-G [LEVEL level] [SYSTEM on] - control logging (levels: DEBUG, INFO, WARNING, ERROR, CRITICAL) or enable system logging]
	[-h display this message and terminate (default: false)]
	[-K - print a new API key with its SHA-256 and how to use it, and terminate]
	[-J [file] - write this command line as a configuration file and terminate: to the file, or the screen without one; -C reads it, -E runs it in managed mode]
	[-H [optional: url] - send messages via HTTP, for options see documentation]
	[-i [interface] - read NMEA2000 data from socketCAN interface - Linux only]
	[-I [interface] - push messages as NMEA2000 data to a socketCAN interface - Linux only]
	[-m xx - run specific decoding model (default: 2), see README for more details]
	[-M xxx - set additional meta data to generate: T = NMEA timestamp, D = decoder related (signal power, ppm) (default: none)]
	[-n show NMEA messages on screen without detail (-o 1)]
	[-N [optional: port][optional settings] - a web server at port: the map, and api, mcp, system, geojson, kml or metrics switched on; with a message filter it keeps ships of its own; TLS_CERT file TLS_KEY file for HTTPS; KEYS name:scopes:sha256[:limit],... for access by key (scopes data or data+system, limit requests a minute); see README for details]
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
	[-W url [key value]... - events to a webhook (http, https), or the station's state to Home Assistant over MQTT (mqtt, mqtts, ws, wss); keys as in the configuration file, lists comma-separated]
	[-X connect to AIS community feed at www.aiscatcher.org (default: off)]
	[-Q publish data to MQTT server]
	[-Z lat lon - set receiver location (latitude and longitude in decimal degrees)]

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
	[-gd HydraSDR: SENSITIVITY [0-21] LINEARITY [0-21] VGA [0-14] LNA [auto/0-14] MIXER [auto/0-14] BIASTEE [on/off] ]
	[-ge Serial Port: PRINT [on/off] FLOWCONTROL [none/hardware/software] INIT_SEQ [string] ]
	[-gf HACKRF: LNA [0-40] VGA [0-62] PREAMP [on/off] ]
	[-gh Airspy HF+: THRESHOLD [low/high] PREAMP [on/off] ]
	[-gm Airspy: SENSITIVITY [0-21] LINEARITY [0-21] VGA [0-14] LNA [auto/0-14] MIXER [auto/0-14] BIASTEE [on/off] ]
	[-gr RTLSDRs: TUNER [auto/0.0-50.0] RTLAGC [on/off] BIASTEE [on/off] ]
	[-gs SDRPLAY: GRDB [0-59] LNASTATE [0-9] AGC [on/off] ]
	[-gt RTLTCP: HOST [address] PORT [port] TUNER [auto/0.0-50.0] RTLAGC [on/off] FREQOFFSET [-150-150] PROTOCOL [none/rtltcp] TIMEOUT [1-60] ]
	[-gu SOAPYSDR: DEVICE [string] GAIN [string] AGC [on/off] STREAM [string] SETTING [string] CH [0+] PROBE [on/off] ANTENNA [string] ]
	[-gw WAV file: FILE [filename] ]
	[-gy SPYSERVER: HOST [address] PORT [port] GAIN [0-50] ]
	[-gz ZMQ: ENDPOINT [endpoint] FORMAT [CF32/CS16/CU8/CS8] ]

	Model specific settings:

	[-go Model: AFC_WIDE [on/off] FP_DS [on/off] PS_EMA [on/off] SOXR [on/off] SRC [on/off] DROOP [on/off] DD_TRAIN [weight] DD_WEIGHT [weight] ]
````
