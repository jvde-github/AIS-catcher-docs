# Running on RPI Zero W and other devices with performance limitations

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