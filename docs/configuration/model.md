#  Decoding Models

The command line provides the `-m```` option which selects the specific decoding model.  In the current version, 4 different receiver models are embedded for raw data samples:

- **Default Model** (``-m 2``): the default demodulation engine.
- **Base Model (non-coherent)** (``-m 1``): using FM discriminator model, similar to RTL-AIS (and GNUAIS/Aisdecoder) with tweaks to the Phase Locked Loop and main receiver filter (computed with a stochastic search algorithm).
- **Standard Model (non-coherent)** (``-m 0``): as the Base Model with brute force timing recovery.
- **FM Discriminator model**: (``-m `3`) as the Standard Model but with the input already assumed to be the output of an FM discriminator. Hence no FM demodulation takes place which allows ```AIS-catcher``` to be used as GNUAIS and AISdecoder.

The Default Model is the most time and memory consuming but experiments suggest it to be the most effective. In my home station, it improves message count by a factor 2 - 3. The reception quality of the Standard Model over the Base Model is more modest at the expense of roughly a 20% increase in computation time. Advice is to start with the Default Model, which should run fine on most modern hardware including a Raspberry 4B and then scale down to ```-m 0```or even ```-m 1```, if needed.

Notice that you can execute multiple models in one run for benchmarking purposes but only the messages from the first model specified are displayed on screen. To benchmark different models specify ```-b``` for timing and/or ```-v``` to compare message count, e.g.
```bash
AIS-catcher -s 1536K -r posterholt.raw -m 2 -m 0 -m 1 -q -b -v
```
The program will run and summarize the performance (count and timing) of three decoding models (on a Raspberry Pi 4B):
```
[AIS engine v0.35]:                      38 msgs at 6.3 msg/s
[Standard (non-coherent)]:               4 msgs at 0.7 msg/s
[Base (non-coherent)]:                   3 msgs at 0.5 msg/s
```
```
[AIS engine v0.35]:                      1036.54 ms
[Standard (non-coherent)]:               932.47 ms
[Base (non-coherent)]:                   859.065 ms
```
In this example the Default Model performs quite well in contrast to the Standard non-coherent engine with 38 messages identified versus 4 for the standard engine. 
This is typical when there are messages of poor quality. However, it increases the decoding time a bit and has a slightly higher memory usage so needs more powerful hardware. Please note that the improvements seen for this particular file are an exception.

For completeness, the decoder for NMEA input as text is activated by `-m 5` and `-m `4` is an experimental implementation to test new ideas. In practice, the user will not require these settings.