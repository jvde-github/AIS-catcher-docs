#  Raspberry Pi Installation

## Disclaimer

...

## Installation


This guide provides instructions for installing AIS-catcher on Debian-based systems (like Raspberry Pi) and setting it up to run as a background service. This ensures AIS-catcher will automatically start when the machine is booted.
## Basic Installation

To install AIS-catcher via a script, open a terminal or log in via SSH, then run the following command:
```console
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install)"
```
The script will install all dependencies and build AIS-catcher. The required SDR libraries are installed from the official packages if they cannot be found on the system. For the RTL-SDR we build from source from the official package to guarantee support for the RTL-SDR V4 but, again, only if the package is not already installed on the system. On a fresh Raspberry Pi4 this will take less than 20 minutes. 

To update AIS-catcher to the latest version, simply run the above command again.

---

[Start First Run](../usage/cli.md){ .md-button .md-button--primary }

---

### Using pre-installed Debian packages

If you want to use pre-installed Debian packages in the installation use:
```console
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/jvde-github/AIS-catcher/main/scripts/aiscatcher-install)" _ -p
```
The advantage that this avoids an compilation step which can save quite a bit of time on older Raspberry devices but it does not optimize the binaries for the specific hardware and ***is not compatible with the RTL-SDR V4***.

## Installation with Web GUI 

AIS-catcher provides a web-based graphical user interface for easy configuration. It needs to be installed as a separate service by entering in the terminal:
```bash
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher-control/main/install_ais_catcher_control.sh)"
```
To access it, open your web browser and navigate to your Raspberry Pi's IP address on port 8110 (for example, `http://zerowh:8110`). 

---

[Start First Run](../usage/gui.md){ .md-button .md-button--primary }

---

![image](https://github.com/user-attachments/assets/1fe942d2-dd3a-4116-99e8-f88f2de4ed14)



## Configuration Files

For running AIS-catcher as a background service we can use two configuration files:

- /etc/AIS-catcher/config.json (JSON configuration)
- /etc/AIS-catcher/config.cmd (command line parameters)

The simplest approach is to edit the configuration file /etc/AIS-catcher/config.cmd to capture your settings which are detailed below. Lines starting with # are considered comments and ignored. The default file contains comments for popular options, which can be modified using a text editor, for example:
```console
sudo nano /etc/AIS-catcher/config.cmd
```

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
### Feedback
This is fairly new script and under development so any feedback is appreciated. 

![image](https://github.com/user-attachments/assets/1be6abdb-7df2-4f4b-8d73-1740e0476013)