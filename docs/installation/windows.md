# Windows Binaries

!!! warning "Disclaimer"
    **AIS-catcher is intended for hobbyist and research projects only. It is NOT approved for use in navigation or safety-of-life applications.** [Read the full disclaimer](../disclaimer.md).

## Installation

Pre-built Windows binaries are available below, with and without SDRPlay support. There are two ways to run your station:

- **[Managed mode](#managed-mode)** (recommended) — configure and control your station from the browser.
- **[Manual mode](#manual-mode)** — configure via command-line options.

<div class="recommended" markdown>

## Managed Mode

<div class="steps" markdown>

<div class="step" markdown>

**Download and unpack**  
Download the **Edge** build from the [releases table](#recent-releases) below and unpack the ZIP file to a directory

</div>

<div class="step" markdown>

**Set up the dongle driver**  
Use [Zadig](https://www.rtl-sdr.com/tag/zadig/) to assign the generic WinUSB driver to your RTL-SDR dongle (once per dongle)

</div>

<div class="step" markdown>

**Launch AIS-catcher**  
Double-click `start-GUI.bat` in the unzipped folder to start AIS-catcher in managed mode

</div>

<div class="step" markdown>

**Complete the setup wizard**  
Open the dashboard in your browser at `http://localhost:8118`. On first use, the setup wizard walks you through configuring your input device and outputs, and starts the receiver:

[Setup Wizard](../managed/setup-wizard.md){ .md-button .md-button--primary }

</div>

</div>

That's it — your station is up and running. See [Getting Around the Dashboard](../managed/dashboard.md) to monitor and fine-tune it.

</div>

## Manual Mode

Alternatively, launch via the command line or `start.bat` (editable with Notepad) for a command-line based configuration.

[Command Line Run](../usage/cli.md){ .md-button }

!!! tip
    If AIS-catcher won't start, install the Visual Studio [runtime libraries](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) (usually already present).

## Recent Releases

The AIS-catcher executables are built with the latest Windows MSVC compiler. Please update your [libraries](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) before starting the executables below. Issues have been reported on Windows 10.


| Version | Win32 | x64 | Win32 + SDRPlay | x64 + SDRPlay |
| :------ | :---- | :--: | :-------------- | :------------ |
| Edge    | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.SDRPLAY.x64.zip) |
| v0.70   | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.SDRPLAY.x64.zip) |

If you are looking for a Windows version for the latest development version, it is automatically produced by the standard workflow and referenced in the table above as **Edge**.

