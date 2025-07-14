#  Ubuntu/Debian/Raspberry Pi Installation

--8<-- "docs/disclaimer.md"

## Installation


This guide provides instructions for installing AIS-catcher on Debian-based systems (like Raspberry Pi) and setting it up to run as a background service. The background service provides the option for AIS-catcher to automatically start when the machine is booted.

>  Basic Installation via the below script is  required as a first step if you want to install the Web GUI package.

## Basic Installation

To install AIS-catcher via a script, open a terminal or log in via SSH, then run the following command:
```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install) _ -p"
```

The script will install all dependencies and install AIS-catcher. If `curl` is not available on your device install it with `sudo apt install curl`. The required SDR libraries are installed from the official packages, if they cannot be found on the system. This script will install AIS-catcher from the latest available Debian package on Github. To guarantee support for the RTL-SDR V4 the latest version of the Osmocom library is statically linked into the AIS-catcher executable.

> This script ***is not compatible with*** the first versions of the Raspberry Pi and Zero due to their limited support for floating point hardware acceleration.
> The pre-build packages also do not include PostgreSQL support. If this is required, please build from [source](#install-from-source).

To additionally install the Web GUI, see [below](#installation-with-web-gui). The Web GUI allows you to control the AIS-catcher process (start and stop) and set the configuration remotely via a convenient Web GUI.

---

[Start First Run](../usage/cli.md){ .md-button .md-button--primary }
[Install Web GUI](#installation-with-web-gui){ .md-button .md-button--secondary }

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

For running AIS-catcher as a background service we can use two configuration files:

- /etc/AIS-catcher/config.json (JSON configuration)
- /etc/AIS-catcher/config.cmd (command line parameters)

The simplest approach is to edit the configuration file /etc/AIS-catcher/config.cmd to capture your settings which are detailed below. Lines starting with # are considered comments and ignored. The default file can be modified using a text editor, for example:
```console
sudo nano /etc/AIS-catcher/config.cmd
```
Please note that config.json takes precedence over config.cmd.

### Running AIS-catcher as a Background Service

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

## Installation with Web GUI 

AIS-catcher provides a web-based graphical user interface for easy configuration. Ensure you have installed the basic [package](#basic-installation) first. It needs to be installed as a separate service by entering in the terminal:
```bash
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher-control/main/install_ais_catcher_control.sh)"
```
To access it, open your web browser and navigate to your Raspberry Pi's IP address on port 8110 (for example, `http://zerowh:8110`). 

> Please note that once you manually edit the AIS-catcher configuration files, certain simplified Web  UI features (such as one-click or wizard-like configuration menus) will no longer be available.  However, you can still configure advanced settings via the Web UI and manage AIS-catcher by viewing logs or starting and stopping the service.

---

[Start First Run](../usage/gui.md){ .md-button .md-button--primary }

---

![image](https://github.com/user-attachments/assets/1fe942d2-dd3a-4116-99e8-f88f2de4ed14)


### Feedback
This is fairly new script and under development so any feedback is appreciated. 

![image](https://github.com/user-attachments/assets/1be6abdb-7df2-4f4b-8d73-1740e0476013)
