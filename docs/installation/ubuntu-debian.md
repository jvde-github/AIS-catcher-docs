# Raspberry Pi and Linux

One script installs AIS-catcher and what it needs, and sets it up as a service that starts at boot. It works on Raspberry Pi OS, Debian, Ubuntu and Fedora. If `curl` is missing, install it first with `sudo apt install curl` (or `sudo dnf install curl` on Fedora).

## Managed mode

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -p -M"
```

Then open the dashboard in your browser, as in the [Quick Start](../getting-started/overview.md#open-the-dashboard).

!!! warning "Coming from manual mode?"
    Managed mode starts with fresh settings: your `/etc/AIS-catcher/config.json` and `config.cmd` are not carried over. The files stay where they are, so you can look at them while you set up the station in the dashboard. Running the installer again on a managed station is an update, and keeps your settings.

## Manual mode

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -p"
```

The service then runs the settings in `/etc/AIS-catcher`. See [Running as a Service](../usage/service.md).

## Pre-built or from source

The `-p` option installs a pre-built package: a `.deb` on Debian, Ubuntu and Raspberry Pi OS, or an `.rpm` on Fedora 43 and 44 (`x86_64` and `aarch64`). Leave out `-p` to build AIS-catcher from source instead, for example in managed mode:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -M"
```

A build takes about 20 minutes on a Raspberry Pi 4, and is needed on other Fedora releases and for PostgreSQL support.

!!! note
    The pre-built packages do not run on the first Raspberry Pi and the first Pi Zero.

## Updating

Run the same install command again. Your settings are kept.

## AIS-catcher-control

[AIS-catcher-control](../usage/gui.md) is a separate tool to start and stop AIS-catcher, read its log, update it and reboot the computer from the browser. Install it with:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher-control/main/install_ais_catcher_control.sh)"
```
