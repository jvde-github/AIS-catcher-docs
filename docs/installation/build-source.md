# Building from Source

--8<-- "docs/disclaimer.md"


## Building

The steps to compile AIS-catcher for RTL-SDR dongles are fairly straightforward on most systems. There are various options including a standard Makefile, a ```solution``` file for MSVC (see next section) and you can use ```cmake```, as we will detail now.

The first step is to ensure you have the necessary dependencies and build tools installed for your device(s). 
For example, the following installs the minimum build tools for Ubuntu and Raspberry Pi:
```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install git make gcc g++ cmake pkg-config libsqlite3-dev -y
```
For MacOS with `brew` installed:
```bash
brew update
brew upgrade

brew install git make gcc cmake pkg-config sqlite3
```

AIS-catcher requires libraries for the particular hardware you want to use. The following table summarizes the installation instructions for all supported hardware:

| System | Linux/Raspberry | macOS | MSVC/vcpkg |
|--|--|--|--|
| Command | *sudo apt install ...* | *brew install ...* | *vcpkg install ...* |
| **RTL-SDR** | librtlsdr-dev | librtlsdr | rtlsdr rtlsdr:x64-windows |
| **Airspy** | libairspy-dev | airspy | - |
| **Airspy HF+** | libairspyhf-dev | airspyhf | - |
| **HackRF** | libhackrf-dev | hackrf | - |
| **SDRplay 1A** | [API 3.x](https://www.sdrplay.com/downloads/) | - | [API 3.x](https://www.sdrplay.com/downloads/) |
| **SoapySDR** | libsoapysdr-dev | - | - |
| **ZeroMQ** | libzmq3-dev | zeromq | ZeroMQ ZeroMQ:x64-windows |
| **HTTP secure** | libssl-dev | - | openssl openssl:x64-windows |
| **ZIP** | zlib1g-dev | - | zlib zlib:x64-windows |

Once the dependencies are in place, the process of installing AIS-catcher  on Linux-based systems becomes:
```bash
git clone https://github.com/jvde-github/AIS-catcher.git --depth 1
cd AIS-catcher
mkdir build
cd build
cmake ..
make
sudo make install
```
For the SDRPlay the software needs to be downloaded and installed from the website of the manufacturer. Once installed, the AIS-catcher build process automatically includes it in the build if available. 

## Microsoft Visual Studio 2019+ 

Ensure that you have ```vcpkg``` [installed](https://vcpkg.io/en/getting-started.html) and integrated into Visual Studio via ```vcpkg integrate install``` (as Administrator). Then install the rtl-sdr drivers as follows:
```
vcpkg install rtlsdr rtlsdr:x64-windows ZeroMQ ZeroMQ:x64-windows soxr soxr:x64-windows
```
The included solution file in the mscv directory allows you to build AIS-catcher with RTL-SDR/ZMQ support in the Visual Studio IDE.
