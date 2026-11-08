# How Manual Mode Works

In manual mode, AIS-catcher does exactly what you tell it when you start it: on the command line, or in a configuration file. There is no dashboard and nothing changes while it runs. To change a setting, stop AIS-catcher, change the command or the file, and start it again.

## A first run

```bash
AIS-catcher -v 10
```

That is a complete AIS receiver. AIS-catcher starts the first receiver it finds, shows each message on the screen, and prints statistics every 10 seconds.

## Command line or configuration file

Both hold the same settings, so pick the one that suits the job:

- **[Command line](cli.md)**: quick to type and to try. Good for a first run and for experiments.
- **[Configuration file](json-configuration.md)**: one JSON file, loaded with `-C`. Good for a station that runs for months, for several receivers, and for keeping your settings in one place.

To move from one to the other, let AIS-catcher write the file:

```bash
AIS-catcher -gr tuner auto -u 192.168.1.20 10110 -J config.json
AIS-catcher -C config.json
```

`-J` writes the command line as a configuration file instead of running it, and `-C` runs the file.

## Where to go next

- [Command Line](cli.md): how a command line is built, and every switch.
- [Configuration File](json-configuration.md): how the file is laid out.
- [Running as a Service](service.md): start AIS-catcher at boot on Linux and the Raspberry Pi.
- The reference: every setting of the [inputs](../configuration/input/overview.md), the [decoding](../configuration/model.md) and the [outputs](../configuration/output/overview.md).

Set up from the dashboard in your browser instead? That is managed mode: see [the dashboard](../managed/dashboard.md).
