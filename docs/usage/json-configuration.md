# JSON Configuration

AIS-catcher (v0.41+) supports extensive configuration through JSON files, enabling users to tailor the application to their specific needs. This guide provides an in-depth look at the JSON configuration structure, key settings, and best practices to help you effectively set up and manage AIS-catcher.

To start AIS-catcher with a JSON configuration file, use the -C option followed by the path to your config.json file:

```bash
AIS-catcher -C config.json
```
This command instructs AIS-catcher to load and apply the settings defined in config.json.

## Basic Structure

A minimal JSON configuration file for AIS-catcher requires the following structure:
```json
{
    "config": "aiscatcher",
    "version": 1
}
```

- config: Identifies the configuration type. Must be "aiscatcher".
- version: Specifies the configuration version. Currently, only version 1 is supported.

## Configuration Keys

Configuration keys are organized into several categories to manage different aspects of AIS-catcher's functionality. Each key has a specific purpose and should be used as per the documentation.

### Core Settings

Core settings define fundamental aspects of AIS-catcher's operation.

| Key | Type | Description | Documentation |
|-----|------|-------------|---------------|
| `config` | string | "aiscatcher" | |
| `version` | number | 1 | |
| `input` | string | Primary input device selection | [Input Options](../configuration/input/overview.md) |
| `serial` | string | Device serial number | [Input Options](../configuration/input/overview.md) |
| `verbose` | boolean | Enable verbose output | [Console Output](../configuration/output/console.md) |
| `sharing` | boolean | Enable community feed sharing | [Community Feed](../configuration/output/community-feed.md) |
| `sharing_key` | string | Community feed key | [Community Feed](../configuration/output/community-feed.md) |
| `screen` | number | Screen output mode (0-5) | [Console Output](../configuration/output/console.md) |

- config: Must always be set to "aiscatcher" to identify the configuration type.

- version: Defines the configuration file version. Ensure it is set to 1 as this is the currently supported version.

-   input: Specifies the primary input device for AIS data (e.g., "rtlsdr", "airspy"). Refer to Input Options for supported devices.

- serial: Defines the serial number of the device to be used. Useful when multiple devices are connected.

- verbose: When set to true, AIS-catcher provides detailed logs and output for debugging purposes.

- sharing: Enables sharing of AIS data with the AIS-catcher community feed, allowing others to access your AIS data and vice versa.

- sharing_key: A unique key obtained from aiscatcher.org to securely share your AIS data with the community.

- screen: Controls the verbosity and format of the console output. Values range from 0 (no output) to 5 (full JSON decoding).

## Input Device Settings

AIS-catcher supports various input devices. Each device type has specific configuration options. Below are the supported devices and their respective settings.

### RTL-SDR (`rtlsdr`)
```json
{
    "rtlsdr": {
        "active": true,
        "rtlagc": true,
        "tuner": "auto",
        "bandwidth": "192K",
        "sample_rate": "1536K",
        "biastee": false,
    }
}
```
[Full RTL-SDR Documentation](../configuration/input/rtlsdr.md)

### Airspy (`airspy`)
```json
{
    "airspy": {
        "sample_rate": "3000K",
        "linearity": 17,
        "biastee": false
    }
}
```
[Full Airspy Documentation](../configuration/input/airspy.md)

### Airspy HF+ (`airspyhf`)
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

### HackRF (`hackrf`)
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
[Full HackRF Documentation](../configuration/input/hackrf.md)

### SDRPlay (`sdrplay`)
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
[Full SDRPlay Documentation](../configuration/input/sdrplay.md)

### Serial Port Input (`serialport`)
```json
{
    "serialport": {
        "baudrate": 38400,
        "port": "/dev/tty0"
    }
}
```
[Full Serial Port Documentation](../configuration/input/serial.md)

## Network Input Settings

### TCP Client (`tcp`)
```json
{
    "tcp": {
        "host": "192.168.1.100",
        "port": 12345
    }
}
```
[Full TCP Documentation](../configuration/input/tcp.md)

### SpyServer (`spyserver`)
```json
{
    "spyserver": {
        "host": "server.example.com",
        "port": 5555
    }
}
```
[Full SpyServer Documentation](../configuration/input/spyserver.md)

## Output Settings

### Web Viewer (`server`)
```json
{
    "server": {
        "active": true,
        "port": 8100,
        "station": "My Station",
        "share_loc": true,
        "lat": 52,
        "lon": 4.3
    }
}
```
[Full Web Server Documentation](../configuration/output/web-viewer.md)


### UDP Output (`udp`)
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
[Full UDP Documentation](../configuration/output/UDP.md)

### TCP Output (`tcp`)
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
[Full TCP Documentation](../configuration/output/TCP-client.md)

## Multi-Receiver Configuration

For multiple receivers, use the `receiver` array:
```json
{
    "config": "aiscatcher",
    "version": 1,
    "receiver": [
        {
            "input": "airspy",
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

## Important Notes

JSON is case-sensitive; all keys must be lowercase. Device-specific sections only configure the device but don't select it - use `input` or `serial` for device selection. The `active` boolean in any section enables/disables that configuration. Array-based outputs like for example for `udp` support multiple output channels.