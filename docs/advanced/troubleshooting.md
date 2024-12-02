# Troubleshooting

## Frequency Correction
AIS-catcher tunes in on a frequency of 162 MHz. However, due to deviations in the internal oscillator of RTL-SDR devices, the actual frequency can be slightly off which will result in no or poor reception of AIS signals. It is therefore important to provide the program with the necessary correction in parts-per-million (ppm) to offset this deviation where needed. For most of our testing, we have used the RTL-SDR v3 dongle where in principle no frequency correction is needed as deviations are guaranteed to be small. For optimal reception though ensure you determine the necessary correction, e.g. [see](https://github.com/steve-m/kalibrate-rtl) and provide this as input via the ```-p``` switch on the command line.

If you are using a cheap RTL-SDR dongle that suffers from thermal drift (i.e. the required PPM correction drifts when the dongle is getting warmer), you can use the option ``-go AFC_WIDE on`` (which is the default model in recent releases). This is a relatively new model (per v0.48) that is less sensitive to frequency drift. You can switch off this model using the switch `-go AFC_WIDE off'. Running the new model setting and the previous default yields results that are more stable for frequency drift.

<p align="center">
<img width="30%" alt="image" src="https://github.com/jvde-github/AIS-catcher/assets/52420030/41c86f20-5bc3-4e83-be15-59d538820a52">
<img width="30%" alt="image" src="https://github.com/jvde-github/AIS-catcher/assets/52420030/7929bfaf-6e21-485d-9a98-4e1ab5f3384d">
</p>

## Frequency Shift and PPM
The Web Viewer include plots of what is called the `frequency shift`. The `frequency shift` is the frequency correction from the central frequencies that AIS-catcher has used to decode the signal. This value is related to  the frequency offset of the RTL-SDR dongle as discussed above but also depends on the deviations in the equipment of the sender. The number is in ppm (parts-per-million, so 1ppm ~ 162 Hz) and in some tables and in screen output the quanity is refered to as `ppm`.  Long-running averages can be used to determine the optimal ppm correction for the receiver setup. These deviations can be corrected with `-p`. Deviations between -3 and +3 will usually not impact reception quality so for modern dongles with frequency stabilization no action is required.


## System USB performance
On some laptops we observed that Windows was struggling with the high volume of data transferred from the RTL SDR dongle to the PC. I am not sure why (likely some driver issue as Ubuntu on the same machine worked fine) but it is worthwhile to check if your system supports transferring from the dongle at a sampling rate of 1.536 MHz with the following command which is part of the osmocom rtl-sdr package:
```console
rtl_test -s 1536000
```
In case you observe a high number of lost data, the advice is to run AIS-catcher at a lower sampling rate for RTL SDR dongles:
```console
AIS-catcher -s 288000
```
If your system allows for it you might opt to run ```AIS-catcher``` at a sample rate of ```2304000```. 

## Known issues

- call of ```rtlsdr_close```  on Windows can result in a crash. This is a problem with the rtlsdr library and not AIS-catcher. Solution: ensure you have the latest version of the library with this patch [rtlsdr](https://github.com/osmocom/rtl-sdr/pull/18). For the shared Windows binaries I have included [this version](https://github.com/jvde-github/rtl-sdr) of the library in which I did a proper [patch](https://lists.osmocom.org/hyperkitty/list/osmocom-sdr@lists.osmocom.org/thread/WPL5MZIX7CGVDF2NECPSTZYDLACAEXRI/) to fix this issue (essentially ensuring all usb transfers have been closed before freeing memory.
- pkg-config on Raspberry Pi returns ```-L``` as library path which results in a build error. Temporarily fixed by assuming lib is in standard location, long term fix: switch to cmake
- ...