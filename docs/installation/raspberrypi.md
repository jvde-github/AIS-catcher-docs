#  Ubuntu/Debian/Raspberry Pi Installation

--8<-- "docs/disclaimer.md"

## Installation

This guide provides instructions for installing AIS-catcher on Debian-based systems (like Raspberry Pi) and setting it up to run as a background service. The background service provides the option for AIS-catcher to automatically start when the machine is booted.

### Recommended Installation Path for New Users

If you are new to Linux or Raspberry Pi, we recommend installing AIS-catcher with the **Visual Web Control interface**. This allows you to visually configure all settings without needing to edit configuration files manually.

👉 **Follow the complete installation guide here:** [Installation with Visual Web Control](#installation-with-visual-web-control)

## Basic Installation

To install AIS-catcher via a script, open a terminal or log in via SSH, then run the following command:
```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -p"
```

The script will install all dependencies and install AIS-catcher. If `curl` is not available on your device install it with `sudo apt install curl`. The required SDR libraries are installed from the official packages, if they cannot be found on the system. This script will install AIS-catcher from the latest available Debian package on Github. To guarantee support for the RTL-SDR V4 the latest version of the Osmocom library is statically linked into the AIS-catcher executable.

> This script ***is not compatible with*** the first versions of the Raspberry Pi and Zero due to their limited support for floating point hardware acceleration.
> The pre-build packages also do not include PostgreSQL support. If this is required, please build from [source](#install-from-source).

To additionally install the Visual Web Control interface, see [below](#installation-with-visual-web-control). The Visual Web Control allows you to control the AIS-catcher process (start and stop) and set the configuration remotely via a convenient web interface.

---

[Start First Run](../usage/cli.md){ .md-button .md-button--primary }
[Install Visual Web Control](#installation-with-visual-web-control){ .md-button .md-button--secondary }

---

### Update AIS-catcher to latest version

After you have installed with the above script, 
to update AIS-catcher to the latest version, simply run the above command again. It will ***not*** overwrite any configuration files when there are available on the system.

### Install From Source

If you want to install from source, you can run the script as follows:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install)" 
```
The advantage of building from source is that the executable is optimized for the hardware specifics but can take a significant amount of time (20 minutes on a Raspberry Pi 4).


### Testing the installation

Once the program is installed it can be run on the command line and checked for the features that are included in the build:
```console
AIS-catcher -L
```

More information to [get started](../usage/cli.md) is available. The installation script also sets up the infrastructure to run AIS-catcher as a systemd background service automatically on start up. 

## Configuration Files for background service

> **Tip:** If you're using the [Visual Web Control interface](#installation-with-visual-web-control), you can configure all settings through the web browser without manually editing these files.

For running AIS-catcher as a background service we can use two configuration files:

- /etc/AIS-catcher/config.json (JSON configuration)
- /etc/AIS-catcher/config.cmd (command line parameters)

The simplest approach is to edit the configuration file /etc/AIS-catcher/config.cmd to capture your settings which are detailed below. Lines starting with # are considered comments and ignored. The default file can be modified using a text editor, for example:
```console
sudo nano /etc/AIS-catcher/config.cmd
```
Please note that config.json takes precedence over config.cmd.

### Running AIS-catcher as a Background Service

> **Note:** If you're using the [Visual Web Control interface](#installation-with-visual-web-control), service management (start, stop, enable) is handled through the web interface. The commands below are only needed for manual command-line configuration.

To start AIS-catcher as a background service use the following command:
```console
sudo systemctl start ais-catcher.service
```
To view the status of the service copy the following command:
```console
sudo systemctl status ais-catcher.service
```
To ensure AIS-catcher starts automatically at boot time, enable the service with:
```console
sudo systemctl enable ais-catcher.service
```

## Installation with Visual Web Control

AIS-catcher provides a web-based visual control interface for easy configuration, which is **highly recommended for new users**. This two-step installation process will get you up and running with a visual interface to manage all settings, including updates and upgrades.

### Step 1: Install the Core AIS-catcher Package

First, install the basic AIS-catcher package. Open a terminal or log in via SSH, then run:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) -p"
```

The script will install all dependencies and AIS-catcher. If `curl` is not available, install it with `sudo apt install curl`.

### Step 2: Install the Visual Web Control Interface

Once the core package is installed, install the Visual Web Control interface as a separate service:

```bash
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher-control/main/install_ais_catcher_control.sh)"
```

### Step 3: Access the Visual Web Control Interface

After installation, open your web browser and navigate to your Raspberry Pi's IP address on port 8110. For example:
- `http://192.168.1.100:8110` (replace with your Pi's actual IP address)
- `http://raspberrypi.local:8110` (if using hostname)
- `http://zerowh:8110` (if you've set a custom hostname)

With the Visual Web Control interface, you can manage everything through your browser without needing to use command-line tools:
- Configure all AIS-catcher settings visually
- Start, stop, and monitor the AIS-catcher service (no need for systemctl commands)
- **Update and upgrade AIS-catcher** to the latest version with one click
- View logs and system status

> **Note:** Once you manually edit the AIS-catcher configuration files, certain simplified Visual Web Control features (such as one-click or wizard-like configuration menus) will no longer be available. However, you can still configure advanced settings via the Visual Web Control interface and manage AIS-catcher by viewing logs or starting and stopping the service.

---

[Start First Run](../usage/gui.md){ .md-button .md-button--primary }

---

![image](https://github.com/user-attachments/assets/1fe942d2-dd3a-4116-99e8-f88f2de4ed14)


### Feedback
This is fairly new script and under development so any feedback is appreciated. 

![image](https://github.com/user-attachments/assets/1be6abdb-7df2-4f4b-8d73-1740e0476013)
