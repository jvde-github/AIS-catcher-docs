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

Core but optional settings define fundamental aspects of AIS-catcher's operation.

| Key | Type | Description | Documentation |
|-----|------|-------------|---------------|
| **General**  |
| `config` | string | "aiscatcher" | |
| `version` | number | 1 | |
| `sharing` | boolean | Enable community feed sharing | [Community Feed](../configuration/output/community-feed.md) |
| `sharing_key` | string | Community feed key | [Community Feed](../configuration/output/community-feed.md) |
| **Receiver** |
| `input` | string | Primary input device selection | rtlsdr/hackrf/etc |
| `serial` | string | Device serial number | |
| `verbose` | boolean | Enable verbose output | [Console Output](../configuration/output/console.md) |
| `screen` | number | Screen output mode (0-5) | [Console Output](../configuration/output/console.md) |

- `config`: Must always be set to "aiscatcher" to identify the configuration type.

- `version`: Defines the configuration file version. Ensure it is set to 1 as this is the currently supported version.

- `sharing`: Enables sharing of AIS data with the AIS-catcher community feed, allowing others to access your AIS data and vice versa.

- `sharing_key`: A unique key obtained from [aiscatcher.org](https://aiscatcher.org/addstation_ac) to easily share your AIS data with the community.

-   `input`: Specifies the primary input device for AIS data (e.g., "rtlsdr", "airspy", etc).

- `serial`: Defines the serial number of the device to be used. Useful when multiple devices are connected.

- `verbose`: When set to true, AIS-catcher provides detailed logs and output for debugging purposes.

- `screen`: Controls the verbosity and format of the console output. Values range from 0 (no output) to 5 (full JSON decoding). 

>## Important Notes
>
>JSON is case-sensitive; all keys must be lowercase. Device-specific sections only configure the device but don't select it - use `input` or `serial` for device selection. 
>The `active` boolean in any section enables/disables that configuration and if ommited it is assumed to be active.
>
>Outputs are often captured in a JSON-array, like for example for `udp`, to support multiple output channels.

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
        "biastee": false,
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

### TCP  Output (Server) (`tcp-listener`)
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

## Multi-Receiver Configuration

For multiple receivers,  you can more the relevant settings to a `receiver` array as in this example
starting two receivers:
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

