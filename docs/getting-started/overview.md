---
hide:
  - toc
---

# Quick Start

From a receiver in its box to ships on your own map, in five steps. AIS-catcher runs in **managed mode**: it runs in the background, and you set it up in the dashboard in your browser. To run it with a configuration file or command-line options instead, see [Manual Mode](../usage/overview.md).

<div class="stepper" markdown>

<div class="stepper-step" markdown>

## Before you start

Have these ready:

<div class="ready" markdown>

**Computer** A Raspberry Pi, a PC or a Mac

**Receiver** An RTL-SDR dongle or a dAISy-catcher

**Antenna** A VHF antenna, tuned to 162 MHz

</div>

Not sure what to get? See [What you need](../what-you-need.md). Connect the antenna to the receiver, and the receiver to the computer.

</div>

<div class="stepper-step" markdown>

## Install AIS-catcher

Pick your computer:

=== "Raspberry Pi and Linux"

    One command installs AIS-catcher and what it needs, and runs it in managed mode as a service that starts at boot:

    ```console
    sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -p -M"
    ```

    It works on Raspberry Pi OS, Debian, Ubuntu and Fedora. See [Raspberry Pi and Linux](../installation/ubuntu-debian.md) for the details.

=== "Windows"

    1. Download the **Edge** build from the [downloads](../installation/windows.md#downloads) and unzip it.
    2. With an RTL-SDR, use [Zadig](https://www.rtl-sdr.com/tag/zadig/) to give it the WinUSB driver, once per dongle.
    3. Double-click `start-GUI.bat` in the unzipped folder.

=== "macOS"

    Build it with [Homebrew](https://brew.sh). This takes a few minutes:

    ```bash
    brew install git make gcc cmake pkg-config sqlite3 librtlsdr
    git clone https://github.com/jvde-github/AIS-catcher.git --depth 1
    cd AIS-catcher && mkdir build && cd build
    cmake .. && make && sudo make install
    ```

    Then start it in managed mode:

    ```bash
    AIS-catcher -E ~/aiscatcher.json 127.0.0.1:8118
    ```

    See [macOS](../installation/macos.md) for other receivers.

=== "Docker"

    ```console
    docker run --rm -it --network=host --device-cgroup-rule='c 189:* rmw' -v /dev/bus/usb:/dev/bus/usb -v ais-config:/config ghcr.io/jvde-github/ais-catcher:edge -E /config/config.json 127.0.0.1:8118
    ```

    The settings live in the `ais-config` volume, so they survive a restart. With a dAISy-catcher, add `--device /dev/ttyACM0`. See [Docker](../installation/docker.md).

Something else, such as Android? See [all installs](../installation/overview.md).

</div>

<div class="stepper-step" markdown>

## Open the dashboard

In your browser, open port 8118 of the computer that runs AIS-catcher:

- `http://localhost:8118`{ .address } on that computer itself,
- `http://raspberrypi.local:8118`{ .address }, or the computer's IP address, from another device.

From another device, AIS-catcher first asks you to set a password. On macOS and in Docker, the commands in the previous step only let the computer itself in: replace `127.0.0.1` with `0.0.0.0` to open the dashboard from elsewhere.

</div>

<div class="stepper-step" markdown>

## Run the setup wizard

The first time, a short wizard sets up the station. Every step can be skipped, and everything can be changed later under **Settings**.

1. **Welcome:** press **Get started**.
2. **Input Device:** pick your receiver. The wizard lists the SDRs it finds on the computer, the dAISy-catcher and other serial receivers.
3. **AIS-catcher Community:** to put your station on the community map, press **Create station on aiscatcher.org**, register it and paste the station key you get. Your station then gets a name, coverage statistics and its own page. Or press **Skip**.
4. **AISHub:** for the AISHub data exchange, if you are a member. Otherwise press **Skip**.
5. **Summary:** check it, keep **Start the receiver after saving** ticked, and press **Save & Close**.

![The setup wizard's summary](../assets/qs-w4-summary.webp){ width="560" }

</div>

<div class="stepper-step" markdown>

## See your ships

In an area with traffic, the first ships appear on the dashboard map within a few minutes. Names can take longer: ships send them less often than their position.

!!! question "No ships after a few minutes?"
    - Check that the antenna is connected, and that the station can see water with traffic.
    - Check that no other program uses the receiver.
    - See [Troubleshooting](../advanced/troubleshooting.md).

Where to go next:

- [Getting Around the Dashboard](../managed/dashboard.md): the map, the receiver controls and the settings.
- [Send Ships to Your Chart Plotter](../managed/chart-plotter.md).
- [Outputs](../managed/output.md): the community map, other programs and services.

</div>

</div>
