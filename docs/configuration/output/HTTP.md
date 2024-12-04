
# HTTP

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-H</span>
        <span class="cmd-value">url</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>


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

## Summary Settimgs

| Key | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">URL</span> | string | <span class="cmd-value">-</span> | Target HTTP endpoint URL |
| <span class="cmd-setting">USERPWD</span> | string | <span class="cmd-value">-</span> | Authentication credentials |
| <span class="cmd-setting">STATIONID</span> | string | <span class="cmd-value">-</span> | Station identifier |
| <span class="cmd-setting">INTERVAL</span> | integer | <span class="cmd-value">60</span> | Post interval in seconds (1-86400) |
| <span class="cmd-setting">TIMEOUT</span> | integer | <span class="cmd-value">10</span> | Connection timeout in seconds (1-30) |
| <span class="cmd-setting">GZIP</span> | boolean | <span class="cmd-value">false</span> | Enable GZIP compression |
| <span class="cmd-setting">RESPONSE</span> | boolean | <span class="cmd-value">true</span> | Show response messages |
| <span class="cmd-setting">PROTOCOL</span> | string | <span class="cmd-value">AISCATCHER</span> | Protocol type (AISCATCHER/MINIMAL/AIRFRAMES/LIST/APRS) |
| <span class="cmd-setting">LAT</span> | float | <span class="cmd-value">0.0</span> | Station latitude |
| <span class="cmd-setting">LON</span> | float | <span class="cmd-value">0.0</span> | Station longitude |
| <span class="cmd-setting">DEVICE_SETTING</span> | string | <span class="cmd-value">N/A</span> | Device settings |

Note: filter and routing options can be set as per [generic output settings](overview.md)