# FAQ

## How to Connect to OpenCPN?

In this example, we have AIS-catcher running on a Raspberry PI and aim to receive the messages in OpenCPN running on a Windows computer with IP address ``192.168.1.239``. We have chosen to use port ``10101``. On the Raspberry, we start AIS-catcher with the following command to send the NMEA messages to the Windows machine:
```bash
 AIS-catcher -u 192.168.1.239 10101
```
 
In OpenCPN the only thing we need to do is create a Connection with the following settings:

<p align="center">
<img src="https://raw.githubusercontent.com/jvde-github/AIS-catcher/eb6ac606933f1793ad04f56fa58c92ae49171f0c/media/OpenCPN%20settings.jpg" width=40% height=40%>
</p>

> In newer versions of OpenCPN, the user has to specify a protocol, in this case select NMEA0183.