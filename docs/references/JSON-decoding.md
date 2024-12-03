# Complete AIS Message JSON Documentation

## JSON Format
Below documents the JSON format used for decoding AIS messages. Depending on the settings for JSON decoding fields may or may not be included in the outcome.
With format `JSON_NMEA` only the common fields will be included in the JSON package. The AIS message details are still included in the NMEA array embedded in the JSON. With format `JSON_FULL` the program will perform a full decoding of the AIS messages and include in the JSON. The output format is largely compatible with `gpsdecode`.

### Common Fields
These fields are present in all AIS messages:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| class | String | Always "AIS" | "AIS" |
| device | String | Always "AIS-catcher" | "AIS-catcher" |
| type | Integer | Message type number | 1 |
| scaled | Boolean | Values scaled to real units | true |
| channel | String | AIS channel | "A" |
| nmea | String | Original NMEA sentence | "!AIVDM,1,1,,A,13..." |
| mmsi | Integer | MMSI number | 123456789 |

Optional configuration-dependent fields:

| Field | Type | Description |
|-------|------|-------------|
| version | String | Software version |
| driver | Integer | Driver identifier |
| hardware | String | Hardware identifier |
| signal_power | Float | Signal strength in dB |
| ppm | Float | Frequency error in ppm |
| rxtime | String | Reception timestamp |
| country | String | Country name from MMSI |
| country_code | String | Two-letter country code |


### Type 1, 2, 3: Position Report Class A

| Field | Type | Range/Units | Description |
|-------|------|-------------|-------------|
| status | Integer | 0-15 | Navigation status |
| status_text | String | See note 1 | Navigation status description |
| turn | Float | ±720°/min | Rate of turn |
| turn_unscaled | Integer | Raw | Unscaled turn value |
| speed | Float | 0-102.2 knots | Speed over ground |
| accuracy | Boolean | - | Position accuracy flag |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| course | Float | 0-359.9° | Course over ground |
| heading | Integer | 0-359° | True heading |
| second | Integer | 0-59 | Second of timestamp |
| maneuver | Integer | 0-2 | Maneuver indicator |
| raim | Boolean | - | RAIM flag |
| radio | Integer | - | Radio status |

### Type 4: Base Station Report

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| year | Integer | YYYY | UTC year |
| month | Integer | 1-12 | UTC month |
| day | Integer | 1-31 | UTC day |
| hour | Integer | 0-23 | UTC hour |
| minute | Integer | 0-59 | UTC minute |
| second | Integer | 0-59 | UTC second |
| accuracy | Boolean | - | Position accuracy flag |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| epfd | Integer | 0-8 | EPFD type |
| epfd_text | String | See note 2 | EPFD description |
| raim | Boolean | - | RAIM flag |
| radio | Integer | - | Radio status |

### Type 5: Static and Voyage Related Data

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| ais_version | Integer | 0-3 | AIS version |
| imo | Integer | 1-999999999 | IMO number |
| callsign | String | 7 chars | Radio callsign |
| shipname | String | 20 chars | Vessel name |
| shiptype | Integer | 0-99 | Ship type code |
| shiptype_text | String | See note 3 | Ship type description |
| to_bow | Integer | 0-511m | Dimension to bow |
| to_stern | Integer | 0-511m | Dimension to stern |
| to_port | Integer | 0-63m | Dimension to port |
| to_starboard | Integer | 0-63m | Dimension to starboard |
| epfd | Integer | 0-8 | EPFD type |
| epfd_text | String | See note 2 | EPFD description |
| eta | String | ISO8601 | Estimated time of arrival |
| draught | Float | 0-25.5m | Draft in meters |
| destination | String | 20 chars | Destination port |
| dte | Boolean | - | Data terminal flag |

### Type 6: Binary Addressed Message

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| seqno | Integer | 0-3 | Sequence number |
| dest_mmsi | Integer | 9 digits | Destination MMSI |
| retransmit | Boolean | - | Retransmit flag |
| dac | Integer | - | Designated Area Code |
| fid | Integer | - | Function ID |
| data | String | - | Binary data |

### Type 7: Binary Acknowledge

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| mmsi1 | Integer | 9 digits | MMSI number 1 |
| mmsiseq1 | Integer | 0-3 | Sequence for MMSI 1 |
| mmsi2 | Integer | 9 digits | MMSI number 2 |
| mmsiseq2 | Integer | 0-3 | Sequence for MMSI 2 |
| mmsi3 | Integer | 9 digits | MMSI number 3 |
| mmsiseq3 | Integer | 0-3 | Sequence for MMSI 3 |
| mmsi4 | Integer | 9 digits | MMSI number 4 |
| mmsiseq4 | Integer | 0-3 | Sequence for MMSI 4 |

### Type 8: Binary Broadcast Message

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| dac | Integer | - | Designated Area Code |
| fid | Integer | - | Function ID |
| data | String | - | Binary data |

