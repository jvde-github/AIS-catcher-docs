# JSON Configuration

AIS-catcher (v0.41+) supports extensive configuration through JSON files. This guide describes the JSON structure, key settings, and common patterns.

To start AIS-catcher with a JSON configuration file, use the `-C` option followed by the path to your `config.json` file:

```bash
AIS-catcher -C config.json
```
This loads and applies the settings from the JSON file.

## Basic Structure

A JSON configuration file always starts with the configuration header:
```json
{
    "config": "aiscatcher",
    "version": 1
}
```

Where:

- `config`: Identifies the configuration type. Must be `"aiscatcher"`.
- `version`: Configuration version. Currently, only `1` is supported.


This is the absolute minimal structure (just the first two keys). If no receiver is configured, AIS-catcher will use the default behaviour for selecting an input device.

To select the RTL-SDR as an input device:
```json
{
    "config": "aiscatcher",
    "version": 1,
    "receiver": [
        {
            "input": "rtlsdr"
        }
    ]
}
```


> Note: older configurations allowed receiver selection at the root level (e.g. `input`, `serial`). This is legacy and may disappear in a future release. Prefer defining receivers in the `receiver` array. [^legacy-root-receiver]

## Important Notes

- JSON keys are case-sensitive and must be lowercase.
- CLI setting names are not case-sensitive.
- Define receivers in the `receiver` array (even for a single receiver).
- Device sections (e.g. `rtlsdr`, `airspy`) configure the device, but do not select it. Use `input` (and optionally `serial`) inside each receiver object.
- `active` is optional in any section; if omitted, it is assumed to be `true`.
- Outputs like `udp` are arrays to support multiple output channels.

## Configuration Keys

Configuration keys are grouped below by purpose.

### General Overview

General (mostly optional) settings define fundamental aspects of AIS-catcher's operation.

#### Root-level keys

