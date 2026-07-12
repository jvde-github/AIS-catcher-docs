# AIS-catcher-control

**AIS-catcher-control** is a separate package for Raspberry Pi and Debian-based systems that starts and stops the AIS-catcher process and manages the host from the browser. Configuration of the receiver itself is done in AIS-catcher's own [dashboard](../managed/dashboard.md) — AIS-catcher-control is the tool around it: service control, one-click updates and reboot.

!!! note
    Earlier versions of AIS-catcher-control included full configuration menus (device, outputs, data flow). This functionality has been superseded by [managed mode](../managed/dashboard.md); AIS-catcher-control now focuses on controlling the process and the host. On other platforms the process is managed with the native tools instead — e.g. Docker containers via Docker itself.

## Installation

First install AIS-catcher itself via the [install script](../installation/raspberrypi.md), then install AIS-catcher-control as a separate service:

```console
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher-control/main/install_ais_catcher_control.sh)"
```

## Accessing the Interface

Open your web browser and navigate to the machine's address on port **8110**, for example:

```
http://raspberrypi.local:8110
```

Log in with the password — you will be asked to set one on first access.

## Controlling the Service

Navigate to **Control** to manage the AIS-catcher service:

- **Start/Stop** the service.
- Enable **Auto-Start** functionality.
- Monitor the service status through the live log stream (colour-coded by level: error, warning, notice, info, debug).

![image](https://github.com/user-attachments/assets/abf29893-0567-4b94-9354-e0630cc6f9fc)

## System Management

The **System** section shows host information (load, memory, disk, AIS-catcher and Control versions) and lets you:

- check for updates of both AIS-catcher and AIS-catcher-control;
- start the update / install scripts and watch their progress live;
- reboot the host or reset a failed service;
- inspect the optional reboot watchdog status (enabled via the install script).
