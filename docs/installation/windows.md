# Windows Binaries

Links to fully built Windows binaries of recent releases are provided in the table below, with and without SDRPlay support (which requires a running SDRPlay API). Running `AIS-catcher` should be a simple matter of unpacking the ZIP file in one directory and starting the executable on the command line with the required parameters or by clicking `start.bat`, which you can edit with Notepad to set desired parameters.

It will likely run out of the box if you already have RTL-SDR software running on your PC. If you encounter an issue or crash, you might want to check:
- Installation of RTL-SDR drivers is done via [Zadig](https://www.rtl-sdr.com/tag/zadig/).
- Installation of the Visual Studio runtime [libraries](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

The AIS-catcher executables are built with the latest Windows MSVC compiler. Please update your [libraries](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) before starting the executables below. Issues have been reported on Windows 10.

## Recent Releases

| Version | Win32 | x64 | Win32 + SDRPlay | x64 + SDRPlay |
| :------ | :---- | :--: | :-------------- | :------------ |
| Edge    | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/Edge/AIS-catcher.SDRPLAY.x64.zip) |
| v0.60   | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.60/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.60/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.60/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.60/AIS-catcher.SDRPLAY.x64.zip) |
| v0.59   | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.59/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.59/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.59/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.59/AIS-catcher.SDRPLAY.x64.zip) |
| v0.58   | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.58/AIS-catcher.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.58/AIS-catcher.x64.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.58/AIS-catcher.SDRPLAY.x86.zip) | [ZIP](https://github.com/jvde-github/AIS-catcher/releases/download/v0.58/AIS-catcher.SDRPLAY.x64.zip) |

If you are looking for a Windows version for the latest development version, it is automatically produced by the standard workflow and referenced in the table above.
