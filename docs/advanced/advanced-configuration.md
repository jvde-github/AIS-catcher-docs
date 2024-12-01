# Advanced Configuration

## Long Range AIS messages

AIS-catcher has the option to listen at frequency 156.8 Mhz to receive Channel 3/C and 4/D (vs the default A and B around 162 MHz) with the switch ```-c CD```. This follows ideas from a post on the [Shipplotter forum](https://groups.io/g/shipplotter/topic/ais_type_27_long_range/92150532?p=,,,20,0,0,0::recentpostdate/sticky,,,20,2,0,92150532,previd%3D1657138240979957244,nextid%3D1644163712453715490&previd=1657138240979957244&nextid=1644163712453715490). The default decoder is available with the switch ```-c AB```. Note that ``gpsdecode`` cannot handle channel designations C and D in NMEA lines. You can provide an optional argument to use channel designations A and B in the NMEA line with the command ```-c CD AB```.

In a similar fashion `-c X` will decode one channel. This is only useful in some instances, see the ZMQ example below.

## NMEA input

AIS-catcher can be used as a command line utility that decodes NMEA lines in a file and prints the results as JSON. It provides a way to move the JSON analysis to the server side (send over NMEA with minimal metadata) or for unit testing the JSON decoder which was the prime reason for the addition of this feature. As an example:
```bash
echo '!AIVDM,1,1,,B,3776k`5000a3SLPEKnDQQWpH0000,0*78'  | AIS-catcher -r txt . -o 5
```
which produces
```json
{"class":"AIS","device":"AIS-catcher","scaled":true,"channel":"B","nmea":["!AIVDM,1,1,,B,3776k`5000a3SLPEKnDQQWpH0000,0*78"],"type":3,"repeat":0,"mmsi":477213600,"status":5,"status_text":"Moored","turn":0,"speed":0.000000,"accuracy":true,"lon":126.605469,"lat":37.460617,"course":39.000000,"heading":252,"second":12,"maneuver":0,"raim":false,"radio":0}
```
When piping NMEA text lines into AIS-catcher, use format ``TXT`` which ensures that the program immediately processes the incoming characters and will not buffer them first. The NMEA decoder can be activated with the switch `-m 5` but setting the input format to TXT will automatically activate this decoder. 

This functionality opens a few doors. For example, you can use AIS-catcher to read and forward messages from a dAISy Hat (simply read from the file ``cat /dev/serial0`` on Linux) or process the data from Norwegian coastal traffic offered via a TCP server, like this:  
```bash
netcat  153.44.253.27  5631 | AIS-catcher -r txt . -o 5
```

For input via TCP, you can skip the `netcat` command and directly read the input into the program as follows:
```bash
AIS-catcher -t txt 153.44.253.27 5631
```
Again, the `FORMAT txt` option switches off the buffering and automatically selects the NMEA decoder.

Finally, you can also receive NMEA input via a built-in UDP server:
```bash
AIS-catcher -x 192.168.1.235 4002
```

The functionality to read NMEA lines from text files has been used to validate AIS-catcher JSON output on a [file](https://www.aishub.net/ais-dispatcher) with 80K+ lines against [pyais](https://pypi.org/project/pyais/) and [gpsdecode](https://gpsd.io/gpsdecode.html). Only available switches for this decoder are ``-go NMEA_REFRESH`` and ``-go CRC_CHECK`` which force AIS-catcher to, respectively, recalculate the NMEA lines if ``on`` (default ``off``) and ignore messages with incorrect CRC if ``on`` (default ``off``). Example: 
```bash
echo '$AIVDM,1,1,,,3776k`5000a3SLPEKnDQQWpH0000,0*79' | AIS-catcher -r txt . -n -go nmea_refresh on crc_check off
```
returns a warning on the incorrect CRC and:
```
!AIVDM,1,1,,,3776k`5000a3SLPEKnDQQWpH0000,0*3A
```
Note that CRC/checksum is the simple xor-checksum for validating that the NMEA line is not corrupted and not the CRC that is transmitted with the AIS message for a decoder to check the correct reception over air. This latter 16-bit checksum/CRC is not included in the NMEA message.

AIS-catcher will also accept AIVDO input which is typically used for the MMSI of the own ship. You can enable/disable this with: `-go VDO on/off`.

## Specifying Station Location

As discussed above, the webserver will only share a known location of the station with the front-end web viewer if `share_loc` is set for the webserver:
```bash
AIS-catcher -N 8100 share_loc on
```
This option is switched off by default for privacy reasons in case the web viewer is shared externally.
The NMEA decoder accepts NMEA lines from a GPS device (NMEA lines GPRMC, GPGLL and GPGGA):
```bash
echo '$GPGGA, 161229.487, 3723.2475, N, 12158.3416, W, 1, 07, 1.0, 9.0, M, , , , 0000*18' | ./AIS-catcher -r txt .
```
These GPS coordinates will be used to set the location of the station. In this way, the station can be visualized and tracked while on the move. This is useful if you use AIS-catcher to read from a hardware AIS receiver that has a built-in GPS.
Another approach is to read from a GPSD server, e.g. when GPSD listens on post 2947 of the local PC: 
```bash
AIS-catcher -t gpsd localhost 2947 -N 8100 share_loc on` 
```
or from a serial device:
```bash
AIS-catcher -e 38400 /dev/serial/by-id/usb-u-blox_AG_-_www.u-blox.com_u-blox
```
The web viewer has the options `-N use_gps on/off` and `-N own_mmsi xxxxx`. The first enables/disables the use of GPS NMEA input as the location for the receiver station (default is on). The latter sets the station's location as the location of the vessel with the specified MMSI. The own MMSI will be highlighted on the web viewer map.




## Running on RPI Zero W and other devices with performance limitations

AIS-catcher implements a trick to speed up downsampling for RTLSDR input at 1536K samples/second by using fixed point calculations (```-F```). In essence, the downsampling is done 
in 16-bit integers performed in parallel for the I and Q channels using only 32-bit integers.

<p align="center">
<img src="https://raw.githubusercontent.com/jvde-github/AIS-catcher/media/media/raspberry.jpg" width=40% height=40%>
</p>

This feature can activated with the ```-F``` switch and is only available for RTL-SDR running at a rate 1536K per second (the default). 
To give an idea of the performance improvement on a Raspberry Pi Model B Rev 2 (700 MHz), I used the following command to decode from a file on the aforementioned Raspberry Pi:

```bash
AIS-catcher -r posterholt.raw -s 1536K -b -q -v
```
Resulting in 38 messages and the ```-b``` switch prints the timing used for decoding:
```
[AIS engine v0.31]	: 17312.1 ms
```
Adding the ```-F``` switch yielded the same number of messages but the timing is now:
```
[AIS engine (speed optimized) v0.31]	: 7722.32 ms
```
On an RPI Zero W this will bring down CPU load to ~40% and avoid buffer overruns.

## Connecting to GNU Radio via ZMQ

The latest code base of AIS-catcher can take streaming data via ZeroMQ (ZMQ) as input. This eases the interface with packages like GNU Radio. The steps are simple and will be demonstrated by decoding the messages in the AIS example file from [here](https://www.sdrplay.com/iq-demo-files/). AIS-catcher cannot directly decode this file as the file contains only one channel, the frequency is shifted away from the center at 162Mhz and the sample rate of 62.5 KHz is not supported in our program. We can however perform decoding with some help from [``GNU Radio``](https://www.gnuradio.org/). First start AIS-catcher to receive a stream (data format is complex float and sample rate is 96K) at a defined ZMQ endpoint:
```bash
AIS-catcher -z CF32 tcp://127.0.0.1:5555 -s 96000
```
Next we can build a simple GRC model that performs all the necessary steps and has a ZMQ Pub Sink with the chosen endpoint:
![Image](https://raw.githubusercontent.com/jvde-github/AIS-catcher/media/media/SDRuno%20GRC.png)
Running this model, will allow us to successfully decode the messages in the file:

![Image](https://raw.githubusercontent.com/jvde-github/AIS-catcher/media/media/SDRuno%20example.png)

The ZMQ interface is useful if a datastream from an SDR needs to be shared and processed by multiple decoders or for experimentation with different decoder models with support from GNU Radio.

Note that with [CSDR](https://github.com/ha7ilm/csdr) and [SoX](https://sox.sourceforge.net/) we can also decode this file as follows:
```bash
sox SDRuno_20200907_184926Z_161985kHz.wav -t raw -b 32 -e floating-point - |csdr shift_math_cc 0.165 | AIS-catcher  -r cf32 . -s 62500 -c X -v
```




## Input from FM discriminator
We can run AIS-catcher on a RAW audio file as in this [tutorial](https://github.com/freerange/ais-on-sdr/wiki/Testing-GNU-AIS):
```bash
wget "https://github.com/freerange/ais-on-sdr/wiki/example-data/helsinki-210-messages.raw"
AIS-catcher  -m 3 -v -s 48K -r cs16 helsinki-210-messages.raw
```
On this file we should extract roughly ``362`` AIVDM lines. Notice that with switch ```-m 3``` on the command line AIS-catcher runs a decoding model that assumes the input is the output of an FM discriminator. In this case, the program is similar to the following usage of GNUAIS:
```bash
gnuais -l helsinki-210-messages.raw
```
which produces:
```
INFO: A: Received correctly: 153 packets, wrong CRC: 49 packets, wrong size: 4 packets
INFO: B: Received correctly: 52 packets, wrong CRC: 65 packets, wrong size: 10 packets
```