# JSON Configuration

AIS-catcher (v0.41+) supports configuration via JSON format:

```bash
AIS-catcher -C config.json
```

## Basic Structure

Required minimal configuration:
```json
{
    "config": "aiscatcher",
    "version": 1
}
```

## Configuration Keys

## Core Settings

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

## Input Device Settings

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
        "buffer_count": 2
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