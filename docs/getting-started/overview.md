# Work In Progress!

Welcome to the **AIS-catcher Documentation**! Whether you're just beginning or looking to enhance your skills, this comprehensive guide will walk you through installing, configuring, and utilizing AIS-catcher—a powerful tool for processing AIS (Automatic Identification System) data. Discover how AIS-catcher can elevate your maritime data experience.

## What You’ll Learn

By following this guide, you will:

- **Understand AIS Data Fundamentals**: Learn what AIS data is and its significance in maritime operations.
- **Install AIS-catcher Seamlessly**: Set up AIS-catcher on your preferred platform with ease.
- **Configure Your First AIS-catcher Instance**: Set up input and output configurations to start capturing AIS data.
- **Explore Advanced Features**: Delve into integrations such as MQTT, Grafana, and NMEA2000 to enhance your data processing capabilities.

## What You’ll Need

Before getting started, ensure you have the following:

1. **Compatible Hardware Setup**:
   - A **USB-based RTL-SDR device** or another supported SDR receiver.
   - An **AIS antenna** for optimal data reception.

2. **Computer or Server**:
   - **Windows**, **Raspberry Pi**, **Linux**, or **macOS** with basic command-line proficiency.

3. **Internet Connection**:
   - Essential for installation and accessing online resources.

4. **Line of Sight to Ships**:
   - Position yourself near water with active vessel traffic to receive AIS signals effectively.

## High-Level Steps

Follow these high-level steps to get AIS-catcher up and running:

1. **Learn the Basics**:
   - Start with the [AIS Basics](./ais-basics.md) section to understand AIS technology and the role of AIS-catcher.

2. **Install AIS-catcher**:
   - Follow the detailed instructions in the [Installation Guide](./installation.md) tailored to your platform.

3. **Customize Input and Output**:
   - Tailor your setup by exploring the [Input Options](../configuration/input/overview.md) and [Output Options](../configuration/output/overview.md) to meet your specific needs.

4. **Leverage Advanced Features**:
   - Enhance your AIS-catcher experience by integrating advanced tools such as MQTT, Grafana, and NMEA2000 support.

## References

To kickstart your AIS-catcher journey, refer to the following resources:

- [Installation Guide](./installation.md)
- [Full Configuration](../configuration/overview.md)
- [Troubleshooting](../advanced/troubleshooting.md)

If you encounter any issues, the [Community](../community.md) section is a great place to ask questions and connect with other users.

---

With these steps, you're well on your way to making the most of AIS-catcher. Let’s get started!


Follow these quick links to get started:

1. [**Overview**](getting-started/overview.md): Learn the basics of AIS-Catcher and its capabilities.
2. [**Installation Guide**](getting-started/installation.md): Step-by-step instructions for setting up AIS-Catcher on your platform.
4. [**AIS Basics**](getting-started/ais-basics.md): A primer on AIS technology and how it works.


---

## Design criteria of AIS-Catcher

AIS-Catcher is a tool for decoding and analyzing AIS signals from ships, allowing you to monitor vessel movements, improve situational awareness, and contribute to the maritime community.

### **Key Features**
- **Multi-Platform Compatibility**  
  Runs seamlessly on Windows, Ubuntu/Debian, Raspberry Pi, macOS, and even inside Docker containers.
  
  - **Sensitive Decoder**
  The decoder has been designed to extract maximum performance from the available SDR hardware 

  - **Lightweight and Efficient**  
  Written in C++ and optimized for high performance and small footprint on low-power devices like Raspberry Pi.

- **Wide SDR Support**  
  Works with popular SDRs like RTL-SDR, AirSpy, AirSpy HF+ HackRF, SDRPlay, and more.

- **Flexible Outputs**  
  Send AIS data in NMEA format, JSON. Stream data to databases, MQTT brokers, or external software like OpenCPN.

- **Built-In Web Viewer**  
  Access real-time AIS data and system statistics through a web-based interface with advanced customization options and plugin system.

- **Community Exchange**
  Share data with community feed (aiscatcher.org) abd receive position reports from nearby station in the local Web Viewer for performance tuning



---
AIS-catcher began as a basic decoder for RTL-SDR dongles, offering on-screen output and UDP transmission for key aggregation sites. Over time, we've expanded its compatibility to include a wider range of SDRs and input methods. On the output side, it now supports viewing signals and positions through a web viewer, saving to databases, and forwarding as NMEA2000 on Linux systems using socketCAN. This enhancement has subtly shifted AIS-catcher's role, making it a useful tool for managing different AIS data streams. Below is a cheatsheet for the various input and output modes.

![image](https://github.com/jvde-github/AIS-catcher/assets/52420030/53fdef5c-f8ff-4040-a505-2af06c03c234)

---


## Powerful Features for Every Use Case

### Easy to Install
Installation scripts are provided for Linux and Raspberry and pre-build Docker images for easy install. For Raspberry a GUI is available providing easy configuration and start/stop

### Input Options
Receive AIS data from various Software Defined Radios includeing the RTL-SDR, NMEA over network connections or serial devices and NMEA2000 via SocketCAN

### Output Options
Stream AIS messages via UDP/TCP/WebSockets/HTTP push, publish to MQTT brokers, save to files or databases, or visualize in real-time in a built-in Web Viewer.

### JSON and CLI Configuration
Run AIS-Catcher with flexible JSON configuration files or directly via command-line options for advanced control.

### Plugins and Customization
Enhance your setup with custom plugins, styles, and offline map support to create a tailored experience.


---



---

## Join the AIS-Catcher Community

Visit [aiscatcher.org](https://aiscatcher.org) to explore real-time examples, register your station, and contribute to our growing network. Together, we can enhance AIS data visibility worldwide.

---

**Ready to get started?**  
[Install AIS-Catcher](getting-started/installation.md) and turn your SDR-equipped device into a powerful AIS receiver today!
