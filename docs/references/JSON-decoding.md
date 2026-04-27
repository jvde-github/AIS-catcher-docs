# Complete AIS Message JSON Documentation

## JSON Format
Below documents the JSON format used for decoding AIS messages. Depending on the settings for JSON decoding fields may or may not be included in the outcome.
With format `JSON_NMEA` only the common fields will be included in the JSON package. The AIS message details are still included in the NMEA array embedded in the JSON. With format `JSON_FULL` the program will perform a full decoding of the AIS messages and include in the JSON. The output format is largely compatible with `gpsdecode`.

## Message types index

**Position reports**
[1, 2, 3 — Class A](#type-123) ·
[4 — Base Station](#type-4) ·
[9 — SAR Aircraft](#type-9) ·
[11 — UTC Response](#type-11) ·
[18 — Class B](#type-18) ·
[19 — Extended Class B](#type-19) ·
[27 — Long-Range](#type-27)

**Static / voyage**
[5 — Static and Voyage](#type-5) ·
[24 — Static Data Report](#type-24)

**Binary / safety / text**
[6 — Binary Addressed](#type-6) ·
[7, 13 — Binary / Safety Ack](#type-7) ·
[8 — Binary Broadcast](#type-8) ·
[12 — Safety Addressed](#type-12) ·
[14 — Safety Broadcast](#type-14) ·
[25, 26 — Single/Multi Slot Binary (not decoded)](#type-2526)

**Network management**
[10 — UTC Inquiry](#type-10) ·
[15 — Interrogation](#type-15) ·
[16 — Assignment Mode](#type-16) ·
[17 — DGNSS](#type-17) ·
[20 — Data Link Mgmt](#type-20) ·
[22 — Channel Mgmt](#type-22) ·
[23 — Group Assignment](#type-23)

**Aids to navigation**
[21 — Aid-to-Nav Report](#type-21)

**Other**
[Common fields](#common-fields) ·
[ASM payloads (Type 6 / 8)](#asm) ·
[Notes](#notes)

### Common Fields {#common-fields}
These fields are present in every emitted message:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| class | String | Always "AIS" | "AIS" |
| device | String | Always "AIS-catcher" | "AIS-catcher" |
| version | String | AIS-catcher version that produced this output | "v0.68" |
| driver | Integer | Numeric device driver identifier | 3 |
| hardware | String | Hardware/device product name reported by the driver | "RTL-SDR" |
| scaled | Boolean | Values scaled to engineering units | true |
| channel | String | VHF channel (A or B) | "A" |
| nmea | Array of String | Original NMEA sentence(s) | ["!AIVDM,1,1,,A,13...,0\*5C"] |
| type | Integer | AIS message type number (1–27) | 1 |
| repeat | Integer | Repeat indicator (0..3; 3 = do not repeat) | 0 |
| mmsi | Integer | MMSI number | 123456789 |

Optional fields, added depending on input mode and message contents:

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| rxtime | String | UTC | Host receive time (`YYYYMMDDHHMMSS`). Added when timestamping is enabled (`-M T`). |
| rxuxtime | Float | seconds | Host receive time as Unix epoch (with microsecond fraction). Added with `rxtime`. |
| signalpower | Float | dB | Signal power level. Added when stats are enabled (`-M D`). |
| ppm | Float | ppm | Estimated frequency offset of the receiver during decoding. Added with `signalpower`. |
| toa | Float | seconds | Time of arrival within the host capture (when provided by the source). |
| station_id | Integer or String | – | Station identifier (numeric, or 7-char ASCII for SLS). |
| error | Integer | – | Decode error code (only present when a decode error was flagged). |
| country | String | – | Flag country name derived from MMSI MID. Added with `-M M`. |
| country_code | String | – | ISO-3166 alpha-2 country code derived from MMSI MID. Added with `-M M`. |

### Type 1, 2, 3: Position Report Class A {#type-123}

| Field | Type | Range/Units | Description |
|-------|------|-------------|-------------|
| status | Integer | 0–15 | Navigation status |
| status_text | String | See note 1 | Navigation status description |
| turn | Integer | ±720 °/min | Rate of turn (scaled). 128 = N/A; ±127 = >5°/30s |
| turn_unscaled | Integer | -128..127 | Raw ROT field (-128 = N/A) |
| speed | Float | 0–102.2 knots | Speed over ground |
| accuracy | Boolean | – | Position accuracy flag (1 = DGPS <10 m) |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| course | Float | 0–359.9° | Course over ground |
| heading | Integer | 0–359° | True heading (511 = N/A) |
| second | Integer | 0–59 | UTC second (60 = N/A; 61 = manual; 62 = dead reckoning; 63 = inoperative) |
| maneuver | Integer | 0–2 | Maneuver indicator |
| spare | Integer | – | Spare/reserved bits |
| raim | Boolean | – | RAIM flag |
| radio | Integer | – | Radio status (19-bit SOTDMA/ITDMA state). When non-zero, sub-fields are also decoded — see note 5. |

### Type 4, 11: Base Station Report / UTC Date Response {#type-4}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| timestamp | String | ISO-8601 | UTC timestamp (`YYYY-MM-DDTHH:MM:SSZ`) |
| year | Integer | YYYY | UTC year |
| month | Integer | 1–12 | UTC month |
| day | Integer | 1–31 | UTC day |
| hour | Integer | 0–23 | UTC hour |
| minute | Integer | 0–59 | UTC minute |
| second | Integer | 0–59 | UTC second |
| accuracy | Boolean | – | Position accuracy flag |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| epfd | Integer | 0–8 | EPFD type |
| epfd_text | String | See note 2 | EPFD description |
| spare | Integer | – | Spare/reserved bits |
| raim | Boolean | – | RAIM flag |
| radio | Integer | – | Radio status. See note 5 for sub-fields. |

### Type 5: Static and Voyage Related Data {#type-5}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| ais_version | Integer | 0–3 | AIS version |
| imo | Integer | 1–999999999 | IMO number |
| callsign | String | 7 chars | Radio callsign |
| shipname | String | 20 chars | Vessel name |
| shiptype | Integer | 0–99 | Ship type code |
| shiptype_text | String | See note 3 | Ship type description |
| to_bow | Integer | 0–511 m | Dimension to bow |
| to_stern | Integer | 0–511 m | Dimension to stern |
| to_port | Integer | 0–63 m | Dimension to port |
| to_starboard | Integer | 0–63 m | Dimension to starboard |
| epfd | Integer | 0–8 | EPFD type |
| epfd_text | String | See note 2 | EPFD description |
| eta | String | `MM-DDTHH:MMZ` | Estimated time of arrival (UTC) |
| month | Integer | 1–12 | ETA month (also exposed individually) |
| day | Integer | 1–31 | ETA day |
| hour | Integer | 0–23 | ETA hour |
| minute | Integer | 0–59 | ETA minute |
| draught | Float | 0–25.5 m | Draught in metres |
| destination | String | 20 chars | Destination port |
| dte | Boolean | – | Data terminal equipment ready (0 = ready) |
| spare | Integer | – | Spare/reserved bit |

### Type 6: Binary Addressed Message {#type-6}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| seqno | Integer | 0–3 | Sequence number |
| dest_mmsi | Integer | 9 digits | Destination MMSI |
| retransmit | Boolean | – | Retransmit flag |
| spare | Integer | – | Spare bit |
| dac | Integer | – | Designated Area Code |
| fid | Integer | – | Functional Identifier |
| data | String | hex | Raw binary payload (only when no decoder matched) |

When the (DAC, FID) pair is recognised, the payload is decoded into structured fields instead of `data` — see [ASM payloads (Type 6 / Type 8)](#asm-payloads-type-6--type-8) below.

### Type 7, 13: Binary / Safety Acknowledge {#type-7}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| spare | Integer | – | Spare bits |
| mmsi1 | Integer | 9 digits | MMSI number 1 |
| mmsiseq1 | Integer | 0–3 | Sequence for MMSI 1 |
| mmsi2 | Integer | 9 digits | MMSI number 2 (if present) |
| mmsiseq2 | Integer | 0–3 | Sequence for MMSI 2 |
| mmsi3 | Integer | 9 digits | MMSI number 3 (if present) |
| mmsiseq3 | Integer | 0–3 | Sequence for MMSI 3 |
| mmsi4 | Integer | 9 digits | MMSI number 4 (if present) |
| mmsiseq4 | Integer | 0–3 | Sequence for MMSI 4 |

### Type 8: Binary Broadcast Message {#type-8}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| dac | Integer | – | Designated Area Code |
| fid | Integer | – | Functional Identifier |
| data | String | hex | Raw binary payload (only when no decoder matched) |

When the (DAC, FID) pair is recognised, the payload is decoded into structured fields — see [ASM payloads (Type 6 / Type 8)](#asm-payloads-type-6--type-8) below.

### Type 9: Standard SAR Aircraft Position Report {#type-9}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| alt | Integer | 0–4095 m | Altitude (4095 = N/A) |
| speed | Integer | 0–1023 knots | Speed over ground |
| accuracy | Boolean | – | Position accuracy |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| course | Float | 0–359.9° | Course over ground |
| second | Integer | 0–59 | UTC second |
| regional | Integer | – | Regional reserved |
| dte | Boolean | – | DTE flag |
| assigned | Boolean | – | Assigned mode flag |
| raim | Boolean | – | RAIM flag |
| radio | Integer | – | Radio status. See note 5 for sub-fields. |

### Type 10: UTC/Date Inquiry {#type-10}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| dest_mmsi | Integer | 9 digits | Destination MMSI |

### Type 11: UTC/Date Response {#type-11}
Same fields as [Type 4](#type-4).

### Type 12: Addressed Safety Related Message {#type-12}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| seqno | Integer | 0–3 | Sequence number |
| dest_mmsi | Integer | 9 digits | Destination MMSI |
| retransmit | Boolean | – | Retransmit flag |
| text | String | – | Safety related text |

### Type 13: Safety Related Acknowledge {#type-13}
Same fields as [Type 7](#type-7).

### Type 14: Safety Related Broadcast Message {#type-14}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| text | String | – | Safety related text |

### Type 15: Interrogation {#type-15}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| mmsi1 | Integer | 9 digits | Interrogated MMSI 1 |
| type1_1 | Integer | 1–27 | First message type requested from station 1 |
| offset1_1 | Integer | – | Reply slot offset for first request |
| type1_2 | Integer | 1–27 | Second message type requested from station 1 (if present) |
| offset1_2 | Integer | – | Reply slot offset for second request |
| mmsi2 | Integer | 9 digits | Interrogated MMSI 2 (if present) |
| type2_1 | Integer | 1–27 | First message type requested from station 2 |
| offset2_1 | Integer | – | Reply slot offset for first request |

### Type 16: Assignment Mode Command {#type-16}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| mmsi1 | Integer | 9 digits | First MMSI |
| offset1 | Integer | – | First offset |
| increment1 | Integer | – | First increment |
| mmsi2 | Integer | 9 digits | Second MMSI (if present) |
| offset2 | Integer | – | Second offset |
| increment2 | Integer | – | Second increment |

### Type 17: DGNSS Binary Broadcast Message {#type-17}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| lon | Float | ±180° | Longitude (1/600 degree resolution) |
| lat | Float | ±90° | Latitude (1/600 degree resolution) |
| data | String | hex | DGNSS data |

### Type 18: Standard Class B CS Position Report {#type-18}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| reserved | Integer | – | Reserved |
| speed | Float | 0–102.2 knots | Speed over ground |
| accuracy | Boolean | – | Position accuracy |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| course | Float | 0–359.9° | Course over ground |
| heading | Integer | 0–359° | True heading |
| second | Integer | 0–59 | UTC second |
| regional | Integer | – | Regional reserved |
| cs | Boolean | – | Class B unit type flag (false = SOTDMA, true = Carrier Sense) |
| display | Boolean | – | Display flag |
| dsc | Boolean | – | DSC flag |
| band | Boolean | – | Band flag |
| msg22 | Boolean | – | Message 22 flag |
| assigned | Boolean | – | Assigned mode flag |
| raim | Boolean | – | RAIM flag |
| radio | Integer | – | Radio status. See note 5 for sub-fields. |

### Type 19: Extended Class B CS Position Report {#type-19}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| reserved | Integer | – | Reserved |
| speed | Float | 0–102.2 knots | Speed over ground |
| accuracy | Boolean | – | Position accuracy |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| course | Float | 0–359.9° | Course over ground |
| heading | Integer | 0–359° | True heading |
| second | Integer | 0–59 | UTC second |
| regional | Integer | – | Regional reserved |
| shipname | String | 20 chars | Vessel name |
| shiptype | Integer | 0–99 | Ship type code |
| shiptype_text | String | See note 3 | Ship type description |
| to_bow | Integer | 0–511 m | Dimension to bow |
| to_stern | Integer | 0–511 m | Dimension to stern |
| to_port | Integer | 0–63 m | Dimension to port |
| to_starboard | Integer | 0–63 m | Dimension to starboard |
| epfd | Integer | 0–8 | EPFD type |
| epfd_text | String | See note 2 | EPFD description |
| raim | Boolean | – | RAIM flag |
| dte | Boolean | – | DTE flag |
| assigned | Boolean | – | Assigned mode flag |
| spare | Integer | – | Spare bits |

### Type 20: Data Link Management {#type-20}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| offset1 | Integer | – | Offset number 1 |
| number1 | Integer | – | Reserved slots 1 |
| timeout1 | Integer | minutes | Timeout 1 |
| increment1 | Integer | – | Increment 1 |
| offset2 | Integer | – | Offset number 2 (if present) |
| number2 | Integer | – | Reserved slots 2 |
| timeout2 | Integer | minutes | Timeout 2 |
| increment2 | Integer | – | Increment 2 |
| offset3 | Integer | – | Offset number 3 (if present) |
| number3 | Integer | – | Reserved slots 3 |
| timeout3 | Integer | minutes | Timeout 3 |
| increment3 | Integer | – | Increment 3 |
| offset4 | Integer | – | Offset number 4 (if present) |
| number4 | Integer | – | Reserved slots 4 |
| timeout4 | Integer | minutes | Timeout 4 |
| increment4 | Integer | – | Increment 4 |

### Type 21: Aid-to-Navigation Report {#type-21}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| aid_type | Integer | 0–31 | Aid type |
| aid_type_text | String | See note 4 | Aid type description |
| name | String | 20 chars | Name of aid |
| accuracy | Boolean | – | Position accuracy |
| lon | Float | ±180° | Longitude |
| lat | Float | ±90° | Latitude |
| to_bow | Integer | 0–511 m | Dimension to bow |
| to_stern | Integer | 0–511 m | Dimension to stern |
| to_port | Integer | 0–63 m | Dimension to port |
| to_starboard | Integer | 0–63 m | Dimension to starboard |
| epfd | Integer | 0–8 | EPFD type |
| epfd_text | String | See note 2 | EPFD description |
| second | Integer | 0–59 | UTC second |
| off_position | Boolean | – | Off position indicator |
| regional | Integer | – | Regional reserved |
| raim | Boolean | – | RAIM flag |
| virtual_aid | Boolean | – | Virtual aid flag |
| assigned | Boolean | – | Assigned mode flag |

### Type 22: Channel Management {#type-22}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| channel_a | Integer | – | Channel A number |
| channel_b | Integer | – | Channel B number |
| txrx | Integer | – | Tx/Rx mode |
| power | Boolean | – | Transmit power flag (0 = high, 1 = low) |
| addressed | Boolean | – | Addressed flag |
| band_a | Boolean | – | Channel A band (0 = default, 1 = 12.5 kHz allowed) |
| band_b | Boolean | – | Channel B band |
| zonesize | Integer | – | Size of transitional zone |

If `addressed = true`:

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| dest1 | Integer | 9 digits | Destination MMSI 1 |
| dest2 | Integer | 9 digits | Destination MMSI 2 |

If `addressed = false`:

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| ne_lon | Float | ±180° | NE longitude |
| ne_lat | Float | ±90° | NE latitude |
| sw_lon | Float | ±180° | SW longitude |
| sw_lat | Float | ±90° | SW latitude |

### Type 23: Group Assignment Command {#type-23}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| ne_lon | Float | ±180° | NE longitude |
| ne_lat | Float | ±90° | NE latitude |
| sw_lon | Float | ±180° | SW longitude |
| sw_lat | Float | ±90° | SW latitude |
| station_type | Integer | – | Station type |
| ship_type | Integer | – | Ship type |
| txrx | Integer | – | Tx/Rx mode |
| interval | Integer | – | Reporting interval |
| quiet | Integer | minutes | Quiet time |

### Type 24: Static Data Report {#type-24}

Message Type 24 Part A:

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| partno | Integer | 0 | Part number, always 0 for Part A |
| shipname | String | 20 chars | Name of the vessel |

Message Type 24 Part B:

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| partno | Integer | 1 | Part number, always 1 for Part B |
| shiptype | Integer | 0–99 | Type of ship and cargo |
| shiptype_text | String | See note 3 | Description of ship type |
| vendorid | String | 3 chars | Manufacturer's ID |
| model | Integer | 0–15 | Equipment model code |
| serial | Integer | 0–999999 | Unit serial number |
| callsign | String | 7 chars | Vessel radio callsign |
| to_bow | Integer | 0–511 m | Distance from GPS to bow |
| to_stern | Integer | 0–511 m | Distance from GPS to stern |
| to_port | Integer | 0–63 m | Distance from GPS to port |
| to_starboard | Integer | 0–63 m | Distance from GPS to starboard |
| mothership_mmsi | Integer | 9 digits | MMSI of mothership (only for auxiliary craft, MMSI prefix 98) |

### Type 25, 26: Single Slot / Multi Slot Binary Message {#type-2526}

These message types are not currently decoded by AIS-catcher; only the [common fields](#common-fields) are emitted. The raw payload is available in the `nmea` array.

### Type 27: Long-Range AIS Broadcast {#type-27}

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| accuracy | Boolean | – | Position accuracy (true if <10 m) |
| raim | Boolean | – | RAIM flag |
| status | Integer | 0–15 | Navigation status |
| status_text | String | See note 1 | Navigation status description |
| lon | Float | ±180° | Longitude (1/600 degree resolution) |
| lat | Float | ±90° | Latitude (1/600 degree resolution) |
| speed | Integer | 0–62 knots | Speed over ground |
| course | Integer | 0–359° | Course over ground |
| gnss | Boolean | – | GNSS position status (0 = current, 1 = not GNSS) |

## ASM payloads (Type 6 / Type 8) {#asm}

For Type 6 and Type 8 messages, AIS-catcher decodes selected Application-Specific Messages (ASMs) identified by the `(dac, fid)` pair. When a decoder matches, the structured fields below are emitted **in addition to** the per-type fields (`dac`, `fid`, etc.); when no decoder matches, the raw payload is emitted as `data` (hex string).

**Jump to:**
[IMO/ITU-R (DAC=1)](#asm-imo) ·
[IALA Zeni Lite Buoy (DAC=0)](#asm-iala) ·
[Inland AIS (DAC=200)](#asm-inland) ·
[IALA UK & ROI (DAC=235/250)](#asm-uk) ·
[St Lawrence Seaway (DAC=316/366)](#asm-sls) ·
[US Environmental (DAC=367)](#asm-us)

### IMO / ITU-R M.1371 (DAC = 1) {#asm-imo}

#### FID = 0: Text using 6-bit ASCII (msg 6 and 8)

| Field | Type | Description |
|-------|------|-------------|
| ack_required | Boolean | Acknowledgement required |
| text_sequence | Integer | Sequence number for multi-part text |
| text | String | Text payload |

#### FID = 2: Interrogation for a specified FMS (msg 6)

| Field | Type | Description |
|-------|------|-------------|
| requested_dac | Integer | Designated Area Code requested |
| requested_fid | Integer | Functional Identifier requested |

#### FID = 3: Extended interrogation (msg 6)

| Field | Type | Description |
|-------|------|-------------|
| requested_dac | Integer | Designated Area Code requested |
| spare | Integer | Spare bits |

#### FID = 4: Capability reply (msg 6)

| Field | Type | Description |
|-------|------|-------------|
| ai_available | String | 128-bit AI-available bitstring (ASCII '0'/'1') |

#### FID = 11: Legacy meteorological/hydrological (msg 8, IMO SN/Circ.236)

Same fields as FID = 31 below (legacy encoding; superseded by FID = 31).

#### FID = 16: Persons on board (msg 6) / VTS targets (msg 8)

The same `(DAC=1, FID=16)` slot is reused for two different payloads depending on message type.

In **msg 6** (number of persons on board, also FID = 40):

| Field | Type | Description |
|-------|------|-------------|
| persons | Integer | Number of persons on board |

In **msg 8** (VTS targets, IMO Circ.289 §6):

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| vts_target_id_type | Integer | – | Target ID type |
| vts_target_id | Integer or String | – | Target identifier (string when id_type = 2; numeric otherwise) |
| spare | Integer | – | Spare bits |
| vts_target_lat | Float | degrees | Target latitude |
| vts_target_lon | Float | degrees | Target longitude |
| vts_target_cog | Integer | degrees | Target course over ground |
| vts_target_timestamp | Integer | seconds | UTC second of report |
| vts_target_sog | Integer | knots | Target speed over ground |

#### FID = 21: Weather observation from ship (msg 8, IMO Circ.289 §10)

Only the non-WMO variant (variant 0) is decoded.

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| weather_report_type | Integer | – | Variant indicator (0 = non-WMO, 1 = WMO BUFR — not decoded) |
| station_name | String | – | Reporting station name |
| lon | Float | degrees | Longitude |
| lat | Float | degrees | Latitude |
| day | Integer | – | UTC day |
| hour | Integer | – | UTC hour |
| minute | Integer | – | UTC minute |
| present_weather | Integer | – | Present weather code |
| visgreater | Boolean | – | Visibility-greater-than flag |
| visibility | Float | nm | Horizontal visibility |
| humidity | Integer | percent | Relative humidity |
| wspeed | Integer | knots | Wind speed |
| wdir | Integer | degrees | Wind direction |
| pressure | Integer | hPa | Atmospheric pressure |
| pressuretend_wmo | Integer | – | Pressure tendency (WMO FM-13) |
| airtemp | Float | °C | Air temperature |
| watertemp | Float | °C | Water temperature |
| waveperiod | Integer | seconds | Wave period |
| waveheight | Float | metres | Wave height |
| wavedir | Integer | degrees | Wave direction |
| swellheight | Float | metres | Swell height |
| swelldir | Integer | degrees | Swell direction |
| swellperiod | Integer | seconds | Swell period |

#### FID = 26: Environmental (msg 8, IMO Circ.289 §12)

Only the first sensor report's common header is decoded; per-sensor bodies are not.

| Field | Type | Description |
|-------|------|-------------|
| sensor_report_type | Integer | Sensor report type (Table 12.4) |
| day | Integer | UTC day |
| hour | Integer | UTC hour |
| minute | Integer | UTC minute |
| site_id | Integer | Site identifier |

#### FID = 27: Route information, broadcast (msg 8, IMO Circ.289 §13)

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| linkage_id | Integer | – | Message linkage ID |
| sender_classification | Integer | – | Sender classification |
| route_type | Integer | – | Route type |
| month | Integer | – | UTC month |
| day | Integer | – | UTC day |
| hour | Integer | – | UTC hour |
| minute | Integer | – | UTC minute |
| duration_minutes | Integer | minutes | Route validity duration |
| waypoint_count | Integer | – | Number of waypoints |
| waypoints | String | – | Waypoint list as `lat,lon[;lat,lon]…` |

#### FID = 29: Text description, broadcast (msg 8, IMO Circ.289 §14)

| Field | Type | Description |
|-------|------|-------------|
| linkage_id | Integer | Message linkage ID |
| text | String | Text description |

#### FID = 30: Text description, addressed (msg 6, IMO Circ.289 §14)

| Field | Type | Description |
|-------|------|-------------|
| linkage_id | Integer | Message linkage ID |
| text | String | Text description |

#### FID = 31: Meteorological/hydrological data (msg 8, IMO Circ.289 §11)

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| lon | Float | degrees | Longitude |
| lat | Float | degrees | Latitude |
| accuracy | Boolean | – | Position accuracy |
| day | Integer | – | UTC day |
| hour | Integer | – | UTC hour |
| minute | Integer | – | UTC minute |
| wspeed | Integer | knots | Wind speed |
| wgust | Integer | knots | Wind gust |
| wdir | Integer | degrees | Wind direction |
| wgustdir | Integer | degrees | Wind gust direction |
| airtemp | Float | °C | Air temperature |
| humidity | Integer | percent | Relative humidity |
| dewpoint | Float | °C | Dew point |
| pressure | Integer | hPa | Atmospheric pressure |
| pressuretend | Integer | – | Pressure tendency |
| visgreater | Boolean | – | Visibility-greater-than flag |
| visibility | Float | nm | Horizontal visibility |
| waterlevel | Float | metres | Water level (deviation from chart datum) |
| leveltrend | Integer | – | Water level trend |
| cspeed | Float | knots | Surface current speed |
| cdir | Integer | degrees | Surface current direction |
| cspeed2 | Float | knots | Current speed at depth #2 |
| cdir2 | Integer | degrees | Current direction at depth #2 |
| cdepth2 | Integer | metres | Measurement depth #2 |
| cspeed3 | Float | knots | Current speed at depth #3 |
| cdir3 | Integer | degrees | Current direction at depth #3 |
| cdepth3 | Integer | metres | Measurement depth #3 |
| waveheight | Float | metres | Wave height |
| waveperiod | Integer | seconds | Wave period |
| wavedir | Integer | degrees | Wave direction |
| swellheight | Float | metres | Swell height |
| swellperiod | Integer | seconds | Swell period |
| swelldir | Integer | degrees | Swell direction |
| seastate | Integer | – | Sea state (Beaufort) |
| watertemp | Float | °C | Water temperature |
| preciptype | Integer | – | Precipitation type |
| salinity | Integer | percent | Salinity |
| ice | Integer | – | Ice indicator |

### IALA Zeni Lite Buoy (DAC = 0, FID = 0, msg 6) {#asm-iala}

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| asm_sub_app_id | Integer | – | ASM sub-application ID |
| asm_voltage_data | Float | V | Voltage sensor data |
| asm_current_data | Float | A | Current sensor data |
| asm_power_supply_type | Boolean | – | Power supply type |
| asm_light_status | Boolean | – | Light status |
| asm_battery_status | Boolean | – | Battery status |
| asm_off_position_status | Boolean | – | Off-position status |
| spare | Integer | – | Spare bits |

### Inland AIS — CCNR/CESNI (DAC = 200) {#asm-inland}

#### FID = 10: ERI ship static voyage data (msg 8)

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| vin | String | – | European Number of Vessel (ERI ENI) |
| length | Float | metres | Overall length of vessel |
| beam | Float | metres | Beam |
| shiptype | Integer | – | ERI ship type |
| hazard | Integer | – | Hazardous cargo code |
| draught | Float | metres | Draught |
| loaded | Integer | – | Loaded/unloaded |
| speed_q | Boolean | – | Speed quality |
| course_q | Boolean | – | Course quality |
| heading_q | Boolean | – | Heading quality |

#### FID = 25: Bridge clearance (msg 8)

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| asm_version | Integer | – | ASM version indicator |
| un_country | String | – | UN country code |
| fairway_section | Integer | – | Fairway section number |
| object_code | String | – | Object code |
| fairway_hectometre | Integer | – | Fairway hectometre |
| bridge_clearance | Integer | cm | Bridge clearance from water surface |
| measurement_age | Integer | minutes | Age of measurement |
| clearance_accuracy | Integer | cm | Bridge clearance accuracy (±cm) |

#### FID = 55: Persons on board, detailed (msg 6)

| Field | Type | Description |
|-------|------|-------------|
| crew_count | Integer | Number of crew |
| passenger_count | Integer | Number of passengers |
| shipboard_personnel_count | Integer | Other shipboard personnel |

### IALA UK & ROI (DAC = 235 / 250) {#asm-uk}

#### FID = 10: Aid-to-navigation monitor (msg 6)

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| ana_int | Float | V | Internal analogue voltage |
| ana_ext1 | Float | V | External analogue input 1 |
| ana_ext2 | Float | V | External analogue input 2 |
| racon | Integer | – | RACON status |
| health | Integer | – | Health status |
| stat_ext | Integer | – | External digital input status (8-bit) |
| off_position | Boolean | – | Off-position flag |

#### FID = 20: Trinity House buoy position monitoring (msg 6, DAC = 235 only)

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| station_name | String | – | Station name |
| utc_day | Integer | – | UTC day |
| utc_hour | Integer | – | UTC hour |
| utc_minute | Integer | – | UTC minute |
| lon | Float | degrees | Longitude |
| lat | Float | degrees | Latitude |
| off_position | Boolean | – | Off-position flag |
| spare | Integer | – | Spare bits |

### St Lawrence Seaway (DAC = 316 CA / 366 US) {#asm-sls}

#### FID = 1: Meteorological/hydrological (msg 6 and 8)

`message_id` selects the sub-payload (1 = weather, 2 = wind, 3 = water level, 6 = water flow). All variants share a common header.

Common header (all variants):

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| message_id | Integer | – | Sub-message identifier |
| month | Integer | – | UTC month |
| day | Integer | – | UTC day |
| hour | Integer | – | UTC hour |
| minute | Integer | – | UTC minute |
| station_id | String | – | Station identifier (7-char ASCII) |
| lon | Float | degrees | Longitude |
| lat | Float | degrees | Latitude |

`message_id = 1` (weather) adds:

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| wspeed | Float | m/s | Wind speed |
| wgust | Float | knots | Wind gust |
| wdir | Integer | degrees | Wind direction |
| barometric_pressure | Integer | hPa | Barometric pressure |
| air_temperature | Float | °C | Air temperature |
| dew_point | Float | °C | Dew point |
| visibility_km | Float | km | Horizontal visibility |
| watertemp | Float | °C | Water temperature |

`message_id = 2` (wind) adds:

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| wind_speed_avg | Float | knots | Average wind speed |
| wind_gust_speed | Float | knots | Wind gust speed |
| wind_direction_avg | Integer | degrees | Average wind direction |
| spare | Integer | – | Spare bits |

`message_id = 3` (water level) adds:

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| water_level_type | Integer | – | Water level type |
| waterlevel | Float | metres | Water level |
| reference_datum | Integer | – | Reference datum |
| reading_type | Integer | – | Reading type |
| spare | Integer | – | Spare bits |

`message_id = 6` (water flow) adds:

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| water_flow | Integer | – | Water flow |
| spare | Integer | – | Spare bits |

#### FID = 2 (lock scheduling) and FID = 32 (specific): only `message_id` is decoded.

### US Environmental Sensor Report (DAC = 367, FID = 33, msg 8) {#asm-us}

Common header:

| Field | Type | Description |
|-------|------|-------------|
| report_type | Integer | Sensor report type (selects body fields) |
| day | Integer | UTC day |
| hour | Integer | UTC hour |
| minute | Integer | UTC minute |
| site_id | Integer | Site identifier |

Only the **first** sensor report body is decoded.

`report_type = 0` (location) body adds:

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| version | Integer | – | Sensor version |
| lon | Float | degrees | Longitude |
| lat | Float | degrees | Latitude |
| precision | Integer | – | Position precision |
| alt | Integer | metres | Altitude |

`report_type = 1` (station identification) body adds:

| Field | Type | Description |
|-------|------|-------------|
| name | String | Station name |

`report_type = 2` (wind) body adds:

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| wspeed | Integer | knots | Wind speed |
| wgust | Integer | knots | Wind gust |
| wdir | Integer | degrees | Wind direction |
| wgustdir | Integer | degrees | Wind gust direction |
| sensor_description | Integer | – | Sensor description code |
| forecast_wspeed | Integer | knots | Forecast wind speed |
| forecast_wgust | Integer | knots | Forecast wind gust |
| forecast_wdir | Integer | degrees | Forecast wind direction |
| forecast_day | Integer | – | Forecast UTC day |
| forecast_hour | Integer | – | Forecast UTC hour |
| forecast_minute | Integer | – | Forecast UTC minute |
| forecast_duration | Integer | minutes | Forecast validity duration |

`report_type = 3` (water level) body adds:

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| water_level_type | Integer | – | Water level type |
| waterlevel | Float | metres | Water level |
| leveltrend | Integer | – | Water level trend |
| reference_datum | Integer | – | Reference datum |

## Notes

### Note 1: Navigation Status Values

| Value | Description |
|-------|-------------|
| 0 | Under way using engine |
| 1 | At anchor |
| 2 | Not under command |
| 3 | Restricted maneuverability |
| 4 | Constrained by her draught |
| 5 | Moored |
| 6 | Aground |
| 7 | Engaged in fishing |
| 8 | Under way sailing |
| 9 | Reserved for HSC |
| 10 | Reserved for WIG |
| 11 | Towing astern (regional) |
| 12 | Pushing ahead or towing alongside (regional) |
| 13 | Reserved |
| 14 | AIS-SART is active |
| 15 | Not defined |

### Note 2: EPFD Type Values

| Value | Description |
|-------|-------------|
| 0 | Undefined |
| 1 | GPS |
| 2 | GLONASS |
| 3 | Combined GPS/GLONASS |
| 4 | Loran-C |
| 5 | Chayka |
| 6 | Integrated navigation system |
| 7 | Surveyed |
| 8 | Galileo |

### Note 3: Ship Type Values

| Value | Description |
|-------|-------------|
| 0 | Not available |
| 1-19 | Reserved |
| 20 | Wing in ground (WIG) - all ships of this type |
| 21 | Wing in ground (WIG) - Hazardous category A |
| 22 | Wing in ground (WIG) - Hazardous category B |
| 23 | Wing in ground (WIG) - Hazardous category C |
| 24 | Wing in ground (WIG) - Hazardous category D |
| 25-29 | Wing in ground (WIG) - Reserved |
| 30 | Fishing |
| 31 | Towing |
| 32 | Towing: length exceeds 200m or breadth exceeds 25m |
| 33 | Dredging or underwater ops |
| 34 | Diving ops |
| 35 | Military ops |
| 36 | Sailing |
| 37 | Pleasure Craft |
| 38-39 | Reserved |
| 40 | High speed craft (HSC) - all ships of this type |
| 41 | High speed craft (HSC) - Hazardous category A |
| 42 | High speed craft (HSC) - Hazardous category B |
| 43 | High speed craft (HSC) - Hazardous category C |
| 44 | High speed craft (HSC) - Hazardous category D |
| 45-48 | High speed craft (HSC) - Reserved for future use |
| 49 | High speed craft (HSC) - No additional information |
| 50 | Pilot Vessel |
| 51 | Search and Rescue vessel |
| 52 | Tug |
| 53 | Port Tender |
| 54 | Anti-pollution equipment |
| 55 | Law Enforcement |
| 56-57 | Spare - Local Vessel |
| 58 | Medical Transport |
| 59 | Noncombatant ship according to RR Resolution No. 18 |
| 60 | Passenger - all ships of this type |
| 61 | Passenger - Hazardous category A |
| 62 | Passenger - Hazardous category B |
| 63 | Passenger - Hazardous category C |
| 64 | Passenger - Hazardous category D |
| 65-68 | Passenger - Reserved for future use |
| 69 | Passenger - No additional information |
| 70 | Cargo - all ships of this type |
| 71 | Cargo - Hazardous category A |
| 72 | Cargo - Hazardous category B |
| 73 | Cargo - Hazardous category C |
| 74 | Cargo - Hazardous category D |
| 75-78 | Cargo - Reserved for future use |
| 79 | Cargo - No additional information |
| 80 | Tanker - all ships of this type |
| 81 | Tanker - Hazardous category A |
| 82 | Tanker - Hazardous category B |
| 83 | Tanker - Hazardous category C |
| 84 | Tanker - Hazardous category D |
| 85-88 | Tanker - Reserved for future use |
| 89 | Tanker - No additional information |
| 90 | Other Type - all ships of this type |
| 91 | Other Type - Hazardous category A |
| 92 | Other Type - Hazardous category B |
| 93 | Other Type - Hazardous category C |
| 94 | Other Type - Hazardous category D |
| 95-98 | Other Type - Reserved for future use |
| 99 | Other Type - no additional information |

### Note 4: Aid to Navigation Type Values

| Value | Description |
|-------|-------------|
| 0 | Default, Type of Aid to Navigation not specified |
| 1 | Reference point |
| 2 | RACON (radar transponder marking a navigation hazard) |
| 3 | Fixed offshore structure |
| 4 | Spare, Reserved for future use |
| 5 | Light, without sectors |
| 6 | Light, with sectors |
| 7 | Leading Light Front |
| 8 | Leading Light Rear |
| 9 | Beacon, Cardinal N |
| 10 | Beacon, Cardinal E |
| 11 | Beacon, Cardinal S |
| 12 | Beacon, Cardinal W |
| 13 | Beacon, Port hand |
| 14 | Beacon, Starboard hand |
| 15 | Beacon, Preferred Channel port hand |
| 16 | Beacon, Preferred Channel starboard hand |
| 17 | Beacon, Isolated danger |
| 18 | Beacon, Safe water |
| 19 | Beacon, Special mark |
| 20 | Cardinal Mark N |
| 21 | Cardinal Mark E |
| 22 | Cardinal Mark S |
| 23 | Cardinal Mark W |
| 24 | Port hand Mark |
| 25 | Starboard hand Mark |
| 26 | Preferred Channel Port hand |
| 27 | Preferred Channel Starboard hand |
| 28 | Isolated danger |
| 29 | Safe Water |
| 30 | Special Mark |
| 31 | Light Vessel / LANBY / Rigs |

### Note 5: Radio status sub-fields

When `radio` is non-zero on a Type 1/2/3/4/9/11/18 message, AIS-catcher decodes the SOTDMA/ITDMA state into additional fields:

| Field | Type | Description |
|-------|------|-------------|
| sync_state | Integer | Sync state (0–3) |
| slot_timeout | Integer | Frames until new slot (0 = next frame) |
| slot_offset | Integer | Slot offset (only when `slot_timeout = 0`) |
| utc_hour | Integer | UTC hour from sync (only when `slot_timeout = 1`) |
| utc_minute | Integer | UTC minute from sync (only when `slot_timeout = 1`) |
| slot_number | Integer | TDMA slot number used (only when `slot_timeout` ∈ {2, 4, 6}) |
| received_stations | Integer | Stations received in last frame (only when `slot_timeout` ∈ {3, 5, 7}) |
