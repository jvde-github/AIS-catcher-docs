# Web GUI for Remote Configuration

This section is for Rdevices that have AIS-catcher-control installed (Docker/Raspberry only).

## Configuring AIS-catcher via the Web GUI


To access it, open your web browser and navigate to your Raspberry Pi's IP address on port 8110 (for example, `http://zerowh:8110`). 

![image](https://github.com/user-attachments/assets/1fe942d2-dd3a-4116-99e8-f88f2de4ed14)


When you first access the interface, use the default credentials (username: `admin`, password: `admin`). You'll be prompted to change this password immediately for security purposes.

![image](https://github.com/user-attachments/assets/aea1eb3b-0344-47a9-8b4f-8ddd77ecdeb0)


### Input Device Selection

In the Input section of the web GUI, you'll need to select your input device. The interface allows you to select from any connected devices or manually specify a device type and serial number. If you're using a single SDR device, you can leave the device selection as 'None', and AIS-catcher will automatically use the available device. You can also click the Search Icon to let AIS-catcher detect the available SDR hardware.

![image](https://github.com/user-attachments/assets/83cc4f88-7d76-49db-b126-e62a2b652663)

Specific device settings for your SDR or other input device can be set on this page as well. 

> **Note:** After any modification to the settings the changes need to be saved and the program needs to be (re)started for the changes to become effective.
> 
### Output Settings

AIS-catcher offers the ability to share your data with the aiscatcher.org community. Navigate to the Output > Community section to enable this feature. By default, sharing is anonymous, but you can generate and enter a sharing key to associate the data with your station and view statistics. If you want to create a sharing key click "Create" and this will take you to the page on aiscatcher.org where you can set up a station and receive a sharing key.

![image](https://github.com/user-attachments/assets/9f032bea-784f-465a-93f4-003a5fd7f587)

#### Local Webviewer

The local web viewer configuration can be found under Output > Web Viewer. Here, you should activate the viewer and enter your station details, including a name and your geographical coordinates.

This local webviewer is available from your Raspberry device (e.g. in this example at port 8100, hence can be accessed with `http://zerowh:8100` in the browser) and not by default accessible outside the local network. Some users share their webviewer externally, see [here](https://aiscatcher.org/dashboards) for examples. 

> **Note:** If you desire a public page with your station performance the easiest approach is to feed aiscatcher.org with a sharing key.

### Service Control

The Control section is where you manage the AIS-catcher service. Here you can start and stop the service, enable auto-start functionality, and monitor the service status through the log display. 
![image](https://github.com/user-attachments/assets/abf29893-0567-4b94-9354-e0630cc6f9fc)


## Accessing the AIS Web Viewer

Press start in the Control section and ensure that it is running without errors (see the log). Once AIS-catcher is running, you can view your received AIS data through the aforementioned local web viewer. Access it by navigating to your Raspberry Pi's IP address on port 8100 (for example, `http://zerowh:8100`). The viewer provides a real-time display of AIS messages and vessel positions, allowing you to verify that your setup is working correctly. Another option is to have a quick view by choosing the Webviewer menu item in the menu.

![image](https://github.com/user-attachments/assets/1762ee88-e8b0-47a3-b50a-1ca2a7b42acb)

## Conclusion

With these steps completed, you now have a fully functional AIS receiving station running on your Raspberry Pi. The system will receive AIS messages from nearby vessels and, if configured, share this data with the AIScatcher.org community. You can monitor vessel traffic in real-time through the web viewer interface.

For advanced users who want to fine-tune their setup, AIS-catcher provides two configuration files:

The JSON configuration file at:
```bash
/etc/AIS-catcher/config.json
```

And the command-line parameters file at:
```bash
/etc/AIS-catcher/config.cmd
```

> **Note:** The GUI script can also be run for existing installations that are based on the AIS-catcher install script. But once configuration files are manually edited they cannot be edited via the HTML forms anymore. The configuration files still can be edited though under the advanced options menu. 