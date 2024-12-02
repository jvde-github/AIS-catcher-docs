# Long Range AIS messages

AIS-catcher has the option to listen at frequency 156.8 Mhz to receive Channel 3/C and 4/D (vs the default A and B around 162 MHz) with the switch ```-c CD```. This follows ideas from a post on the [Shipplotter forum](https://groups.io/g/shipplotter/topic/ais_type_27_long_range/92150532?p=,,,20,0,0,0::recentpostdate/sticky,,,20,2,0,92150532,previd%3D1657138240979957244,nextid%3D1644163712453715490&previd=1657138240979957244&nextid=1644163712453715490). The default decoder is available with the switch ```-c AB```. Note that ``gpsdecode`` cannot handle channel designations C and D in NMEA lines. You can provide an optional argument to use channel designations A and B in the NMEA line with the command ```-c CD AB```.

In a similar fashion `-c X` will decode one channel. This is only useful in some instances, see the ZMQ example below.
