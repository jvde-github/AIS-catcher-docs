# Getting Started

## What You’ll Need

Before getting started, ensure you have the following:

1. **Compatible Hardware Setup**:  
    A USB-based RTL-SDR device or another supported SDR receiver.
    An AIS antenna for optimal data reception.

2. **Computer or Server**:  
    Windows, Raspberry Pi, Linux, or OSX with basic command-line proficiency.

3. **Internet Connection**:    
    Essential for installation and accessing online resources.

4. **Line of Sight to Ships**:  
   Position yourself near water with active vessel traffic to receive AIS signals effectively.


---

[Start Installation](../installation/overview.md){ .md-button .md-button--primary }

---


## High Level Steps

Follow these high-level steps to get AIS-catcher up and running:

<div class="steps" markdown>

<div class="step" markdown>

**Decide on your desired setup**  
Decide on using the [Visual Web Control or](#the-visual-web-control) not, for Docker or Raspberry Pi

</div>

<div class="step" markdown>

**Install AIS-catcher**  
Follow the detailed instructions in the [Installation Guide](../installation/overview.md) tailored to your platform and needs
</div>

<div class="step" markdown>

**Customize Input and Output**  
Tailor your setup with our advanced [Options](../configuration/overview.md)
</div>

<div class="step" markdown>

**Set up your Community Feed**  
[Register](https://aiscatcher.org/addstation_ac) your station at **aiscatcher.org** and start feeding
</div>

<div class="step" markdown>

**Leverage Advanced Features**  
Start experimenting with advanced options such as MQTT, Grafana, and NMEA2000 support
</div>

</div>


## The Visual Web Control


![image](https://github.com/user-attachments/assets/abf29893-0567-4b94-9354-e0630cc6f9fc)

The Visual Web Control management interface is available exclusively for Raspberry Pi and Docker deployments as a separate package to ease configuration and management of the receiver. Key features include:

- Background service management
- Configuration interface
- System monitoring
- One-click updates and upgrades

Note: Manual configuration edits may limit certain GUI functionality. The interface provides a lightweight solution ideal for Linux newcomers.


