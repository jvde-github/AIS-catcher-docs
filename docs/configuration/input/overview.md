# Input Configuration

## Device Selection and Discovery

To list all connected compatible hardware devices:
```bash
AIS-catcher -l
```
To select a specific device, use either:

`-d:N` where N is the device number from the list
`-d SERIAL` where SERIAL is the device's serial number

## Universal Settings
The following settings apply across all input devices. For the most common options there is a command line option available that can be used as a shortcut. 

| Setting | Command Line | Key | Description | Range | Default |
|---------|--------------|---|----------|--------|---------|
| Sample Rate | `-s RATE` | SAMPLE_RATE | Sampling rate in Hz | 0-20,000,000 | Device-specific |
| Bandwidth | `-a BW` | BANDWIDTH | Tuner bandwidth in Hz | 0-1,000,000 | 0 (auto) |
| Frequency Correction | `-p PPM` |  FREQOFFSET | Frequency correction in PPM | -150 to +150 | 0 |
| Data Type | | FORMAT | Data type for input source |

For example, to set the sample rate to 1536K, frequecy offset of your device to 1 ppm and bandwidth to 192K:
```bash
AIS-catcher -s 1536K -a 192K -p 1
```

The format option sets the data type for the input source. This is less relevant for SDRs but is useful when reading raw data from file or an internet connection.

## Multiple device input

We can run with multiple receivers in parallel. For example, one dongle for channel A+B and one dongle for channel C+D. To run with two receivers in parallel you can use a command like:
```bash
AIS-catcher -d serial1 -v -d serial2 -c CD -v -N 8100
```

Similarly, this functionality allows to receive input from an AIS receiver over UDP via a UDP server and a connected GPS device in parallel, e.g.:
```bash
AIS-catcher -e 38400 /dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox_7_-_GPS_GNSS_Receiver-if00 -x 192.168.1.235 4002
```
The first receiver (`-e ...`) reads from a GPS device that is connected and emits NMEA lines. The second receiver (`-x`) reads AIS NMEA lines at port 4002 coming from another instance of AIS-catcher. The station is now plotted on the map with the location as provided
by the GPS coordinates. The web page has an option to fix the center of the map on the location of the receiving station (right-click on the station icon on the map).


## Further Documentation

For detailed information about specific devices and input types, please refer to the following documentation:

### SDR Devices
- [RTL-SDR Configuration](rtlsdr.md)
- [AirSpy Configuration](airspy.md)
- [AirSpy HF+ Configuration](airspyhf.md)
- [HackRF Configuration](hackrf.md)
- [SDRPlay Configuration](sdrplay.md)
- [SoapySDR Configuration](soapysdr.md)

### Network and File Input
- [TCP Input](tcp.md)
- [UDP Input](udp.md)
- [SpyServer Input](spyserver.md)
- [File Input](file.md)
- [WAV File Input](wav.md)

### Other Inputs
- [Serial Port Configuration](serial.md)
- [NMEA2000 Configuration](NMEA2000.md)

See the [Input Overview](overview.md) for a complete introduction to all input options.