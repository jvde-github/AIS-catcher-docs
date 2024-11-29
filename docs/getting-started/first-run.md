# First Run


To test that the installation was successful (see below for instructions), a good start is the following command which lists the devices available for AIS reception:
```bash
AIS-catcher -l
```
The output depends on the available devices but will look something like:
```bash
Found 1 device(s):
0: Realtek, RTL2838UHIDIR, SN: 00000001
```
A specific device can be selected with the ``d``-switch using the device number ``-d:0`` or the serial number ``-d 00000001``. If you were expecting  particular devices that are missing, you might want to try:
```bash
AIS-catcher -L
```
This lists all devices for which support is included in the executable. If particular hardware is not listed here, you might have to install the necessary libraries and rebuild AIS-catcher.

To start AIS decoding, print some occasional statistics (every 10 seconds)
```bash
AIS-catcher -v 10
```