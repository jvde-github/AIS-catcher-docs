# Writing AIS messages to a Postgres Database

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-D</span>
        <span class="cmd-value">url</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>


As per full release `v0.45`, there is functionality to write messages to a database (PostgreSQL). The setup is fairly flexible and can be tailored to the particular needs. First create an empty PostgreSQL database, e.g on an Ubuntu distribution (this might be different on your system):
```bash
sudo -u postgres createdb ais
```
Set up the necessary tables from the AIS-catcher directory:
```bash
psql ais <DBMS/create.sql 
```
Make sure you build the latest version of AIS-catcher with this dependency:
```bash
sudo apt install libpq-dev
```
Now AIS-catcher can write the received messages to the database:
```bash
AIS-catcher -D dbname=ais STATION_ID 17
```
or when more details, like username and password, are required:
```bash
AIS-catcher -D postgresql://[user[:password]@][netloc][:port][/dbname]
```
The `STATION_ID` setting is optional but will populate the entries in the database with the specified ID so multiple feeders can write to one database.
There are a few settings for the new `-D` switch of which the first is the connection string that specifies the database. If you want to use a space in the string use quotation marks around the string. There are other settings that define how tables will be populated:

| Table | Description | Settings | Default |
| :--- | :--- | :--- | :--- |
| ais_vessel | last received data per MMSI | V on/off | **on**  |
| ais_message | received messages with meta data  | MSGS on/off | off  |
| ais_nmea | nmea sentences | NMEA on/off | off |
| ais_basestation | basestation messsages from type 4 | BS on/off | off |
| ais_sar_position | sar positions from type 9 | SAR on/off | off |
| ais_aton | aton messages from type 21 | ATON on/off | off |
| ais_vessel_pos | vessel position messages from type 1-3, 18, 19, 27 | VP on/off | off |
| ais_vessel_static | vessel static data from type 5, 19 | VS on/off | off |
| ais_property | specific key/value pairs with link to message  | fill with keys specified in the table ais_keys | empty |

From hereon it is fairly straightforward to pick up this data and start analysis. If the connection fails during the decoding, for whatever reason, the program will try to reconnect to the database every 2 seconds. The maximum number of failed connection attempts before the program terminates is set with `MAX_FAILS` (<1000) and is set on the command line. If `MAX_FAILS` is 1000 the program will not terminate if the connection fails.  

I hope this is sufficient to get you experimenting! Unfortunately, the options cannot yet be set from the JSON configuration file which is work in progress.

## Summary Settings

<div class="input-table" markdown>
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">CONN_STR</span> | string | <span class="cmd-value">dbname=ais</span> | PostgreSQL connection string |
| <span class="cmd-setting">STATION_ID</span> | integer | <span class="cmd-value">0</span> | Station identifier |
| <span class="cmd-setting">INTERVAL</span> | integer | <span class="cmd-value">10</span> | Database write interval (5-1800 sec) |
| <span class="cmd-setting">MAX_FAILS</span> | integer | <span class="cmd-value">10</span> | Max failed connection attempts |
| | | | |
| Table Options | | | |
| <span class="cmd-setting">V</span> | boolean | <span class="cmd-value">true</span> | Enable vessel table logging |
| <span class="cmd-setting">MSGS</span> | boolean | <span class="cmd-value">false</span> | Enable message table logging |
| <span class="cmd-setting">NMEA</span> | boolean | <span class="cmd-value">false</span> | Enable NMEA sentence logging |
| <span class="cmd-setting">BS</span> | boolean | <span class="cmd-value">false</span> | Enable basestation logging |
| <span class="cmd-setting">SAR</span> | boolean | <span class="cmd-value">false</span> | Enable SAR position logging |
| <span class="cmd-setting">ATON</span> | boolean | <span class="cmd-value">false</span> | Enable AtoN logging |
| <span class="cmd-setting">VP</span> | boolean | <span class="cmd-value">false</span> | Enable vessel position logging |
| <span class="cmd-setting">VS</span> | boolean | <span class="cmd-value">false</span> | Enable vessel static data logging |
</div>