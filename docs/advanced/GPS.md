# Specifying Station Location

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



