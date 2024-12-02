# Features

AIS-catcher is a tool for decoding and analyzing AIS signals from ships, enabling vessel movement monitoring, situational awareness, and maritime community contributions.

## Core Capabilities

### Multi-Platform Support
- Runs on Windows, Ubuntu/Debian, Raspberry Pi, macOS, and Docker
- Easy installation via scripts and pre-built Docker images
- Web GUI available for Raspberry Pi and Docker deployments

### High-Performance Architecture
- Sensitive decoder optimized for maximum SDR performance
- Lightweight C++ implementation for efficient resource usage
- Neon/SSE acceleration support
- Multi-channel decoding capability across multiple SDRs

### Flexible I/O System
- **Input Sources**
  - Wide SDR hardware support (RTL-SDR, AirSpy, AirSpy HF+, HackRF, SDRPlay)
  - NMEA data over network connections
  - Serial devices
  - NMEA2000 via SocketCAN

- **Output Options**
  - NMEA format and JSON output
  - UDP/TCP/WebSocket streaming
  - HTTP push capabilities
  - MQTT broker publishing
  - Database storage (PostgreSQL)
  - OpenCPN integration
  - File-based logging

## Web Interface

### Built-in Web Viewer
- Interactive map with vessel plots
- Station dashboard
- Message visualization graphs
- Dark mode support
- Mobile-friendly design
- Extensible plugin system

### Web GUI Management (Raspberry Pi & Docker)
- Service control (start/stop)
- Input/output configuration
- System settings management

## Database Integration

### PostgreSQL Features
- Configurable table structure
- Vessel tracking tables
- Message logging
- Station metadata storage

## Advanced Features

### Multi-Channel Support
- Dual RTL-SDR capability
- Multiple frequency band monitoring
- Separate AIS channel processing
- Performance benchmarking

### Modular Design
- Customizable processing pipeline
- Experimentation-friendly architecture
- Maintainable codebase
- Plugin support for extended functionality

### Community Integration
- Data sharing via aiscatcher.org
- Local performance tuning
- Real-time position reports from nearby stations

## Getting Started

1. Review the [Installation Guide](../installation/overview.md)
2. Configure using [Full Configuration Guide](../configuration/overview.md)
3. Check [Troubleshooting](../advanced/troubleshooting.md) if needed
4. Check out our [Forum](https://github.com/jvde-github/AIS-catcher/discussions) for support

Visit [aiscatcher.org](https://aiscatcher.org) to:
- Explore real-time examples
- Register your station
- Contribute to the network

Ready to start? [Install AIS-Catcher](../installation/overview.md) and begin monitoring maritime traffic today!