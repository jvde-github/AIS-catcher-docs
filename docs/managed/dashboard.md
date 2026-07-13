# Getting Around the Dashboard

In managed mode, AIS-catcher hosts a **dashboard**: a web interface from which you set up, monitor and run your complete station — input device, decoder settings and all outputs — directly from the browser. All settings live in a JSON configuration file that AIS-catcher creates and maintains itself; there is nothing to edit by hand.

<!-- TODO screenshot: dashboard-overview.webp — the full dashboard with map, control buttons and menus visible; ideally annotated -->

## Opening the Dashboard

Managed mode is simply AIS-catcher started with the `-E` option — the same program, serving its own dashboard. Each [installation](../installation/overview.md) ends with AIS-catcher already running this way, so you can open the dashboard right away in a browser on the machine AIS-catcher runs on: `http://localhost:8118`{ .address }

From another device on your network, use the receiver's address instead, e.g. `http://raspberrypi.local:8118`{ .address } or `http://192.168.1.50:8118`{ .address } — this requires AIS-catcher to be reachable from the network and a password, see [Remote Access and Security](remote-access.md).

On first use, a short [setup wizard](setup-wizard.md) walks you through configuring your station.

## The Map

The dashboard shows the vessels you are receiving live on a map, so you can see at a glance that your station is working and what your coverage looks like.

<!-- TODO screenshot: dashboard-map.webp -->

!!! note
    The dashboard map is a simplified view for monitoring your own station. For a full-featured, customizable map that you can share with others, add a [web viewer](output.md#web-viewer) as an output.

## Controlling the Receiver

The receiver is started and stopped directly from the dashboard — there is no need to restart the program or touch the command line.

<!-- TODO screenshot: dashboard-controls.webp — the start/stop/restart buttons and status indicator -->
<!-- TODO: confirm the exact buttons and status elements (start / stop / restart, log view?) -->

After changing any setting, press **Save**, then restart the receiver for the changes to take effect.

## Settings Menus

All configuration is reached from the menus in the **bottom bar** of the dashboard:

- **Input** — the receiver: device type, channels, tuner gain, sample rate and high-sensitivity mode. See [Input Settings](input.md).
- **Output** — where your data goes: the community feed, UDP, HTTP, MQTT, TCP and web viewers. See [Output Settings](output.md).
- **System** — dashboard and system settings, such as remote access and the password.

<!-- TODO: confirm what the System menu contains (log, password, remote access, backup?) and adjust the description -->

Every underlying setting is documented in detail in the [Settings reference](../configuration/overview.md).

## Starting Managed Mode Yourself

Each platform's [installation](../installation/overview.md) normally leaves AIS-catcher running in managed mode, so starting it yourself is rarely necessary — typically only after a manual installation or when running AIS-catcher from a terminal.

Managed mode is not the default: it must be enabled explicitly with the `-E` switch, which takes the configuration file and the address the dashboard listens on:

```console
AIS-catcher -E /etc/AIS-catcher/config.json 127.0.0.1:8118
```

When any other command-line option is supplied, AIS-catcher runs in [manual mode](../usage/overview.md) instead and behaves as the classic command-line tool: it executes exactly what you type, and neither the dashboard nor its configuration file is used.
