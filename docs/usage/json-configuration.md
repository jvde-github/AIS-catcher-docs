# Configuration (JSON)

As per version 0.41, AIS-catcher can be mostly configured via a configuration file in JSON format,
```console
AIS-catcher -C config.json
```
where `config.json` is the name of the configuration file. The idea behind this feature is to simplify the setup of feeding multiple online sources. The minimal configuration file should have the following:
```json
{ "config": "aiscatcher", "version": 1 }
```
A fuller example config file looks as follows:
```json
{
    "config": "aiscatcher",
    "version": "1",
    "input": "serialport",
    "verbose": true,
    "sharing": true,
    "sharing_key": "6ef40ea8-59b9-11ef-8db4",
    "screen": 0,
    "serialport": {
        "baudrate": 38400,
        "port": "/dev/tty0"
    },
    "rtlsdr": {
        "active": true,
        "rtlagc": true,
        "tuner": "auto",
        "bandwidth": "192K",
        "sample_rate": "1536K",
        "biastee": false,
        "buffer_count": 2
    },
    "airspy": {
        "sample_rate": "3000K",
        "linearity": 17,
        "biastee": false
    },
    "airspyhf": {
        "sample_rate": "192k",
        "threshold": "low",
        "preamp": false
    },
    "hackrf": {
        "sample_rate": "6144k",
        "lna": 8,
        "vga": 20,
        "preamp": false
    },
    "sdrplay": {
        "sample_rate": "2304K",
        "agc": true,
        "lnastate": 5,
        "grdb": 40
    },
    "udpserver": {
        "server": "192.168.1.235",
        "port": 4002
    },
    "server": {
        "file": "stat.bin",
        "backup": 10,
        "realtime": true,
        "active": true,
        "port": 8100,
        "station": "My Station",
        "station_link": "http://example.com/",
        "share_loc": true,
        "lat": 52,
        "lon": 4.3,
        "plugin_dir": "/home/jasper/AIS-catcher/plugins/",
        "cdn": "/home/jasper/webassets",
        "prome": true,
        "context": "settings"
    },
    "tcp": [
        {
            "active": true,
            "host": "5.9.207.224",
            "port": 12,
            "keep_alive": false
        }
    ],
    "udp": [
        {
            "host": "ais.fleetmon.com",
            "port": 0
        },
        {
            "active": true,
            "host": "hub.shipxplorer.com",
            "port": 0,
            "filter": false,
            "allow_type": "1,2,3,5,18,19,24"
        }
    ],
    "tcp_listener": [
        {
            "port": 5012
        }
    ],
    "http": [
        {
            "url": "https://ais.chaos-consulting.de/shipin/index.php",
            "userpwd": "user:pwd",
            "interval": 30,
            "gzip": false,
            "response": false,
            "filter": false
        },
        {
            "url": "http://aprs.fi/jsonais/post/secret_key",
            "id": "myid",
            "interval": 60,
            "protocol": "aprs",
            "response": false
        }
    ]
}
```

The UDP and HTTP outward connections are included as a JSON array (surrounded by `[` and `]`) with an  "object" for each separate channel. In each object we can include the 
boolean field ``active`` (see the second UDP definition) which will cause the program to ignore the settings if set to `false` providing an easy way to switch particular channels or dongle configurations on and off. 

The fields and values in the configuration file can be specified consistent with the command line settings as described 
in this document. JSON is however case sensitive so field names must be entered in lower case.

The active device is selected via the ``input`` or ``serial`` field. Sections for specific SDRs like `rtlsdr` specify the settings of the device only and **do not** automatically select it. Therefore, we can specify settings for many devices even if not connected. This will not have an impact.

If both `input` and `serial` are included in the configuration file to select a device for decoding, the program will check that they are consistent, i.e. the hardware with the specified serial number must be of type ``input``. 
If you want to run multiple receivers simultaneously, this is possible as well but the device-specific settings and selection need to be included in an array ``receiver``:
```json
{
  "config":"aiscatcher",
  "version":1,
  "receiver":[
    {
      "input":"airspy",
      "verbose":true,
      "airspy":{
        "sample_rate":"3000K"
      }
    },
    {
      "input":"rtlsdr",
      "serial":"ais",
      "verbose":true,
      "rtlsdr":{
        "bandwidth":"192k"
      }
    }
  ]
}
```
If there is only one RTL-SDR connected, only `input` set to `rtlsdr` is sufficient. Similarly, if there is only one device connected with serial `ais`, we only have to specify `serial`. 