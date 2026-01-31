# macOS Installation

--8<-- "docs/disclaimer.md"

## Installation

This guide provides instructions for installing AIS-catcher on macOS systems using Homebrew. AIS-catcher is built from source on macOS to ensure optimal performance for your specific hardware.

## Prerequisites

### Install Homebrew

If you don't already have Homebrew installed, you can install it by opening a terminal and running:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen instructions to complete the installation. After installation, you may need to add Homebrew to your PATH as instructed.

## Installation Steps

### 1. Install Build Dependencies

First, ensure you have the necessary build tools and dependencies:

```bash
brew update
brew upgrade

brew install git make gcc cmake pkg-config sqlite3
```

### 2. Install SDR Hardware Libraries

Depending on your SDR hardware, install the appropriate drivers. For RTL-SDR dongles (most common):

```bash
brew install librtlsdr
```

For other hardware types, install the corresponding libraries:

| Hardware | Homebrew Package |
|----------|-----------------|
| **RTL-SDR** | `librtlsdr` |
| **Airspy** | `airspy` |
| **Airspy HF+** | `airspyhf` |
| **HackRF** | `hackrf` |
| **ZeroMQ** | `zeromq` |

For example, to install support for Airspy and HackRF:

```bash
brew install airspy hackrf
```

### 3. Build and Install AIS-catcher

Once the dependencies are in place, clone the repository and build AIS-catcher:

```bash
git clone https://github.com/jvde-github/AIS-catcher.git --depth 1
cd AIS-catcher
mkdir build
cd build
cmake ..
make
sudo make install
```

The build process will automatically detect and include support for any SDR libraries you have installed.

> **Note:** Building from source can take several minutes depending on your Mac's specifications. The executable will be optimized for your specific hardware.

## Testing the Installation

Once the program is installed, verify it works correctly by checking the available features:

```bash
AIS-catcher -L
```

This command will display all the input devices and features that are included in your build.

## Running AIS-catcher

To start receiving AIS messages with your RTL-SDR dongle:

```bash
AIS-catcher
```

For more advanced usage and configuration options, see the [Command Line Usage](../usage/cli.md) guide.

## Running as a Background Service

Unlike the Linux/Raspberry Pi version, there is no automated background service setup script for macOS. However, you can create a launch agent to run AIS-catcher automatically at startup using `launchd`.

### Creating a Launch Agent

1. First, verify the installation path of AIS-catcher:

```bash
which AIS-catcher
```

This will return either `/usr/local/bin/AIS-catcher` (Intel Macs) or `/opt/homebrew/bin/AIS-catcher` (Apple Silicon Macs). Use this path in the next step.

2. Create a launch agent plist file (note: do **not** use `sudo` for this):

```bash
nano ~/Library/LaunchAgents/com.aiscatcher.plist
```

3. Add the following content, adjusting the path and parameters for your setup:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.aiscatcher</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/AIS-catcher</string>
        <string>-v</string>
        <!-- Add additional parameters as separate strings, for example: -->
        <!-- <string>-u</string> -->
        <!-- <string>5.9.207.224</string> -->
        <!-- <string>2947</string> -->
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/YOUR_USERNAME/aiscatcher.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/YOUR_USERNAME/aiscatcher.error.log</string>
</dict>
</plist>
```

> **Important Notes:**
> - Replace `/usr/local/bin/AIS-catcher` with the path from step 1 if different (e.g., `/opt/homebrew/bin/AIS-catcher` for Apple Silicon)
> - Replace `YOUR_USERNAME` with your actual macOS username
> - Each command-line argument must be in its own `<string>` tag (e.g., `-u`, `5.9.207.224`, and `2947` as three separate strings)
> - Logs are stored in your home directory to persist across reboots (unlike `/tmp` which is cleared on restart)

4. Load the launch agent:

```bash
launchctl load ~/Library/LaunchAgents/com.aiscatcher.plist
```

5. To start the service immediately:

```bash
launchctl start com.aiscatcher
```

6. To stop the service:

```bash
launchctl stop com.aiscatcher
```

7. To unload the service (if you need to make changes to the plist):

```bash
launchctl unload ~/Library/LaunchAgents/com.aiscatcher.plist
```

## Updating AIS-catcher

To update to the latest version, navigate to your AIS-catcher directory and rebuild:

```bash
cd AIS-catcher
git pull
cd build
cmake ..
make
sudo make install
```

## Troubleshooting

### Command Not Found

If you get a "command not found" error after installation, ensure `/usr/local/bin` is in your PATH. Add this to your `~/.zshrc` or `~/.bash_profile`:

```bash
export PATH="/usr/local/bin:$PATH"
```

### CMake Not Found

If cmake is not found, ensure Homebrew is properly installed and in your PATH. After installing Homebrew, you may need to run the commands shown at the end of the Homebrew installation.

### Missing Libraries

If the build fails due to missing libraries, make sure you've installed the required SDR libraries with Homebrew as described in step 2.

## Alternative: MacPorts

While this guide focuses on Homebrew, AIS-catcher should also be possible to build using MacPorts. If you have successfully installed AIS-catcher using MacPorts and would like to contribute installation instructions, please reach out via [GitHub Discussions](https://github.com/jvde-github/AIS-catcher/discussions).

---

[Start First Run](../usage/cli.md){ .md-button .md-button--primary }
[Build from Source Details](build-source.md){ .md-button .md-button--secondary }
