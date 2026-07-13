# Docker Container

!!! warning "Disclaimer"
    **AIS-catcher is intended for hobbyist and research projects only. It is NOT approved for use in navigation or safety-of-life applications.** [Read the full disclaimer](../disclaimer.md).

Pre-built container images are available from the GitHub Container Registry, with `latest` (the latest release) and `edge` (the bleeding edge of the `main` branch) being the two main tags — see the [package's page](https://github.com/jvde-github/AIS-catcher/pkgs/container/ais-catcher) for all available tags. There are two ways to run your station:

- **[Managed mode](#managed-mode)** (recommended) — configure and control your station from the browser.
- **[Manual mode](#manual-mode)** — configure via command-line options.

!!! note
    SDRplay devices are currently not supported in the Docker images.

<div class="recommended" markdown>

## Managed Mode

<div class="steps" markdown>

<div class="step" markdown>

**Pull the image**  
With Docker installed:

```console
docker pull ghcr.io/jvde-github/ais-catcher:edge
```

</div>

<div class="step" markdown>

**Run it in managed mode**

```console
docker run --rm -it --network=host --device-cgroup-rule='c 189:* rmw' -v /dev/bus/usb:/dev/bus/usb -v ais-config:/config ghcr.io/jvde-github/ais-catcher:edge -E /config/config.json 127.0.0.1:8118
```

A quick tour of the options:

- `--device-cgroup-rule` and `-v /dev/bus/usb` pass USB SDRs through to the container, and keep working when a device is re-plugged.
- Using a dAISy-catcher or other serial receiver? Add `--device /dev/ttyACM0` instead.
- Your settings live in the `ais-config` volume (created automatically), so they persist across restarts.
- To administer the station from another machine, replace `127.0.0.1` with `0.0.0.0` — a password is then required.

</div>

<div class="step" markdown>

**Complete the setup wizard**  
Open the dashboard in your browser at `http://localhost:8118`{ .address }. On first use, the setup wizard walks you through configuring your input device and outputs, and starts the receiver:

[Setup Wizard](../managed/setup-wizard.md){ .md-button .md-button--primary }

</div>

</div>

That's it — your station is up and running. See [Getting Around the Dashboard](../managed/dashboard.md) to monitor and fine-tune it.

</div>

## Manual Mode

Run the container with any AIS-catcher command-line options:

```console
docker run --rm -it --pull always --device /dev/bus/usb ghcr.io/jvde-github/ais-catcher:latest <ais-catcher command line options>
```

Notice that if you want to run a web viewer (`-N 8100`) you need to make that port available on the host system with `-p 8100:8100`, or use `--network=host`.

[Command Line Run](../usage/cli.md){ .md-button }

!!! tip "docker-shipfeeder"
    For manual-mode setups focused on feeding aggregators, [docker-shipfeeder](https://github.com/sdr-enthusiasts/docker-shipfeeder) by the sdr-enthusiasts community is a user-friendly alternative with excellent documentation and support. Note that it runs AIS-catcher in manual mode and does not offer the managed-mode dashboard.

## Updating

To update to the latest image, simply pull it again:

```console
docker pull ghcr.io/jvde-github/ais-catcher:edge
```
