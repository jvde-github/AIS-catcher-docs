# Output Configuration

AIS-catcher has multiple output options. As for the input, they share a few common settings to manage the flow of messages to output connections and for filtring.


## Message Filtering

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
AIS-catcher -o 5 FILTER on BLOCK_TYPE 1,2,3,4,5,9,18,19,21,24
```
Message type 8 is region-specific. If you encounter any messages in the wild that might be interesting for AIS-catcher to parse, please share in the Issue section and we can see if it is worthwhile to extend the JSON generator. 

**Note**: filtering for messages to screen can only be set on the command line and not in the JSON configuration file at this stage. UDP filtering is available in the JSON configuration file.

### Filter settings

<div class="settings-table" markdown>
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">FILTER</span> | boolean | <span class="cmd-value">false</span> | Enable/disable filtering |
| <span class="cmd-setting">ALLOW_TYPE</span> | list | <span class="cmd-value">all</span> | Comma-separated list of message types to allow (1-27) |
| <span class="cmd-setting">BLOCK_TYPE</span> | list | <span class="cmd-value">none</span> | Comma-separated list of message types to block |
| <span class="cmd-setting">ALLOW_REPEAT</span> | list | <span class="cmd-value">all</span> | Allow messages with specific repeat counter values (0-3) |
| <span class="cmd-setting">BLOCK_REPEAT</span> | list | <span class="cmd-value">none</span> | Block messages with specific repeat counter values |
| <span class="cmd-setting">ALLOW_MMSI</span> | list | <span class="cmd-value">all</span> | Only allow messages from specific MMSI numbers |
| <span class="cmd-setting">BLOCK_MMSI</span> | list | <span class="cmd-value">none</span> | Block messages from specific MMSI numbers |
| <span class="cmd-setting">ALLOW_CHANNEL</span> | string | <span class="cmd-value">all</span> | Only allow messages from specific AIS channels |
| <span class="cmd-setting">ID</span> | integer | <span class="cmd-value">all</span> | Only allow messages from specific station IDs |
| <span class="cmd-setting">GPS</span> | boolean | <span class="cmd-value">true</span> | Include GPS messages in output |
| <span class="cmd-setting">AIS</span> | boolean | <span class="cmd-value">true</span> | Include AIS messages in output |
</div>

## Routing Messages

In principle, messages from all models sourced via all input connections is sourced to all Output Connections. Sometimes it is desirable to manage this flow.
This can be done via the Setting `GROUPS_IN` with as value the list of models that feed this input. 

## Output Options

AIS-catcher offers multiple output options to suit different use cases. Below is an overview of the available output methods:

### Screen Output
- [Console Output](console.md): Display AIS messages directly in your terminal with customizable formats

### Network Output Options
- [TCP Server](TCP-server.md): Run an AIS server that clients can connect to
- [TCP Client](TCP-client.md): Connect to remote AIS servers
- [UDP](UDP.md): Send AIS messages via UDP to specified destinations
- [HTTP](HTTP.md): Provide AIS data through HTTP endpoints

### Integration Options
- [Community Feed](community-feed.md): Share your AIS data with the community
- [PostgreSQL](PSQL.md): Write AIS messages to Postgres database
- [Web Viewer](web-viewer.md): Built-in web interface for visualizing vessel traffic
- [MQTT](MQTT.md): Publish AIS data to MQTT brokers
- [NMEA2000](NMEA2000.md): Interface with NMEA2000 networks

