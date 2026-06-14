# Visual Web Control for Remote Configuration

This guide is for users who have installed **AIS-catcher-control** (available for Docker and Raspberry Pi installations), which provides the Visual Web Control interface for remote configuration and management.

> The input configuration for AIS-catcher is quite flexible and allows for some complex configuration. This is not fully embedded in the UI in first instance. Therefore, the menus only work with our starting config JSON or any version amended by 
> the UI. Once, the configuration files are manually edited, certain functionality will not be available.
>
> You can still set the settings in the Advanced section of the Visual Web Control interface by editing the parameters there. Also controlling the process (viewing the log and starting and stopping) is available. 


## Accessing the Visual Web Control Interface


Open your web browser and navigate to your Raspberry Pi's IP address on port **8110**. For example:
```
http://zerowh:8110
```

![image](https://github.com/user-attachments/assets/1fe942d2-dd3a-4116-99e8-f88f2de4ed14)


When you first access the interface, log in using the default credentials:

-  **Username**: admin
-  **Password**: admin

You'll be prompted to change this password immediately for security reasons.

![image](https://github.com/user-attachments/assets/aea1eb3b-0344-47a9-8b4f-8ddd77ecdeb0)


### Sidebar layout

Once logged in, the Visual Web Control sidebar gives you access to the following sections:

- **Control** — start/stop the AIS-catcher service and watch the live log stream.
- **Webviewer** — opens the local AIS web viewer in a new tab.
- **System** — host info, service status, automatic update checks for both AIS-catcher and the Control panel itself, watchdog status, and system actions (install / update / reboot).
- **General** — global settings (station name, coordinates, sharing toggle, language, etc.).
- **Device** — input device selection and SDR settings.
- **Output** — sub-pages: Community, UDP, TCP Client, TCP Servers, Webviewer, HTTP, MQTT.
- **Data Flow** — visualise and route messages between receivers and outputs via **zones**.
- **Advanced** — direct JSON / command-line editors (`config.json`, `config.cmd`) with **Check** and **Format** buttons that validate the document before save.
- **Change Password** and **Logout**.

### Input Device Selection

Navigate to the **Device** section to select your input device. You can choose from connected devices or manually specify a device type and serial number. If you have only a single SDR device connected, you can leave the device selection as **None**, and AIS-catcher will automatically detect and use the available device. Click the search icon to let AIS-catcher detect available SDR hardware.

![image](https://github.com/user-attachments/assets/83cc4f88-7d76-49db-b126-e62a2b652663)

Specific device settings for your SDR or other input device can be set on this page as well. For SDR inputs (RTL-SDR, AirSpy, AirSpy HF+, HackRF, HydraSDR) two extra fields appear below the device selector:

- **Channel** (`AB` or `CD`) — choose between the standard AIS channel pair (161.975 / 162.025 MHz) or the long-range channels.
- **High Sensitivity** — toggles the higher-sensitivity ("Challenger") decoder model. Trades CPU for a few percent more decoded messages. Equivalent to the `sensitivity_high` setting documented in [Model Settings](../configuration/model.md).


> **Note: After modifying any settings, remember to save the changes and restart AIS-catcher in the Control section for them to take effect.**
    
### Output Settings

AIS-catcher allows you to share your data with the [aiscatcher.org](https://aiscatcher.org) community. To enable this feature, go to **Output > Community**. By default, sharing is anonymous and enabled, but you can generate and enter a sharing key to associate the data with your station and view statistics. Click **Create** to set up a station on aiscatcher.org and receive your sharing key. Here you can also opt not to share your feed with the community.

![image](https://github.com/user-attachments/assets/9f032bea-784f-465a-93f4-003a5fd7f587)

#### Local Webviewer

Under **Output > Webviewer**, you can configure the local web viewer. Activate the viewer and enter your station details, including a name and your geographical coordinates.

Useful per-viewer toggles available here:

- **Use GPS** — feed the station position from a connected GPS source instead of a fixed coordinate pair.
- **Ship Timeout** (`history` setting, in seconds) — how long vessels stay visible after their last message (5 – 43200 s).
- **Backup** (in minutes) — how often the in-memory database is written to disk so state survives restarts.
- **Web Control Link** (`webcontrol_http`) — URL used by the viewer to surface a "Manage station" link back to this Control panel.

The local web viewer is accessible from your Raspberry Pi (e.g., on port **8100**, accessed via http://zerowh:8100) and is not accessible outside your local network by default. Some users choose to share their web viewer externally; see examples [here](https://aiscatcher.org/dashboards).

> Note: For a public page showcasing your station's performance, the easiest method is to feed data to aiscatcher.org using a sharing key.

### Data Flow and Zones

The **Data Flow** section visualises which receivers feed which outputs and lets you configure **zones** — named groupings used to tailor message routing per output channel. Zones are also referenced from the command line by the `sharing_zone` setting and from JSON configuration via the top-level `zones` array.

### System actions

The **System** section shows host information (load, memory, disk, AIS-catcher and Control versions) and lets you:

- check for updates of both AIS-catcher and AIS-catcher-control;
- start the update / install scripts and watch their progress live;
- reboot the host or reset a failed service;
- inspect the optional reboot watchdog status (enabled via the install script).

### Advanced editor

For configurations that can no longer be edited through the forms, **Advanced > Edit Config.json** and **Edit Config.cmd** expose the raw files. Both editors now include **Check** (validate JSON / command syntax) and **Format** (pretty-print) buttons to catch typos before you save. The Check & Format pipeline also migrates older config layouts and normalises types on the fly.

### Service Control
Navigate to **Control** to manage the AIS-catcher service:

- **Start/Stop** the service.
- Enable **Auto-Start** functionality.
- Monitor the service status through the live log stream (colour-coded by level: error, warning, notice, info, debug).
    
![image](https://github.com/user-attachments/assets/abf29893-0567-4b94-9354-e0630cc6f9fc)


## Accessing the AIS Web Viewer

After starting the service in the Control section and ensuring it runs without errors (check the log), you can view your received AIS data through the local web viewer. Access it by navigating to your Raspberry Pi's IP address on port **8100**:
```
http://zerowh:8100
```
The viewer provides a real-time display of AIS messages and vessel positions, allowing you to verify that your setup is working correctly. You can also quickly access it by selecting the Webviewer menu item.

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
