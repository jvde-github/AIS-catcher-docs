# Manual Mode

Managed mode is the default, not the only way to run AIS-catcher. Started with command-line options, AIS-catcher behaves as the classic command-line tool it has always been: it does exactly what you type, and the [dashboard](../managed/dashboard.md) and its configuration file are not in play.

```console
AIS-catcher -v 10
```

That is a complete AIS receiver — decoding starts immediately and NMEA messages appear on screen, with statistics every 10 seconds.

Manual mode is the right choice when you want to script or integrate AIS-catcher, run a minimal headless setup, build complex multi-receiver configurations, or simply prefer the command line.

There are two equivalent ways to express a configuration:

- [Command Line](cli.md) — every setting as a command-line switch. Start here for a first run and experimentation.
- [JSON Configuration](json-configuration.md) — the same settings in a JSON file, loaded with `-C`. Better for larger configurations that you want to keep under version control or deploy to multiple stations.

For unattended operation, see [Running as a Service](service.md).

Every setting is documented in the [Settings reference](../configuration/overview.md) with its command-line switch and JSON key side by side.
