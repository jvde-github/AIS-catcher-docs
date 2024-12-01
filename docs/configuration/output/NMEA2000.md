# NMEA2000 input and output via SocketCAN

In v0.56 we introduced "Experimenter Mode" for NMEA2000 input and output via socketCAN on Linux. To properly handle the mechanics of a NMEA2000 network, the NMEA2000 library by  Timo Lappalainen
is required, build AIS-catcher in the main directory with:
  ```
  ./scripts/build-NMEA2000.sh
  ```
  This downloads and builds the [NMEA2000 library](https://github.com/ttlappalainen/NMEA2000) and includes it in the AIS-catcher build process.
  The following example creates a UDP server listening on port 4002 and forwards these messages to the CAN-bus (`vcan0`):
  ```bash
  AIS-catcher -x 192.168.1.120 4002 -I vcan0  
  ```
  Current implementation handles AIS messages 1-5, 9, 11, 14, 18, 19, 21, 24 and have been very high-level tested with the excellent [CANboat](https://github.com/canboat/canboat) utilities and a virtual network.
  Another option is to have AIS-catcher read AIS messages on the NMEA2000 canbus:
  ```bash
  AIS-catcher -i vcan0
  ``` 
  Note that this only works on Linux with socketCAN support and has not been tested properly. Obviously, the program is not certified by NMEA and is not build for connecting it to a NMEA2000 network on a boat. It is for the experimenters wanting to learn and play with networks and AIS.

  ## Summary Settings Input

  | Setting | Type | Default | Description |
|---------|------|---------|-------------|
| INTERFACE | string | "can0" | CAN bus interface name |

## Summary Settings Output

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| NETWORK | string | "" | CAN network interface name |
  