### Type 9: Standard SAR Aircraft Position Report

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| alt | Integer | 0-4095 | Altitude in meters |
| speed | Integer | 0-1023 | Speed over ground |
| accuracy | Boolean | - | Position accuracy |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| course | Float | 0-359.9° | Course over ground |
| second | Integer | 0-59 | UTC second |
| regional | Integer | - | Regional reserved |
| dte | Boolean | - | DTE flag |
| assigned | Boolean | - | Assigned mode flag |
| raim | Boolean | - | RAIM flag |
| radio | Integer | - | Radio status |

### Type 10: UTC/Date Inquiry

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| dest_mmsi | Integer | 9 digits | Destination MMSI |

### Type 11: UTC/Date Response
Same fields as Type 4

### Type 12: Addressed Safety Related Message

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| seqno | Integer | 0-3 | Sequence number |
| dest_mmsi | Integer | 9 digits | Destination MMSI |
| retransmit | Boolean | - | Retransmit flag |
| text | String | - | Safety related text |

### Type 13: Safety Related Acknowledge
Same fields as Type 7

### Type 14: Safety Related Broadcast Message

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| text | String | - | Safety related text |

### Type 15: Interrogation

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| mmsi1 | Integer | 9 digits | Interrogated MMSI 1 |
| type1_1 | Integer | 1-27 | First message type |
| offset1_1 | Integer | - | First slot offset |
| type1_2 | Integer | 1-27 | Second message type |
| offset1_2 | Integer | - | Second slot offset |
| mmsi2 | Integer | 9 digits | Interrogated MMSI 2 |
| type2_1 | Integer | 1-27 | First message type |
| offset2_1 | Integer | - | First slot offset |

### Type 16: Assignment Mode Command

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| mmsi1 | Integer | 9 digits | First MMSI |
| offset1 | Integer | - | First offset |
| increment1 | Integer | - | First increment |
| mmsi2 | Integer | 9 digits | Second MMSI |
| offset2 | Integer | - | Second offset |
| increment2 | Integer | - | Second increment |

### Type 17: DGNSS Binary Broadcast Message

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| data | String | - | DGNSS data |

### Type 18: Standard Class B CS Position Report

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| reserved | Integer | - | Reserved |
| speed | Float | 0-102.2 knots | Speed over ground |
| accuracy | Boolean | - | Position accuracy |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| course | Float | 0-359.9° | Course over ground |
| heading | Integer | 0-359° | True heading |
| second | Integer | 0-59 | UTC second |
| regional | Integer | - | Regional reserved |
| cs | Boolean | - | Carrier sense unit flag |
| display | Boolean | - | Display flag |
| dsc | Boolean | - | DSC flag |
| band | Boolean | - | Band flag |
| msg22 | Boolean | - | Message 22 flag |
| assigned | Boolean | - | Assigned mode flag |
| raim | Boolean | - | RAIM flag |
| radio | Integer | - | Radio status |

### Type 19: Extended Class B CS Position Report

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| reserved | Integer | - | Reserved |
| speed | Float | 0-102.2 knots | Speed over ground |
| accuracy | Boolean | - | Position accuracy |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| course | Float | 0-359.9° | Course over ground |
| heading | Integer | 0-359° | True heading |
| second | Integer | 0-59 | UTC second |
| regional | Integer | - | Regional reserved |
| shipname | String | 20 chars | Vessel name |
| shiptype | Integer | 0-99 | Ship type code |
| shiptype_text | String | See note 3 | Ship type description |
| to_bow | Integer | 0-511m | Dimension to bow |
| to_stern | Integer | 0-511m | Dimension to stern |
| to_port | Integer | 0-63m | Dimension to port |
| to_starboard | Integer | 0-63m | Dimension to starboard |
| epfd | Integer | 0-8 | EPFD type |
| epfd_text | String | See note 2 | EPFD description |
| raim | Boolean | - | RAIM flag |
| dte | Boolean | - | DTE flag |
| assigned | Boolean | - | Assigned mode flag |

### Type 20: Data Link Management

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| offset1 | Integer | - | Offset number 1 |
| number1 | Integer | - | Reserved slots 1 |
| timeout1 | Integer | - | Timeout 1 |
| increment1 | Integer | - | Increment 1 |
| offset2 | Integer | - | Offset number 2 |
| number2 | Integer | - | Reserved slots 2 |
| timeout2 | Integer | - | Timeout 2 |
| increment2 | Integer | - | Increment 2 |
| offset3 | Integer | - | Offset number 3 |
| number3 | Integer | - | Reserved slots 3 |
| timeout3 | Integer | - | Timeout 3 |
| increment3 | Integer | - | Increment 3 |
| offset4 | Integer | - | Offset number 4 |
| number4 | Integer | - | Reserved slots 4 |
| timeout4 | Integer | - | Timeout 4 |
| increment4 | Integer | - | Increment 4 |

