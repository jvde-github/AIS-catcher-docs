# Getting Around the Dashboard

In managed mode, AIS-catcher hosts a **dashboard**: a web interface from which you set up, monitor and run your complete station — input device, decoder settings and all outputs — directly from the browser. All settings live in a JSON configuration file that AIS-catcher creates and maintains itself; there is nothing to edit by hand.

<!-- TODO screenshot: dashboard-overview.webp — the full dashboard with map, control buttons and menus visible; ideally annotated -->

## Opening the Dashboard

Managed mode is simply AIS-catcher started with the `-E` option — the same program, serving its own dashboard. Each [installation](../installation/overview.md) ends with AIS-catcher already running this way, so you can open the dashboard right away in a browser on the machine AIS-catcher runs on:

```
http://localhost:8118
```

From another device on your network, use the receiver's address instead, e.g. `http://raspberrypi.local:8118` or `http://192.168.1.50:8118` — this requires AIS-catcher to be reachable from the network and a password, see [Remote Access and Security](remote-access.md).

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

Every underlying setting is documented in detail in the [Configuration Reference](../configuration/overview.md).

## Starting Managed Mode Yourself

The [installation](../installation/overview.md) for each platform normally leaves AIS-catcher running in managed mode, so this section is only needed as a backup — for example after a manual install or when running from a terminal.

Managed mode is the default: start AIS-catcher without any command-line options and it comes up in managed mode.

```console
AIS-catcher
```

<!-- TODO: confirm final behaviour and defaults — config file location and listen address when started bare, and from which release this is the default -->

The configuration file and listen address can be set explicitly with the `-E` switch:

```console
AIS-catcher -E /etc/AIS-catcher/config.json 127.0.0.1:8118
```

As soon as any other command-line option is given, AIS-catcher runs in [manual mode](../usage/overview.md) instead and behaves as the classic command-line tool: it does exactly what you type, and the dashboard and its configuration file are not in play.
