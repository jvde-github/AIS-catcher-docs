# Docker Container

--8<-- "docs/disclaimer.md"

Jump to the desired Installation Option:

[Basic](#basic-docker-container){ .md-button .md-button--secondary }
[Visual Web Control](#docker-with-visual-web-control){ .md-button .md-button--secondary }

## Basic Docker Container

Pre-built container images containing AIS-catcher are available from the GitHub Container Registry. Available container tags are documented on the [package's page](https://github.com/jvde-github/AIS-catcher/pkgs/container/ais-catcher), with `latest` (the latest release) and `edge` (the bleeding edge of the `main` branch) being the two main ones.

The following `docker run` command provides an example of the usage of this container image, running the latest release of AIS-catcher interactively:

```console
docker run --rm -it --pull always --device /dev/bus/usb ghcr.io/jvde-github/ais-catcher:latest <ais-catcher command line options>
```

Alternatively, the following `docker-compose.yml` configuration provides a good starting point should you wish to use [Docker Compose](https://docs.docker.com/compose/):

```yaml
services:
  ais-catcher:
    command: <ais-catcher command line options> (e.g. -N 8100)
    container_name: ais-catcher
    ports:
      - 8100:8100 <don't forget to passthrough ports for the webclient>
    devices:
      - "/dev/bus/usb:/dev/bus/usb"
    image: ghcr.io/jvde-github/ais-catcher:latest
    restart: always
```
Please note that the SDRplay devices are currently not supported in the Docker images.

---

[Start First Run](../usage/cli.md){ .md-button .md-button--primary }

---

### More options
To pull the latest docker image (e.g. to create or refresh to the latest version) without running:
```console
docker pull ghcr.io/jvde-github/ais-catcher:edge
```
To start AIS-catcher, you can then use:
```console
docker run --device /dev/bus/usb --rm -it ghcr.io/jvde-github/ais-catcher:edge
```
Notice that if you want to run the webviewer (-N 8100) you need to make that available on the host system with (`-p 8100:8100`). To send UDP data to OpenCPN running on the host computer, you can try to find the bridge network address (`sudo docker network inspect bridge` as per [tutorials](https://www.geeksforgeeks.org/how-to-use-docker-default-bridge-networking/) and use this as UDP destination address (e.g. `-u 172.17.0.1  5077`). Alternatively you could use `--network host` although less desirable. Please consult the Docker documentation.

An excellent Docker set-up is the [docker-shipfeeder](https://github.com/sdr-enthusiasts/docker-shipfeeder) that provides a user friendly way to 
feed various aggregators with excellent documentation and user support by the sdrenthusiasts community.

## Docker with Visual Web Control
If you are already up and running with Docker installed, you can simply use:
```console
wget https://raw.githubusercontent.com/jvde-github/AIS-catcher-control/refs/heads/main/docker-compose.yml
docker compose up -d
```

This will set up AIS-catcher with the Visual Web Control interface, allowing you to configure, manage, and update your installation via a web browser at port 8110.

---

[Start First Run](../usage/gui.md){ .md-button .md-button--primary }

---
