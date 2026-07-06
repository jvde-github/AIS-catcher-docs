# Windows Binaries

--8<-- "docs/disclaimer.md"

## Installation

Links to pre-built Windows binaries are available below, with and without SDRPlay support. To run AIS-catcher:

1. Unpack the ZIP file to a directory
2. Install the RTL-SDR drivers via [Zadig](https://www.rtl-sdr.com/tag/zadig/) (once per dongle)
3. Double-click `start-GUI.bat` to launch AIS-catcher with its built-in control panel, then finalize the configuration in the browser (requires the **Edge** build from the releases table below)

Alternatively, launch via the command line or `start.bat` (editable with Notepad) for a command-line based configuration.

**Prerequisites:**

- RTL-SDR drivers (install via [Zadig](https://www.rtl-sdr.com/tag/zadig/))
- Visual Studio [runtime libraries](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) (usually already present — only needed if AIS-catcher won't start)

## Recent Releases

> **Note:** Built with latest Windows MSVC compiler. Update [runtime libraries](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) before running. Some issues have been reported with outdated runtime libraries and Windows 10

---

[Finalize the Configuration in the Browser](../usage/online-configuration.md){ .md-button .md-button--primary }
[Command Line First Run](../usage/cli.md){ .md-button .md-button--secondary }

---

## Recent Releases

The AIS-catcher executables are built with the latest Windows MSVC compiler. Please update your [libraries](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) before starting the executables below. Issues have been reported on Windows 10.


| Version | Win32 | x64 | Win32 + SDRPlay | x64 + SDRPlay |
| :------ | :---- | :--: | :-------------- | :------------ |
| Edge    | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.SDRPLAY.x64.zip) |
| v0.70   | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.SDRPLAY.x64.zip) |

If you are looking for a Windows version for the latest development version, it is automatically produced by the standard workflow and referenced in the table above as **Edge**.

