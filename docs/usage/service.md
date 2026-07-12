# Running as a Service

On Debian-based systems (including Raspberry Pi), the [install script](../installation/raspberrypi.md) sets up the infrastructure to run AIS-catcher as a systemd background service that starts automatically at boot.

!!! note
    In managed mode this is all handled for you — the service runs the dashboard and you never touch these files. This page is for stations configured manually.

## Configuration Files

The background service reads two configuration files:

- `/etc/AIS-catcher/config.json` (JSON configuration)
- `/etc/AIS-catcher/config.cmd` (command line parameters)

The simplest approach is to edit `/etc/AIS-catcher/config.cmd` to capture your settings. Lines starting with `#` are considered comments and ignored. The file can be modified using a text editor, for example:

```console
sudo nano /etc/AIS-catcher/config.cmd
```

Please note that `config.json` takes precedence over `config.cmd`.

## Service Control

To start AIS-catcher as a background service:

```console
sudo systemctl start ais-catcher.service
```

To view the status of the service:

```console
sudo systemctl status ais-catcher.service
```

To ensure AIS-catcher starts automatically at boot time, enable the service with:

```console
sudo systemctl enable ais-catcher.service
```
