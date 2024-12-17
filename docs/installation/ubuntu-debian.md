#  Ubuntu/Debian/Raspberry Pi Installation

--8<-- "docs/disclaimer.md"

## Installation


This guide provides instructions for installing AIS-catcher on Debian-based systems (like Raspberry Pi) and setting it up to run as a background service. The background service provides the option for AIS-catcher to automatically start when the machine is booted.

>  Basic Installation via the below script is  required as a first step if you want to install the Web GUI package.

## Basic Installation

To install AIS-catcher via a script, open a terminal or log in via SSH, then run the following command:
```console
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install)"
```
The script will install all dependencies and build AIS-catcher. The required SDR libraries are installed from the official packages if they cannot be found on the system. For the RTL-SDR we build from source from the official package to guarantee support for the RTL-SDR V4 but, again, only if the package is not already installed on the system. On a fresh Raspberry Pi4 this will take less than 20 minutes. 

To update AIS-catcher to the latest version, simply run the above command again. To additionally install the Web GUI, see [below](#installation-with-web-gui). The Web GUI allows you to control the AIS-catcher process (start and stop) and set the configuration remotely via a convenient Web GUI.

---

[Start First Run](../usage/cli.md){ .md-button .md-button--primary }
[Install Web GUI](#installation-with-web-gui){ .md-button .md-button--secondary }

---

### Using pre-build Debian packages

If you want to use pre-installed Debian packages in the installation use:
```console
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install)" _ -p
```
The advantage that this avoids an compilation step which can save quite a bit of time on older Raspberry devices but it ***is not compatible with*** the first versions of the Raspberry Pi and Zero due to limnited support for floating point hardware acceleration. The pre-build packages also do not include PostgreSQL support.

### Testing the installation

Once the program is installed it can be run on the command line and checked for the features that are included in the build:
```console
AIS-catcher -L
```

More information to [get started](../usage/cli.md) is available. The installation script also sets up the infrastructure to run AIS-catcher as a systemd background service automatically on start up. 

## Configuration Files for backrgound service

For running AIS-catcher as a background service we can use two configuration files:

- /etc/AIS-catcher/config.json (JSON configuration)
- /etc/AIS-catcher/config.cmd (command line parameters)

The simplest approach is to edit the configuration file /etc/AIS-catcher/config.cmd to capture your settings which are detailed below. Lines starting with # are considered comments and ignored. The default file contains comments for popular options, which can be modified using a text editor, for example:
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

> The input configuration for AIS-catcher is quite flexible and allows for some complex configuration. This is not fully embedded in the UI in first instance. Therefore, the menus only work with our starting config JSON or any version amended by 
> the UI. Once, the configuration files are manually edited, certain functionality will not be available.
>
> You can still set the settings in the Advanced section of the Web UI by editing the parameters there. Also controlling the process (viewing the log and starting and stopping) is availaible. 

---

[Start First Run](../usage/gui.md){ .md-button .md-button--primary }

---

![image](https://github.com/user-attachments/assets/1fe942d2-dd3a-4116-99e8-f88f2de4ed14)


### Feedback
This is fairly new script and under development so any feedback is appreciated. 

![image](https://github.com/user-attachments/assets/1be6abdb-7df2-4f4b-8d73-1740e0476013)