| Key | Type | Description | Documentation |
|-----|------|-------------|---------------|
| **General**  |
| `config` | string | "aiscatcher" | |
| `version` | number | 1 | |
| `sharing` | boolean | Enable community feed sharing | [Community Feed](../configuration/output/community-feed.md) |
| `sharing_key` | string | Community feed key | [Community Feed](../configuration/output/community-feed.md) |
| **Receiver array** |
| `receiver` | array | List of receiver objects (recommended even for a single receiver) [^legacy-root-receiver] | [Receiver configuration](#receiver-configuration-receiver-array) |
| **Output channels** |
| `server` | array | Web viewer configuration | [Web Viewer](../configuration/output/web-viewer.md) |
| `udp` | array | UDP output configuration | [UDP Output](../configuration/output/UDP.md) |
| `tcp` | array | TCP output configuration (client) | [TCP Output](../configuration/output/TCP-server.md) |
| `tcp_listener` | array | TCP output configuration (server) | [TCP Output](../configuration/output/TCP-server.md) |
| `http` | array | HTTP output configuration | [HTTP Output](../configuration/output/HTTP.md) |
| `mqtt` | array | MQTT output configuration | [MQTT Output](../configuration/output/MQTT.md) |

#### Receiver configuration (`receiver` array)

The root-level `receiver` key contains an array of receiver objects. This is the recommended structure going forward.

##### Receiver object keys

Each entry in the root-level `receiver` array is a receiver object. These keys live *inside* each receiver object:

| Key | Type | Description | Documentation |
|-----|------|-------------|---------------|
| `input` | string | Selects the input device type for this receiver (e.g. `rtlsdr`, `airspy`, `spyserver`, ...) | [Input Overview](../configuration/input/overview.md) |
| `serial` | string/number | Receiver identifier (recommended; also used to target per-receiver CLI overrides in some setups) | |
| `verbose` | boolean | Enable verbose output for this receiver | [Console Output](../configuration/output/console.md) |
| `verbose_time` | number | Verbose update interval (seconds) for this receiver | [Console Output](../configuration/output/console.md) |
| `screen` | number | Screen output mode (0-5) for this receiver | [Console Output](../configuration/output/console.md) |
| `meta` | string | Metadata tags (T/D/M) for this receiver | [Console Output](../configuration/output/console.md) |
| `own_mmsi` | number | Own MMSI of receiver station | |
| `<device section>` | object | Device-specific configuration object matching `input` (e.g. `rtlsdr`, `airspy`, ...). See examples in [Input Device Settings](#input-device-settings). | [Input Overview](../configuration/input/overview.md) |
| `model` | object | Decoder model configuration for this receiver | [Model](../configuration/model.md) |

##### Multi-receiver example

Example with two receivers:
```json
{
    "config": "aiscatcher",
    "version": 1,
    "receiver": [
        {
            "input": "airspy",
            "serial": "airspy",
            "airspy": {
                "sample_rate": "3000K"
            }
        },
        {
            "input": "rtlsdr",
            "serial": "ais",
            "rtlsdr": {
                "bandwidth": "192k"
            }
        }
    ]
}
```

In this example, each receiver selects a device via `input`, is optionally named via `serial`, and is configured via its device section (e.g. `rtlsdr`, `airspy`).

[^legacy-root-receiver]: Legacy configurations may use root-level `input` / `serial` to define a single receiver. This still works in some versions, but is discouraged and may be removed in a future release. Prefer putting `input` (and `serial`) inside each receiver object under `receiver`.

## Input Device Settings

AIS-catcher supports various input devices. Each device type has specific configuration options. Below are the supported devices and their respective settings. The documentation of the relevant keys can be found in the [Configuration](../configuration/input/overview.md) sections. Below we provide a few examples.

### RTL-SDR (`rtlsdr`)
<details>
<summary>Example</summary>

```json
{
    "rtlsdr": {
        "active": true,
        "rtlagc": true,
        "tuner": "auto",
        "bandwidth": "192K",
        "sample_rate": "1536K",
        "biastee": false
    }
}
```
</details>
[Full RTL-SDR Documentation](../configuration/input/rtlsdr.md)

### Airspy (`airspy`)
<details>
<summary>Example</summary>
```json
{
    "airspy": {
        "sample_rate": "3000K",
        "linearity": 17,
        "biastee": false
    }
}
```
</details>
[Full Airspy Documentation](../configuration/input/airspy.md)

### Airspy HF+ (`airspyhf`)
<details>
<summary>Example</summary>
```json
{
    "airspyhf": {
        "sample_rate": "192k",
        "threshold": "low",
        "preamp": false
    }
}
```
[Full Airspy HF+ Documentation](../configuration/input/airspyhf.md)
</details>

### HackRF (`hackrf`)
<details>
<summary>Example</summary>
```json
{
    "hackrf": {
        "sample_rate": "6144k",
        "lna": 8,
        "vga": 20,
        "preamp": false
    }
}
```
</details>
[Full HackRF Documentation](../configuration/input/hackrf.md)

### SDRPlay (`sdrplay`)
<details>
<summary>Example</summary>
```json
{
    "sdrplay": {
        "sample_rate": "2304K",
        "agc": true,
        "lnastate": 5,
        "grdb": 40
    }
}
```
</details>
[Full SDRPlay Documentation](../configuration/input/sdrplay.md)

### SoapySDR (`soapysdr`)
<details>
<summary>Example</summary>
```json
{
    "soapysdr": {
        "active": true,
        "device": "driver=rtlsdr",
        "sample_rate": "1536K"
    }
}
```
</details>
[Full SoapySDR Documentation](../configuration/input/soapysdr.md)

### Serial Port Input (`serialport`)
<details>
<summary>Example</summary>
```json
{
    "serialport": {
        "baudrate": 38400,
        "port": "/dev/tty0"
    }
}
```
</details>
[Full Serial Port Documentation](../configuration/input/serial.md)

### NMEA2000 (`nmea2000`)
<details>
<summary>Example</summary>
```json
{
    "nmea2000": {
        "active": true,
        "port": "can0"
    }
}
```
</details>
[Full NMEA2000 Documentation](../configuration/input/NMEA2000.md)

## File Input Settings

### WAV File (`wavfile`)
<details>
<summary>Example</summary>
```json
{
    "wavfile": {
        "active": true,
        "filename": "recording.wav"
    }
}
```
</details>
[Full WAV File Documentation](../configuration/input/wav.md)

### Raw File (`file`)
<details>
<summary>Example</summary>
```json
{
    "file": {
        "active": true,
        "filename": "data.raw"
    }
}
```
</details>
[Full File Documentation](../configuration/input/file.md)

## Network Input Settings

### TCP Client (`rtltcp`)
<details>
<summary>Example</summary>
```json
{
    "rtltcp": {
        "host": "192.168.1.100",
        "port": 12345
    }
}
```
</details>
[Full TCP Documentation](../configuration/input/tcp.md)

### SpyServer (`spyserver`)
<details>
<summary>Example</summary>
```json
{
    "spyserver": {
        "host": "server.example.com",
        "port": 5555
    }
}
```
</details>
[Full SpyServer Documentation](../configuration/input/spyserver.md)

### UDP Server (`udpserver`)
<details>
<summary>Example</summary>
```json
{
    "udpserver": {
        "active": true,
        "port": 10110
    }
}
```
</details>
[Full UDP Documentation](../configuration/input/udp.md)

### ZMQ (`zmq`)
<details>
<summary>Example</summary>
```json
{
    "zmq": {
        "active": true,
        "endpoint": "tcp://localhost:5555"
    }
}
```
</details>
[Full ZMQ Documentation](../configuration/input/tcp.md)

## Output Settings

AIS-catcher supports various output channels. Each output channel has specific configuration options.  The documentation of the relevant keys can be found in the [Configuration](../configuration/output/overview.md) sections with some JSON examples below.

### Web Viewer (`server`)
<details>
<summary>Example</summary>
```json
{
    "server": [
        {
            "active": true,
            "port": 8100,
            "station": "My Station",
            "share_loc": true,
            "lat": 52,
            "lon": 4.3
        }
    ]
}
```
</details>
[Full Web Server Documentation](../configuration/output/web-viewer.md)

### UDP Output (`udp`)
<details>
<summary>Example</summary>
```json
{
    "udp": [
        {
            "active": true,
            "host": "192.168.1.235",
            "port": 4002,
            "filter": false,
            "allow_type": "1,2,3,5,18,19,24"
        }
    ]
}
```
</details>
[Full UDP Documentation](../configuration/output/UDP.md)

### TCP  Output (Client) (`tcp`)
<details>
<summary>Example</summary>
```json
{
    "tcp": [
        {
            "active": true,
            "host": "5.9.207.224",
            "port": 12,
            "keep_alive": false
        }
    ]
}
```
</details>
[Full TCP Documentation](../configuration/output/TCP-server.md)

### TCP  Output (Server) (`tcp_listener`)
<details>
<summary>Example</summary>
```json
{
    "tcp_listener": [
        {
            "active": true,
            "port": 5012
        }
    ]
}
```
</details>
[Full TCP Documentation](../configuration/output/TCP-server.md)

### HTTP Output (`http`)
<details>
<summary>Example</summary>
```json
{
    "http": [
        {
            "active": true,
            "url": "http://example.com/ais",
            "interval": 10,
            "response": "json"
        }
    ]
}
```
</details>
[Full HTTP Documentation](../configuration/output/HTTP.md)

### MQTT Output (`mqtt`)
<details>
<summary>Example</summary>
```json
{
    "mqtt": [
        {
            "active": true,
            "host": "mqtt.example.com",
            "port": 1883,
            "topic": "ais/messages",
            "username": "user",
            "password": "pass"
        }
    ]
}
```
</details>
[Full MQTT Documentation](../configuration/output/MQTT.md)


