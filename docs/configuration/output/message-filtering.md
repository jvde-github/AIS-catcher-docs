# Message filtering

AIS-catcher has functionality to filter UDP, webviewer, TCP, MQTT, HTTP and screen output on message type, e.g. send only messages of type 1, 2, 3, 5, 18, 19, 24 and 27 over UDP:

```bash
AIS-catcher -u 127.0.0.1 10110 filter on allow_type 1,2,3,5,18,19,24,27
```
or remove message type 6 and 8:
```bash
AIS-catcher -u 127.0.0.1 10110 filter on block_type 6,8
```
Do not use spaces in the comma-separated message type list as it confuses the command line. Filtering will only take effect with the filter switched to ``ON`` (default ``OFF``) and the filter needs to be defined per ``-u`` switch (or ``-H`` and ``-o``).

In my home station, I am using this to control the size of the log file but still capture messages for inspection later. I am running with the command line parameter:
```bash
AIS-catcher -o 5 filter on block_type 1,2,3,4,5,9,18,19,21,24
```
Message type 8 is region-specific. If you encounter any messages in the wild that might be interesting for AIS-catcher to parse, please share in the Issue section and we can see if it is worthwhile to extend the JSON generator. 

## Message Downsampling

AIS-catcher provides several options to reduce the number of output messages by filtering or downsampling repeated or redundant data. This helps to minimize bandwidth, storage, or processing requirements, especially in high-traffic environments. The main downsampling options are:

### Removing duplicates: `unique` 

The `unique` or `unique_interval` option ensures that only unique messages are output within a specified time window. If a message with the same content (hash) is received multiple times within the interval, only the first is output, and duplicates are suppressed. This is useful for reducing repeated identical messages from the same source.

### Downsampling VDO messages: `own_interval`

The `own_interval` option controls the minimum interval (in seconds) between outputting messages from the receiver's own station (VDO messages). If multiple own-station messages are received within this interval, only the first is output. This is useful for reducing the frequency of self-reported position or status updates which can be quite frequent for certain devices.

### Downsampling position messages: `position_interval`

The `position_interval` option sets the minimum interval (in seconds) between outputting position reports (types 1, 2, 3, 18, and 27) for each MMSI. If multiple position messages for the same vessel are received within this interval, only the first is output. This helps to limit the rate of position updates for each vessel which are typically the most frequent messages.

These options can be combined to fine-tune the output rate and avoid redundant data, depending on your use case and requirements.

**Note**: filtering for messages to screen can only be set on the command line and not in the JSON configuration file at this stage. UDP filtering is available in the JSON configuration file.

### Filter settings

<div class="settings-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">filter</span> | boolean | <span class="cmd-value">false</span> | Enable/disable filtering |
| <span class="cmd-setting">allow_type</span> | list | <span class="cmd-value">all</span> | Comma-separated list of message types to allow (1-27) |
| <span class="cmd-setting">block_type</span> | list | <span class="cmd-value">none</span> | Comma-separated list of message types to block |
| <span class="cmd-setting">allow_repeat</span> | list | <span class="cmd-value">all</span> | Allow messages with specific repeat counter values (0-3) |
| <span class="cmd-setting">block_repeat</span> | list | <span class="cmd-value">none</span> | Block messages with specific repeat counter values |
| <span class="cmd-setting">allow_mmsi</span> | list | <span class="cmd-value">all</span> | Only allow messages from specific MMSI numbers |
| <span class="cmd-setting">block_mmsi</span> | list | <span class="cmd-value">none</span> | Block messages from specific MMSI numbers |
| <span class="cmd-setting">allow_channel</span> | string | <span class="cmd-value">all</span> | Only allow messages from specific AIS channels |
| <span class="cmd-setting">id</span> | integer | <span class="cmd-value">all</span> | Only allow messages from specific station IDs |
| <span class="cmd-setting">gps</span> | boolean | <span class="cmd-value">true</span> | Include GPS messages in output |
| <span class="cmd-setting">ais</span> | boolean | <span class="cmd-value">true</span> | Include AIS messages in output |
| <span class="cmd-setting">unique</span> | boolean | <span class="cmd-value">false</span> | Only send/show unique messages|
| <span class="cmd-setting">position_interval</span> | number | <span class="cmd-value">false</span> | Minimal time in seconds between position updates for a ship, off = false or 0 |
| <span class="cmd-setting">own_interval</span> | number | <span class="cmd-value">false</span> | Minimal time in seconds between  updates for own ship, off = false or 0 |
</div>