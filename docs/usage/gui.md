# Web GUI for Remote Configuration

This guide is for users who have installed **AIS-catcher-control** (available for Docker and Raspberry Pi installations), which provides the Web GUI for remote configuration and management.

> The input configuration for AIS-catcher is quite flexible and allows for some complex configuration. This is not fully embedded in the UI in first instance. Therefore, the menus only work with our starting config JSON or any version amended by 
> the UI. Once, the configuration files are manually edited, certain functionality will not be available.
>
> You can still set the settings in the Advanced section of the Web UI by editing the parameters there. Also controlling the process (viewing the log and starting and stopping) is availaible. 


## Accessing the Web GUI


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


### Input Device Selection

Navigate to the **Input** section to select your input device. You can choose from connected devices or manually specify a device type and serial number. If you have only a single SDR device connected, you can leave the device selection as **None**, and AIS-catcher will automatically detect and use the available device. Click the search icon to let AIS-catcher detect available SDR hardware.

![image](https://github.com/user-attachments/assets/83cc4f88-7d76-49db-b126-e62a2b652663)

Specific device settings for your SDR or other input device can be set on this page as well. 


> **Note: After modifying any settings, remember to save the changes and restart AIS-catcher in the Control section for them to take effect.**
    
### Output Settings

AIS-catcher allows you to share your data with the [aiscatcher.org](https://aiscatcher.org) community. To enable this feature, go to **Output > Community**. By default, sharing is anonymous and enabled, but you can generate and enter a sharing key to associate the data with your station and view statistics. Click **Create** to set up a station on aiscatcher.org and receive your sharing key. Here you can also opt not to share your feed with the community.

![image](https://github.com/user-attachments/assets/9f032bea-784f-465a-93f4-003a5fd7f587)

#### Local Webviewer

Under **Output > Web Viewer**, you can configure the local web viewer. Activate the viewer and enter your station details, including a name and your geographical coordinates.

The local web viewer is accessible from your Raspberry Pi (e.g., on port **8100**, accessed via http://zerowh:8100) and is not accessible outside your local network by default. Some users choose to share their web viewer externally; see examples [here](https://aiscatcher.org/dashboards).

> Note: For a public page showcasing your station's performance, the easiest method is to feed data to aiscatcher.org using a sharing key.

### Service Control
Navigate to **Control** to manage the AIS-catcher service:

- **Start/Stop** the service.
- Enable **Auto-Start** functionality.
- Monitor the service status through the log display.
    
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