### Type 21: Aid-to-Navigation Report

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| aid_type | Integer | 0-31 | Aid type |
| aid_type_text | String | See note 4 | Aid type description |
| name | String | 20 chars | Name of aid |
| accuracy | Boolean | - | Position accuracy |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| to_bow | Integer | 0-511m | Dimension to bow |
| to_stern | Integer | 0-511m | Dimension to stern |
| to_port | Integer | 0-63m | Dimension to port |
| to_starboard | Integer | 0-63m | Dimension to starboard |
| epfd | Integer | 0-8 | EPFD type |
| epfd_text | String | See note 2 | EPFD description |
| second | Integer | 0-59 | UTC second |
| off_position | Boolean | - | Off position indicator |
| regional | Integer | - | Regional reserved |
| raim | Boolean | - | RAIM flag |
| virtual_aid | Boolean | - | Virtual aid flag |
| assigned | Boolean | - | Assigned mode flag |

### Type 22: Channel Management

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| channel_a | Integer | - | Channel A number |
| channel_b | Integer | - | Channel B number |
| txrx | Integer | - | Tx/Rx mode |
| power | Boolean | - | Power level |
| addressed | Boolean | - | Addressed flag |
| band_a | Boolean | - | Channel A band |
| band_b | Boolean | - | Channel B band |
| zonesize | Integer | - | Zone size |
| If addressed = true: |
| dest1 | Integer | 9 digits | Destination MMSI 1 |
| dest2 | Integer | 9 digits | Destination MMSI 2 |
| If addressed = false: |
| ne_lon | Float | ±180° | NE longitude |
| ne_lat | Float | ±90° | NE latitude |
| sw_lon | Float | ±180° | SW longitude |
| sw_lat | Float | ±90° | SW latitude |

### Type 23: Group Assignment Command

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| ne_lon | Float | ±180° | NE longitude |
| ne_lat | Float | ±90° | NE latitude |
| sw_lon | Float | ±180° | SW longitude |
| sw_lat | Float | ±90° | SW latitude |
| station_type | Integer | - | Station type |
| ship_type | Integer | - | Ship type |
| txrx | Integer | - | Tx/Rx mode |
| interval | Integer | - | Reporting interval |
| quiet | Integer | - | Quiet time |

### Type 24: Static Data Report

Message Type 24 Part A Fields

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| partno | Integer | 0 | Part number, always 0 for Part A |
| shipname | String | 20 chars | Name of the vessel |

Message Type 24 Part B Fields

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| partno | Integer | 1 | Part number, always 1 for Part B |
| callsign | String | 7 chars | Vessel radio callsign |
| shiptype | Integer | 0-99 | Type of ship and cargo |
| shiptype_text | String | See note 1 | Description of ship type |
| vendorid | String | 3 chars | Manufacturer's ID |
| model | Integer | 0-15 | Equipment model code |
| serial | Integer | 0-999999 | Unit serial number |
| to_bow | Integer | 0-511 | Distance from GPS to bow in meters |
| to_stern | Integer | 0-511 | Distance from GPS to stern in meters |
| to_port | Integer | 0-63 | Distance from GPS to port in meters |
| to_starboard | Integer | 0-63 | Distance from GPS to starboard in meters |
| mothership_mmsi | Integer | 9 digits | MMSI of mothership for auxiliary craft |

### Message Type 25 Fields

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| addressed | Boolean | true/false | Message has specific destination |
| structured | Boolean | true/false | Message contains structured data |
| dest_mmsi | Integer | 9 digits | Destination MMSI if addressed |
| data | String | - | Binary payload data |

### Message Type 26 Fields

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| addressed | Boolean | true/false | Message has specific destination |
| structured | Boolean | true/false | Message contains structured data |
| dest_mmsi | Integer | 9 digits | Destination MMSI if addressed |
| radio | Integer | 0-3 | Radio status |
| data | String | - | Binary payload data |

### Message Type 27 Fields

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| accuracy | Boolean | true/false | Position accuracy: true if < 10m |
| raim | Boolean | true/false | RAIM flag: Receiver Autonomous Integrity Monitoring |
| status | Integer | 0-15 | Navigation status |
| status_text | String | See note 1 | Navigation status description |
| lon | Float | ±180° | Longitude in decimal degrees |
| lat | Float | ±90° | Latitude in decimal degrees |
| speed | Integer | 0-62 | Speed over ground in knots |
| course | Integer | 0-359 | Course over ground in degrees |
| gnss | Boolean | true/false | GNSS position status |

Notes

Navigation Status Values:

| Value | Description |
|-------|-------------|
| 0 | Under way using engine |
| 1 | At anchor |
| 2 | Not under command |
| 3 | Restricted manoeuverability |
| 4 | Constrained by draught |
| 5 | Moored |
| 6 | Aground |
| 7 | Engaged in fishing |
| 8 | Under way sailing |
| 9 | Reserved for HSC |
| 10 | Reserved for WIG |
| 11-13 | Reserved |
| 14 | AIS-SART is active |
| 15 | Not defined |
