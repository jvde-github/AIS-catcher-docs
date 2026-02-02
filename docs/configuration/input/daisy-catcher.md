# dAISy Catcher

The **dAISy catcher** is a plug-and-play AIS receiver device from [Wegmatt](https://wegmatt.com). It can be configured to provide output compatible with AIS-catcher, including timestamps, frequency offset, and signal levels. The device connects via serial port (either HAT or USB connection).

## Overview

The **dAISy catcher** outputs NMEA AIS messages over a serial connection (default format, but other formats are available). It can be configured in AIS-catcher as a serial device and connected either via the HAT interface (GPIO serial port) or USB, depending on your setup. AIS-catcher's functionality to send commands to serial devices at startup allows you to configure the **dAISy catcher** directly from the AIS-catcher user interface.

## Setup and Requirements

The first step is to physically connect the **dAISy catcher** to your device. Below are quick instructions for both connection methods.

### Connection Methods

**Raspberry Pi with HAT**: Connect via GPIO serial port. The port varies by Raspberry Pi model (e.g., `/dev/serial0` on Raspberry Pi 4). Installation follows the [dAISy HAT setup guide](https://wegmatt.com/files/dAISy%20HAT%20AIS%20Receiver%20Quickstart.pdf).

**USB Connection**: Plug and play - simply connect via USB. The device path varies by operating system:
- **Linux**: `/dev/serial/by-id/usb-...`
- **Windows**: `COM3`, `COM4`, etc.
- **macOS**: `/dev/tty.usbserial-...`

**Important**: The **dAISy catcher** requires a baud rate of **115200** (different from the standard dAISy HAT).

## Web Control Configuration

For users running AIS-catcher with the [Visual Web Control](../../usage/gui.md) interface (available for Linux and Docker), you can configure the **dAISy catcher** through the web interface:

1. Access the Visual Web Control at `http://your-device:8110` (default credentials: admin/admin)
2. Navigate to the **Input** section
3. In the **Device Type** dropdown, select **SERIAL**
4. For the **Port** field:
   - Click the search icon (magnifying glass) next to the Port field
   - Select the appropriate serial port from the list (e.g., `/dev/serial0` for HAT on Raspberry Pi 4 or `/dev/serial/by-id/...` for USB)
5. Set the **Baud Rate** to `115200`
6. In the **Init Sequence** field, enter `co2,v`

![Web Control Configuration for dAISy Catcher](../../assets/daisy-catcher-webcontrol.png)

7. Click **Save** and then navigate to the **Control** section to restart AIS-catcher for the changes to take effect

This provides a user-friendly alternative to command-line configuration, especially for beginners.

## Command Line Configuration

#### Using HAT Connection (GPIO Serial)

On Raspberry Pi, the **dAISy catcher** connected via HAT uses the GPIO serial port. The port path varies by model (e.g., `/dev/serial0` on Raspberry Pi 4):

```bash
AIS-catcher -e 115200 /dev/serial0 -ge init_seq co2,v
```

#### Using USB Connection

When connected via USB, use the device by-id path for a persistent connection:

```bash
ls /dev/serial/by-id/
AIS-catcher -e 115200 /dev/serial/by-id/usb-... -ge init_seq co2,v
```

### Initialization Sequence

The `init_seq` parameter `co2,v` enables:

- **Signal level** information in the output
- **Frequency offset** reporting

This provides additional diagnostic information that can be useful for monitoring reception quality.

### Example with Output Options

To run the **dAISy catcher** with JSON output and signal quality information:

```bash
AIS-catcher -e 115200 /dev/serial0 -ge init_seq co2,v -o 5
```

### Debugging

To view the raw NMEA data being received from the device:

```bash
AIS-catcher -e 115200 /dev/serial0 -ge print on
```

## JSON Configuration

The **dAISy catcher** can also be configured using JSON:

```json
{
  "serial": {
    "port": "/dev/serial0",
    "baudrate": 115200,
    "init_seq": "co2,v"
  }
}
```

For USB connection:

```json
{
  "serial": {
    "port": "/dev/serial/by-id/usb-...",
    "baudrate": 115200,
    "init_seq": "co2,v"
  }
}
```

## Settings Reference

| Setting | Type | Value | Description |
|---------|------|-------|-------------|
| `baudrate` | integer | `115200` | Serial port speed (required) |
| `port` | string | `/dev/serial0` or `/dev/serial/by-id/...` | Serial port device path |
| `init_seq` | string | `co2,v` | Initialization commands (enables signal level and frequency offset) |
| `print` | boolean | `on` / `off` | Enable debug printing of received data |

## Additional Resources

- [Wegmatt Website](https://wegmatt.com) - Official manufacturer website (documentation may become available)
- [Visual Web Control Guide](../../usage/gui.md) - Setup guide for the web interface
