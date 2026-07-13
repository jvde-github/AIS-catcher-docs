#  Ubuntu/Debian/Raspberry Pi Installation

!!! warning "Disclaimer"
    **AIS-catcher is intended for hobbyist and research projects only. It is NOT approved for use in navigation or safety-of-life applications.** [Read the full disclaimer](../disclaimer.md).

AIS-catcher is installed with a single script that installs all dependencies, sets up a background service and starts it. There are two ways to run your station:

- **[Managed mode](#managed-mode)** (recommended) — configure and control your station from the browser.
- **[Manual mode](#manual-mode)** — configure via the command line or configuration files.

<div class="recommended" markdown>

## Managed Mode

<div class="steps" markdown>

<div class="step" markdown>

**Run the install script**  
Open a terminal or log in via SSH, then run:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -p -M"
```

If `curl` is not available on your device, install it with `sudo apt install curl`.

!!! warning "Upgrading an existing install?"
    Switching from manual mode to managed mode starts with fresh settings: your existing configuration (`/etc/AIS-catcher/config.json` and `config.cmd`) is **not** carried over. The files themselves are left untouched, so you can refer to them when re-entering your settings via the setup wizard. Re-running the installer on an existing **managed** installation is just an update — your settings are kept.

</div>

<div class="step" markdown>

**Complete the setup wizard**  
Open the dashboard in your browser on port **8118**, e.g. `http://localhost:8118`{ .address }. On first use, the setup wizard walks you through configuring your input device and outputs, and starts the receiver:

[Setup Wizard](../managed/setup-wizard.md){ .md-button .md-button--primary }

</div>

</div>

That's it — your station is up and running. See [Getting Around the Dashboard](../managed/dashboard.md) to monitor and fine-tune it.

</div>

## Manual Mode

To configure via the command line instead, omit the `-M` option:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -p"
```

The background service infrastructure is still set up — see [Running as a Service](../usage/service.md) for the configuration files and service commands.

[Command Line Run](../usage/cli.md){ .md-button }

## Install from Source

Both commands above install the latest pre-built Debian package (the `-p` option). Leave out `-p` to build AIS-catcher from source instead:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -M"
```

Building from source optimizes the executable for your hardware but can take a significant amount of time (20 minutes on a Raspberry Pi 4). It is required if you need PostgreSQL support, which is not included in the pre-built packages.

!!! note
    The pre-built packages statically link the latest Osmocom library to guarantee support for the RTL-SDR V4, and are ***not compatible with*** the first versions of the Raspberry Pi and Zero due to their limited support for floating point hardware acceleration.

## Updating

To update AIS-catcher to the latest version, simply run the install command again. It will ***not*** overwrite any configuration files when these are available on the system.

## Remote Start/Stop and Host Management

The separate [AIS-catcher-control](../usage/gui.md) package adds browser-based control of the AIS-catcher process (start and stop, live log) and of the host itself (one-click updates, reboot). It is ***not*** included in the install above — install it with:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher-control/main/install_ais_catcher_control.sh)"
```
