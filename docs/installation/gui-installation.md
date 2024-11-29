# GUI Installation

This section describes setting up the GUI for Raspberry Pi devices.

## Configuring via the Web GUI

AIS-catcher provides a web-based graphical user interface for easy configuration. It needs to be installed as a separate service by entering in the terminal:
```bash
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/jvde-github/AIS-catcher-control/main/install_ais_catcher_control.sh)"
```
To access it, open your web browser and navigate to your Raspberry Pi's IP address on port 8110 (for example, `http://zerowh:8110`). 

![image](https://github.com/user-attachments/assets/1fe942d2-dd3a-4116-99e8-f88f2de4ed14)


When you first access the interface, use the default credentials (username: `admin`, password: `admin`). You'll be prompted to change this password immediately for security purposes.

![image](https://github.com/user-attachments/assets/aea1eb3b-0344-47a9-8b4f-8ddd77ecdeb0)
