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

<div class="steps">

<div class="step">

**Decide on your desired setup**

Decide on using the [Web GUI or](#the-web-gui) not, for Docker or Raspberry Pi
</div>

<div class="step">

**Install AIS-catcher**

Follow the detailed instructions in the [Installation Guide](../installation/overview.md) tailored to your platform and needs
</div>

<div class="step">

**Customize Input and Output**

Tailor your setup with our advanced [Options](../configuration/overview.md)
</div>

<div class="step">

**Set up your Community Feed**

[Register](https://aiscatcher.org/join) your station at **aiscatcher.org** and start feeding
</div>

<div class="step">

**Leverage Advanced Features**

Start experimenting with advanced options such as MQTT, Grafana, and NMEA2000 support
</div>

</div>


## The Web GUI

We developed a seperate program for the Raspberry Pi that can manage the configuration and start/stop the program as a background service. This only is available for Raspberry Pi and Docker configuration. 

![image](https://github.com/user-attachments/assets/abf29893-0567-4b94-9354-e0630cc6f9fc)

There are some limitations around managing the full breadth of options. Also once the configuration files have been edited manually (which is still possible) the Web GUI has some limitations on configuring the program.

Either way, it is light weight, so it can help first set up for users less experienced in Linux.


