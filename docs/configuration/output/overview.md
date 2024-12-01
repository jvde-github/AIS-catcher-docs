# Output Configuration

AIS-catcher offers multiple output options to suit different use cases. Below is an overview of the available output methods:

## Screen Output
- [Console Output](console.md): Display AIS messages directly in your terminal with customizable formats

## Network Output Options
- [TCP Server](TCP-server.md): Run an AIS server that clients can connect to
- [TCP Client](TCP-client.md): Connect to remote AIS servers
- [UDP](UDP.md): Send AIS messages via UDP to specified destinations
- [HTTP](HTTP.md): Provide AIS data through HTTP endpoints

## Integration Options
- [Community Feed](community-feed.md): Share your AIS data with the community
- [PostgreSQL](PSQL.md): Write AIS messages to Postgres database
- [Web Viewer](web-viewer.md): Built-in web interface for visualizing vessel traffic
- [MQTT](MQTT.md): Publish AIS data to MQTT brokers
- [NMEA2000](NMEA2000.md): Interface with NMEA2000 networks

## Message Filtering

Learn how to filter AIS messages by type for various outputs. [Read more about filtering](#filtering-messages)


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