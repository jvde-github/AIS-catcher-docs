# Docker

Container images are on the GitHub Container Registry: `edge` is the latest build of the `main` branch, `latest` the latest release. See the [package page](https://github.com/jvde-github/AIS-catcher/pkgs/container/ais-catcher) for all tags. The images do not support SDRplay devices.

## Managed mode

```console
docker run --rm -it --network=host --device-cgroup-rule='c 189:* rmw' -v /dev/bus/usb:/dev/bus/usb -v ais-config:/config ghcr.io/jvde-github/ais-catcher:edge -E /config/config.json 127.0.0.1:8118
```

- `--device-cgroup-rule` and `-v /dev/bus/usb` pass USB receivers through to the container, and keep them working when one is plugged in again.
- With a dAISy-catcher or another serial receiver, add `--device /dev/ttyACM0` instead.
- The settings live in the `ais-config` volume, so they survive a restart.
- To open the dashboard from another computer, replace `127.0.0.1` with `0.0.0.0`. It then asks for a password.

Then open the dashboard in your browser, as in the [Quick Start](../getting-started/overview.md#open-the-dashboard).

## Manual mode

Run the container with your AIS-catcher options at the end:

```console
docker run --rm -it --pull always --device /dev/bus/usb ghcr.io/jvde-github/ais-catcher:latest <options>
```

For the web viewer (`-N 8100`), make its port available with `-p 8100:8100`, or use `--network=host`. See [Manual Mode](../usage/overview.md).

!!! tip "docker-shipfeeder"
    To feed aggregators, [docker-shipfeeder](https://github.com/sdr-enthusiasts/docker-shipfeeder) from the sdr-enthusiasts community runs AIS-catcher in manual mode, with its own documentation and support.

## Updating

Pull the image again:

```console
docker pull ghcr.io/jvde-github/ais-catcher:edge
```
