# Windows

AIS-catcher for Windows is a ZIP file: download it from the [downloads](#downloads) below and unzip it to a folder. Take the **Edge** build.

## Managed mode

1. With an RTL-SDR, use [Zadig](https://www.rtl-sdr.com/tag/zadig/) to give it the WinUSB driver, once per dongle.
2. Double-click `start-GUI.bat` in the unzipped folder.
3. Open the dashboard in your browser, as in the [Quick Start](../getting-started/overview.md#open-the-dashboard).

## Manual mode

Run `AIS-catcher.exe` from a command prompt in the unzipped folder, or put your options in `start.bat` with Notepad and double-click it. See [Manual Mode](../usage/overview.md).

!!! tip "Does not start?"
    Install the Microsoft [Visual C++ runtime](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170). It is usually already there.

## Downloads

The AIS-catcher executables are built with the latest Windows MSVC compiler. Please update your [libraries](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) before starting the executables below. Issues have been reported on Windows 10.


| Version | Win32 | x64 | Win32 + SDRPlay | x64 + SDRPlay |
| :------ | :---- | :--: | :-------------- | :------------ |
| **Edge** (latest, recommended) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.x64.zip) | not shipped | not shipped |
| v0.70 (older, no managed mode) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.70/AIS-catcher.SDRPLAY.x64.zip) |

!!! note "Edge is the latest build, not the browser"
    **Edge** is the latest build of AIS-catcher, produced automatically from the `main` branch each time the code changes. It is the recommended download and the only Windows build with managed mode and `start-GUI.bat`. The name refers to the build, not the Microsoft Edge browser.

    v0.70 is an older release, kept for its SDRPlay builds (see below). It predates managed mode, so started with `-E` it stops with `Option -E is obsolete`.

!!! note "SDRPlay builds for Windows"
    **v0.70 is the last Windows release with SDRPlay support.** The SDRPlay API installer can no longer be downloaded from an automated build, so these binaries are no longer produced. The v0.70 downloads above remain available.

    SDRPlay support itself has not been removed: it is still part of AIS-catcher and is available on Linux and macOS, where the API is installed separately. On Windows you can still [build from source](build-source.md) after installing the SDRPlay API yourself.

