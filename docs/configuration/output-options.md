# Output Configuration

## Console

The output of NMEA messages to screen can be regulated with the ``-o`` switch. To suppress any messages to screen use ``-o 0`` or ``-q``. This can be useful if you run AIS-catcher as a background process. To show only simple and pure NMEA lines, use the switch ``-o 1`` or ``-n``. Example output:
```
!AIVDM,1,1,,B,33L=LN051HQj3HhRJd7q1W=`0000,0*03
```
By default, and using the command ``-o 2``, AIS-catcher displays NMEA messages with some additional information:
```
!AIVDM,1,1,,B,33L=LN051HQj3HhRJd7q1W=`0000,0*03 ( MSG: 3, REPEAT: 0, MMSI: 230907000, signalpower: -44.0, ppm: 0, timestamp: 20220729191340)
```
This same information but wrapped in JSON to facilitate further processing downstream is generated with the switch ```-o 3``` :
```json
{"class":"AIS","device":"AIS-catcher","channel":"B","rxtime":"20220729191502","signalpower":-44.0,"ppm":0,"mmsi":230907000,"type":3,"nmea":["!AIVDM,1,1,,B,33L=LN051HQj3HhRJd7q1W=`0000,0*03"]}
```
And finally, full decoding of the AIS message is activated via ``-o 5``:
```json
{"class":"AIS","device":"AIS-catcher","rxtime":"20220729191610","scaled":true,"channel":"B","nmea":["!AIVDM,1,1,,B,33L=LN051HQj3HhRJd7q1W=`0000,0*03"],"signalpower":-44.0,"ppm":0.000000,"type":3,"repeat":0,"mmsi":230907000,"status":0,"status_text":"Under way using engine","turn":18,"speed":8.800000,"accuracy":true,"lon":24.915239,"lat":60.148106,"course":231.000000,"heading":230,"second":52,"maneuver":0,"raim":false,"radio":0}
```

Meta data is not calculated by default to keep the program as light as possible when running as a server on low spec devices but can be activated with the ```-M``` switch. The calculation of signal power (in dB) and applied frequency correction (in ppm) are activated with  ``-M D``. NMEA messages are timestamped with  ``-M T`` and additional country information from the station derived from the MMSI is included in JSON output with ``-M M``. 

There are many libraries for decoding AIS messages in NMEA format to JSON format. I encourage you to use your favorite library. Some excellent choices include [libais](https://github.com/schwehr/libais), [gpsdecode](https://github.com/ukyg9e5r6k7gubiekd6/gpsd/blob/master/gpsdecode.c) and [pyais](https://github.com/M0r13n/pyais).

## HTTP

Some cloud services collecting AIS data prefer messages to be periodically posted via the HTTP protocol, for example, [APRS.fi](https://aprs.fi). As per version 0.29, AIS-catcher can do this directly via the ``-H`` switch. For example:
```console
AIS-catcher -r posterholt.raw -v 60 -H http://localhost:8000 INTERVAL 10 ID MyStation
```
will post JSON with the following layout every 10 seconds:

```json
{
	"protocol": "jsonaiscatcher",
	"encodetime": "20221102171325",
	"stationid": "MyStation",
	"receiver":
		{
		"description": "AIS-catcher v0.39",
		"version": 39,
		"engine": "Base (non-coherent)",
		"setting": "droop ON fp_ds OFF "
		},
	"device":
		{
		"product": "FILE-RAW",
		"vendor": "",
		"serial": "",
		"setting": "rate 1536K file posterholt.raw format CU8"
		},
	"msgs": [ 
		{"class":"AIS","device":"AIS-catcher","rxtime":"20221102171324","scaled":true,"channel":"A","nmea":["!AIVDM,1,1,,A,13`fL1PP140KCELMBO7SS?wH0@Jv,0*50"],"ppm":0.000000,"type":1,"mmsi":244030470,"status":0,"status_text":"Under way using engine","speed":6.800000,"accuracy":false,"lon":5.964237,"lat":51.185970,"course":90.800003,"repeat":0,"second":44,"maneuver":0,"raim":false,"radio":67262}
	]
}
```
We can use this functionality to submit data to [APRS.fi](https://aprs.fi) directly without the need of middleware:
```console
AIS-catcher -H http://aprs.fi/jsonais/post/secret-key ID callsign PROTOCOL aprs INTERVAL 30 -q
```
Where ``secret-key`` should be your password and ``callsign`` your callsign.  The ``PROTOCOL`` setting instructs AIS-catcher to submit JSON in a form that is accepted by APRS.fi which is a multi-form HTTP message. The response from the server will be printed on screen, if you want to show this message only in case of an error, add `RESPONSE OFF` to the argument.

Another example of this HTTP feed functionality is to provide data to [Chaos Consulting](https://adsb.chaos-consulting.de/map/) without the need to install any additional scripts. The Chaos Consulting server has been set up so that it can read the AIS-catcher JSON format as per above:
```console
AIS-catcher -H https://ais.chaos-consulting.de/shipin/index.php USERPWD Station:Password GZIP on INTERVAL 5
```
Notice that this server requires authentication with a station name and password and accepts JSON with gzip encoding which significantly reduces bandwidth. 

**Important**: to use and build AIS-catcher with HTTP support, please install the following libraries before running cmake:
```console
sudo apt install libssl-dev zlib1g-dev
```
This step is only required if you want to ZIP content and post data to secure servers.

The supported protocol switches are ``AISCATCHER`` (default), ``MINIMAL`` (NMEA lines and metadata), ``LINES`` (one JSON message per line), ``APRS`` (to submit to APRS.fi).

### Summary Settimgs

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| URL | string | empty | Target HTTP endpoint URL |
| USERPWD | string | empty | Authentication credentials |
| STATIONID/ID/CALLSIGN | string | empty | Station identifier |
| INTERVAL | integer | 60 | Post interval in seconds (1-86400) |
| TIMEOUT | integer | 10 | Connection timeout in seconds (1-30) |
| GZIP | boolean | false | Enable GZIP compression |
| RESPONSE | boolean | true | Show response messages |
| PROTOCOL | enum | "AISCATCHER" | Protocol type ("AISCATCHER", "MINIMAL", "AIRFRAMES", "LIST", "APRS") |
| LAT | float | 0.0 | Station latitude |
| LON | float | 0.0 | Station longitude |
| DEVICE_SETTING | string | "N/A" | Device settings |
| GROUPS_IN | integer | - | Number of input groups |

## UDP 

AIS messages can be forwarded between applications over UDP via the `-u` switch and as a TCP Client using `-P`. To send data to a port at a specific server, we can use:
```bash
AIS-catcher -u 192.168.1.235 4002
```
The command accepts additonal parameters, e.g. to send NMEA messages packaged in a JSON object:
```bash
AIS-catcher -u 192.168.1.235 4002 JSON on
```
Most external programs will not be able to accept these JSON-packaged NMEA strings. It is a way to transfer received messages between AIS-catcher instances without losing metadata like the timestamp, ppm correction and signal level. These are not captured in the standard NMEA strings. 
Another option for UDP sending via `-u` is `BROADCAST on/off` to enable sending to broadcast addresses.


### Summary Settimgs

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| HOST | string | empty | Target UDP host address |
| PORT | string | empty | Target UDP port |
| JSON | boolean | false | Enable JSON output format |
| BROADCAST | boolean | false | Enable broadcast mode |
| RESET | integer | -1 | Socket reset interval in minutes (1-1440) |
| UUID | string | empty | Unique identifier (must be valid UUID) |
| GROUPS_IN | integer | - | Number of input groups |

## TCP Client

To send raw NMEA as a TCP Client connecting to a listener:
```bash
AIS-catcher -P 192.168.1.235 4002
```
In this case, AIS-catcher acts as a TCP client and connects to the remote listener at 192.168.1.239 port 4002. 

### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| HOST | string | empty | Target TCP server host |
| PORT | string | empty | Target TCP server port |
| KEEP_ALIVE | boolean | false | Enable TCP keep-alive |
| JSON | boolean | false | Enable JSON output format |
| PERSIST | boolean | true | Enable persistent connection |
| UUID | string | empty | Unique identifier (must be valid UUID) |
| GROUPS_IN | integer | - | Number of input groups |

## TCP Server


You can also set up AIS-catcher as a TCP listener itself for sending NMEA messages, i.e. the program acts as a TCP server where at most 64 clients can connect to and read NMEA lines:
```bash
AIS-catcher -S 5011
```

### Summary Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| PORT | integer | 5010 | Listen port (0-65535) |
| TIMEOUT | integer | - | Connection timeout |
| JSON | boolean | false | Enable JSON output format |
| GROUPS_IN | integer | - | Number of input groups |



## Filtering Messages

AIS-catcher has functionality to filter UDP, HTTP and screen output on message type, e.g. send only messages of type 1, 2, 3, 5, 18, 19, 24 and 27 over UDP:
```bash
AIS-catcher -u 127.0.0.1 10110 FILTER on ALLOW_TYPE 1,2,3,5,18,19,24,27
```
or remove message type 6 and 8:
```bash
AIS-catcher -u 127.0.0.1 10110 FILTER on BLOCK_TYPE 6,8
```
Do not use spaces in the comma-separated message type list as it confuses the command line. Filtering will only take effect with the filter switched to ``ON`` (default ``OFF``) and the filter needs to be defined per ``-u`` switch (or ``-H`` and ``-o``).

In my home station, I am using this to control the size of the log file but still capture messages for inspection later. I am running with the command line parameter:
```bash
AIS-catcher -o 5 filter on block_type 1,2,3,4,5,9,18,19,21,24
```
Message type 8 is region-specific. If you encounter any messages in the wild that might be interesting for AIS-catcher to parse, please share in the Issue section and we can see if it is worthwhile to extend the JSON generator. 

**Note**: filtering for messages to screen can only be set on the command line and not in the JSON configuration file at this stage. UDP filtering is available in the JSON configuration file.