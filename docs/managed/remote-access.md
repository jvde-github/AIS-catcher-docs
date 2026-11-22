# Remote Access and Security

Started with `127.0.0.1`, as on Windows, on macOS and in Docker in the [Quick Start](../getting-started/overview.md), the dashboard is only reachable from the machine AIS-catcher runs on. The Raspberry Pi and Linux install binds to all interfaces, so there it is open to your network from the start. To do the same by hand:

```console
AIS-catcher -E /etc/AIS-catcher/config.json 0.0.0.0:8118
```

When bound to anything other than `127.0.0.1`/`localhost`, a **password is required**. There is no default password: on the first visit the dashboard asks you to choose one, together with a **setup code**, and every later session requires logging in. The setup code is eight letters and digits that AIS-catcher writes to its log when it starts:

```console
Control: to set the password, use setup code XXXXXXXX
```

The Raspberry Pi and Linux installer shows it when it finishes. For the service, `journalctl -u ais-catcher | grep 'setup code'` finds it later. Only someone who can read the machine's log has the code, so a stranger on the network cannot set the password first.

On `127.0.0.1` or `localhost` the first visit also asks you to choose a password, but without a setup code, and the computer itself is never asked to log in. The password counts once the dashboard is open to the network.

<!-- TODO screenshot: install-password.webp — the set-a-password screen on first access -->

!!! warning
    The dashboard is intended for use on your local network. If you want to expose your station's data publicly, do not expose the dashboard — share your data via the [community feed](../configuration/output/community-feed.md) or add a [web viewer](output.md#maps-home-assistant-and-webhooks) instead.

## HTTPS for the dashboard

The password travels over this connection, so give the dashboard HTTPS when it is reached over a network. You need a certificate as PEM files without a passphrase, readable by the service's user.

- **In the dashboard:** Settings → System → Access. Enter the two files, which must be in the configuration's folder, and press *Apply HTTPS*. The files are checked first, the dashboard moves to `https://` at once and asks for the password again. Leave both empty to go back to plain HTTP.
- **On the command line:** for that run only, not saved in the file.

    ```console
    AIS-catcher -E /etc/AIS-catcher/aiscatcher.json 0.0.0.0:8118 TLS_CERT fullchain.pem TLS_KEY privkey.pem
    ```

- **In the configuration file:** `"control": { "tls": { "cert": "fullchain.pem", "key": "privkey.pem" } }`.

A renewed certificate is taken within a minute. The dashboard answers on one scheme only and never falls back to HTTP. If the files stop loading, the Access page says why; if they do not load at start, AIS-catcher stops with the reason in the log until they are fixed, or `tls` is taken out of the file. The map's own port has its own HTTPS setting, under Services.
