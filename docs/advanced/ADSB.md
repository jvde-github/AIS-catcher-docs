# Visializing ADSB plane in web viewer

AIS-catcher can connect to a ADSB feed over TCP. The plane feed will then be visualized in the WebViewer. To input formats are supported, Beast, e.g,
```bash
AIS-catcher -t beast localhost 30003 -N 8100
```

and BaseStation format:

```bash
AIS-catcher -t basestation localhost 30002 -N 81000
```