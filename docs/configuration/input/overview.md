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

| Option | Command Line | Setting | Description | Range | Default |
|---------|--------------|---|----------|--------|---------|
| Sample Rate | `-s RATE` | <span class="cmd-setting">SAMPLE_RATE</span> | Sampling rate in Hz | 0-20,000,000 | Device-specific |
| Bandwidth | `-a BW` | <span class="cmd-setting">BANDWIDTH</span> | Tuner bandwidth in Hz | 0-1,000,000 | 0 (none) |
| Frequency Correction | `-p PPM` | <span class="cmd-setting">FREQOFFSET</span> | Frequency correction in PPM | -150 to +150 | 0 |
| Data Type | | <span class="cmd-setting">FORMAT</span> | CU8, CF32, CS16, CS8, TXT| | Device-specific |


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


<style>
.device-links {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin: 1rem 0;
}

</style>

<div class="device-links" markdown>
  <div markdown>

### SDR Devices

- [RTL-SDR ](rtlsdr.md)
- [AirSpy ](airspy.md)
- [AirSpy HF+ ](airspyhf.md)
- [HackRF ](hackrf.md)
- [SDRPlay ](sdrplay.md)
- [SoapySDR ](soapysdr.md)
</div>
<div  markdown>

### Other Inputs

- [TCP Input](tcp.md)
- [UDP Input](udp.md)
- [SpyServer Input](spyserver.md)
- [File ](file.md)
- [Wave File ](wav.md)
- [Serial Port ](serial.md)
- [NMEA2000 ](NMEA2000.md)
  </div>
</div>

See the [Input Overview](overview.md) for a complete introduction to all input options.
