# Running as a Service

On Linux and the Raspberry Pi, the [install script](../installation/ubuntu-debian.md) without `-M` sets AIS-catcher up as a systemd service in manual mode. The service runs as the user `aiscatcher` and reads two files:

- `/etc/AIS-catcher/config.json`, a [configuration file](json-configuration.md).
- `/etc/AIS-catcher/config.cmd`, [command-line switches](cli.md), one or more per line. Lines starting with `#` are comments.

AIS-catcher reads `config.json` first, then the switches in `config.cmd`. Outputs in both files add up; a setting in both takes the value from `config.cmd`. Put your settings in whichever file you prefer:

```console
sudo nano /etc/AIS-catcher/config.cmd
```

## Start, stop and check

Restart the service after changing either file:

```console
sudo systemctl restart ais-catcher.service
```

| Command | What it does |
|---------|--------------|
| `sudo systemctl start ais-catcher.service` | Start it |
| `sudo systemctl stop ais-catcher.service` | Stop it |
| `sudo systemctl enable ais-catcher.service` | Start it at boot |
| `sudo systemctl disable ais-catcher.service` | Do not start it at boot |
| `systemctl status ais-catcher.service` | Show whether it runs |
| `journalctl -u ais-catcher.service -f` | Follow its log |
