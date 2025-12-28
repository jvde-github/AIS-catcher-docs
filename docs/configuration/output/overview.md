# Output Configuration

AIS-catcher has multiple output options. As for the input, they share a few common settings to manage the flow of messages to output connections and for filtring.

Note on casing:

- JSON configuration keys are case-sensitive and should be lowercase.
- Command line setting names are not case-sensitive, but this documentation shows them in lowercase to match JSON.


## Message Filtering

For detailed information about filtering options, see the [Filtering](message-filtering.md) page. Filtering allows you to control which messages are included in the output based on type, channel, MMSI, and other criteria.

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

