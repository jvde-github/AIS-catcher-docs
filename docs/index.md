# AIS-Catcher

Welcome to the documentation pages for **AIS-Catcher**, an open-source software package developed to transform your general-purpose Software Defined Radio (SDR)-equipped computer into a powerful, dual-channel AIS receiver. AIS-Catcher bridges the gap between affordable SDR devices like the **RTL-SDR** and expensive commercial AIS receivers, giving you complete control over maritime data monitoring and sharing.

[Community Site](https://aiscatcher.org){ .md-button .md-button--secondary }
[Github](https://github.com/jvde-github/AIS-catcher){ .md-button .md-button--secondary }

Whether you're a maritime enthusiast, researcher, or data aggregator, AIS-Catcher offers advanced features, cross-platform compatibility, and a user-friendly setup to meet your needs. 

## What is AIS?

The **Automatic Identification System (AIS)** is a maritime safety technology similar to **ADSB** used in aviation. AIS provides real-time information such as a vessel’s position, speed, and heading by transmitting messages over **VHF radio frequencies** (around **162 MHz**). 


## Free Open-Source
The sofware is Free Open Source publisched under  GPL3 and can be installed from these docs or our [Github](https://github.com/jvde-github/AIS-catcher)) account.

## Community Features

AIS-catcher offers a vibrant community through our website [aiscatcher.org](https://aiscatcher.org). This platform serves two main purposes:

1. **Station Performance Tracking**  
   Monitor your AIS receiver's performance and compare it with other stations in your area.

2. **Global Ship Movement Overview**  
   Access a comprehensive view of maritime traffic from our network of contributors.

[Join](community/overview.md) our community as stablishd AIS station or as a user of AIS-catcher.


---

## Getting Started

[Getting Started](getting-started/overview.md){ .md-button .md-button--primary }

Follow these quick links to get started:

1. [**Overview**](getting-started/overview.md): Learn the basics of AIS-Catcher and its capabilities.
2. [**Installation Guide**](getting-started/installation.md): Step-by-step instructions for setting up AIS-Catcher on your platform.
4. [**AIS Basics**](getting-started/ais-basics.md): A primer on AIS technology and how it works.

## **Important Disclaimer**

> ### **Hobby and Research Use Only**
> **AIS-Catcher is a hobbyist and research project. It is NOT intended or approved for use in navigation or safety-of-life applications.**
>
> - **No Location Broadcasting:** AIS-Catcher does not broadcast location data and is not compliant with maritime regulations for navigational devices.
> - **Not Certified:** It has not undergone the rigorous testing required for safety-critical applications.
> - **Legal Compliance:** Use of AIS-Catcher must be limited to applications where it is legally allowed, such as personal hobbies or academic research.
>
> **AIS-Catcher is provided as-is, with no guarantees of reliability or accuracy.** Always ensure compliance with your local laws and regulations regarding the reception and processing of AIS signals. AIS-Catcher should only be used in contexts where it is permissible by law and safe to do so.

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

## Resources

- [**Complete User Guide**](getting-started/overview.md): Detailed instructions and feature walkthroughs.
- [**Community and Support**](community.md): Join the AIS-Catcher community to share insights and get help.
- [**FAQ**](faq.md): Answers to frequently asked questions.
- [**References**](references.md): Links to additional resources and documentation.

---

## Join the AIS-Catcher Community

Visit [aiscatcher.org](https://aiscatcher.org) to explore real-time examples, register your station, and contribute to our growing network. Together, we can enhance AIS data visibility worldwide.

---

**Ready to get started?**  
[Install AIS-Catcher](getting-started/installation.md) and turn your SDR-equipped device into a powerful AIS receiver today!
