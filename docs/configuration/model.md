#  Decoding Models

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        [<span class="cmd-flag">-m</span><span class="cmd-value">model</span>]
        <span class="cmd-flag">-go</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

> There is typically no need to tweak the model settings but below is provided for the experimenters and the enthusiasts.

## Model Selection

The command line provides the `-m` option which selects the specific decoding model.  In the current version, 4 different receiver models are embedded for raw data samples:

- **Default Model** (``-m 2``): the default demodulation engine.
- **Base Model (non-coherent)** (``-m 1``): using FM discriminator model, similar to RTL-AIS (and GNUAIS/Aisdecoder) with tweaks to the Phase Locked Loop and main receiver filter (computed with a stochastic search algorithm).
- **Standard Model (non-coherent)** (``-m 0``): as the Base Model with brute force timing recovery.
- **FM Discriminator model**: (``-m `3`) as the Standard Model but with the input already assumed to be the output of an FM discriminator. Hence no FM demodulation takes place which allows ```AIS-catcher``` to be used as GNUAIS and AISdecoder.

The Default Model is the most time and memory consuming but experiments suggest it to be the most effective. In my home station, it improves message count by a factor 2 - 3. The reception quality of the Standard Model over the Base Model is more modest at the expense of roughly a 20% increase in computation time. Advice is to start with the Default Model, which should run fine on most modern hardware including a Raspberry 4B and then scale down to ```-m 0```or even ```-m 1```, if needed.

## Running multiple models 

Notice that you can execute multiple models for one input device for benchmarking purposes but only the messages from the first model specified are displayed on screen. To benchmark different models specify ```-b``` for timing and/or ```-v``` to compare message count, e.g.
```bash
AIS-catcher -s 1536K -r posterholt.raw -m 2 -m 0 -m 1 -q -b -v
```
The program will run and summarize the performance (count and timing) of three decoding models (on a Raspberry Pi 4B):
```
[AIS engine v0.35]:                      38 msgs at 6.3 msg/s
[Standard (non-coherent)]:               4 msgs at 0.7 msg/s
[Base (non-coherent)]:                   3 msgs at 0.5 msg/s
```
```
[AIS engine v0.35]:                      1036.54 ms
[Standard (non-coherent)]:               932.47 ms
[Base (non-coherent)]:                   859.065 ms
```
In this example the Default Model performs quite well in contrast to the Standard non-coherent engine with 38 messages identified versus 4 for the standard engine. 
This is typical when there are messages of poor quality. However, it increases the decoding time a bit and has a slightly higher memory usage so needs more powerful hardware. Please note that the improvements seen for this particular file are an exception.


## Other models
For completeness, the decoder for NMEA input as text is activated by `-m 5` and `-m `4` is an experimental implementation to test new ideas. In practice, the user will not require these settings.

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

The functionality to read NMEA lines from text files has been used to validate AIS-catcher JSON output on a [file](https://www.aishub.net/ais-dispatcher) with 80K+ lines against [pyais](https://pypi.org/project/pyais/) and [gpsdecode](https://gpsd.io/gpsdecode.html). Only available switches for this decoder are ``-go nmea_refresh`` and ``-go crc_check`` which force AIS-catcher to, respectively, recalculate the NMEA lines if ``on`` (default ``off``) and ignore messages with incorrect CRC if ``on`` (default ``off``). Example: 
```bash
echo '$AIVDM,1,1,,,3776k`5000a3SLPEKnDQQWpH0000,0*79' | AIS-catcher -r txt . -n -go nmea_refresh on crc_check off
```
returns a warning on the incorrect CRC and:
```
!AIVDM,1,1,,,3776k`5000a3SLPEKnDQQWpH0000,0*3A
```
Note that CRC/checksum is the simple xor-checksum for validating that the NMEA line is not corrupted and not the CRC that is transmitted with the AIS message for a decoder to check the correct reception over air. This latter 16-bit checksum/CRC is not included in the NMEA message.

AIS-catcher will also accept AIVDO input which is typically used for the MMSI of the own ship. You can enable/disable this with: `-go vdo on/off`.

## Model Settings

### Common Settings
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">droop</span> | boolean | <span class="cmd-value">true</span> | Enable droop compensation in CIC5 filters |
| <span class="cmd-setting">fp_ds</span> | boolean | <span class="cmd-value">false</span> | Enable fixed-point downsampling |
| <span class="cmd-setting">station_id</span> | integer | <span class="cmd-value">0</span> | Station identifier |
| <span class="cmd-setting">own_mmsi</span> | integer | <span class="cmd-value">-1</span> | Own vessel MMSI |

### Downsampling Options
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">soxr</span> | boolean | <span class="cmd-value">false</span> | Use SOXR resampler |
| <span class="cmd-setting">src</span> | boolean | <span class="cmd-value">false</span> | Use SRC resampler |
| <span class="cmd-setting">ma</span> | boolean | <span class="cmd-value">false</span> | Use moving average downsampling |

### NMEA Model Settings
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">nmea_refresh</span> | boolean | <span class="cmd-value">false</span> | Recalculate NMEA lines |
| <span class="cmd-setting">crc_check</span> | boolean | <span class="cmd-value">false</span> | Enable CRC validation |
| <span class="cmd-setting">vdo</span> | boolean | <span class="cmd-value">true</span> | Accept AIVDO messages |
| <span class="cmd-setting">stamp</span> | boolean | <span class="cmd-value">false</span> | Add timestamps |
| <span class="cmd-setting">gps</span> | boolean | <span class="cmd-value">false</span> | Enable GPS output |
| <span class="cmd-setting">uuid</span> | string | <span class="cmd-value">-</span> | Set UUID for messages |
| <span class="cmd-setting">warnings</span> | boolean | <span class="cmd-value">true</span> | Show warning messages |