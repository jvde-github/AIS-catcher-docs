# Remote Access and Security

By default the dashboard is only reachable from the machine AIS-catcher runs on (`127.0.0.1`). To administer it from another machine on your network, bind to all interfaces:

```console
AIS-catcher -E /etc/AIS-catcher/config.json 0.0.0.0:8118
```

When bound to anything other than `127.0.0.1`/`localhost`, a **password is required**: on first access the dashboard asks you to set one, and every subsequent session requires logging in.

<!-- TODO screenshot: install-password.webp — the set-a-password screen on first access -->

!!! warning
    The dashboard is intended for use on your local network. If you want to expose your station's data publicly, do not expose the dashboard — share your data via the [community feed](../configuration/output/community-feed.md) or add a [web viewer](output.md#web-viewer) instead.

## HTTPS for the dashboard

The password travels over this connection, so give the dashboard HTTPS when it is reached over a network. You need a certificate as PEM files without a passphrase, readable by the service's user.

- **In the dashboard:** Settings → System → Access. Enter the two files, which must be in the configuration's folder, and press *Apply HTTPS*. The files are checked first, the dashboard moves to `https://` at once and asks for the password again. Leave both empty to go back to plain HTTP.
- **On the command line:** for that run only, not saved in the file.

    ```console
    AIS-catcher -E /etc/AIS-catcher/aiscatcher.json 0.0.0.0:8118 TLS_CERT fullchain.pem TLS_KEY privkey.pem
    ```

- **In the configuration file:** `"control": { "tls": { "cert": "fullchain.pem", "key": "privkey.pem" } }`.

A renewed certificate is taken within a minute. The dashboard answers on one scheme only and never falls back to HTTP. If the files stop loading, the Access page says why; if they do not load at start, AIS-catcher stops with the reason in the log until they are fixed, or `tls` is taken out of the file. The map's own port has its own HTTPS setting, under Services.
