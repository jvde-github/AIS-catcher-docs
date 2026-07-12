# Remote Access and Security

By default the dashboard is only reachable from the machine AIS-catcher runs on (`127.0.0.1`). To administer it from another machine on your network, bind to all interfaces:

```console
AIS-catcher -E /etc/AIS-catcher/config.json 0.0.0.0:8118
```

When bound to anything other than `127.0.0.1`/`localhost`, a **password is required**: on first access the dashboard asks you to set one, and every subsequent session requires logging in.

<!-- TODO screenshot: install-password.webp — the set-a-password screen on first access -->

!!! warning
    The dashboard is intended for use on your local network. If you want to expose your station's data publicly, do not expose the dashboard — share your data via the [community feed](../configuration/output/community-feed.md) or add a [web viewer](output.md#web-viewer) instead.
