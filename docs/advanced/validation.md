# Validation

## Experiment at the [Meteotoren in Scheveningen](https://www.meteotoren.nl/index.php?id=index) 

On August 25, 2022 I was given the opportunity to connect AIS-catcher for a few minutes to the antenna system at the [Meteotoren](https://www.meteotoren.nl/index.php?id=ais) which has a consistently high message rate and availability on [MarineTraffic](https://www.marinetraffic.com/en/ais/details/stations/15981). 

We ran AIS-catcher on a laptop for 60 seconds and counted the number of messages for two RTL-SDR dongles (```-gr rtlagc on -T 60 -v 60```): 

| SDR | Run 1 | Run 2 |
| :--- | :--- | :---: |
| RTL-SDR blog v3 | 1061 | 1255 |
| ShipXplorer AIS dongle |  1372 | 1315 |

The ShipXplorer AIS dongle, as far as I can see, is an RTL-SDR with an additional SAW filter (TA0395A). The two sets of runs suggest some advantages of using a dongle with a filter. For reference, the AIS-catcher default decoder showed roughly a 30% improvement over an FM-based decoder in message count. An important factor of the high message rate at the Meteotoren though seems to stem from the location and the installed Yagi antenna. An experiment where we reran with a standard antenna placed at a slightly lower height reduced the message count to below 800 messages per second. 

<p align="center">
<img src="https://user-images.githubusercontent.com/52420030/220280154-602637b2-5874-455f-86fd-cd55e6d51573.png" width=30% height=30%>
<img src="https://user-images.githubusercontent.com/52420030/220280223-264e05da-9ccd-45b1-a5a7-58188e54f8de.png" width=30% height=30%>
</p>

Meteotoren feeds MarineTraffic with a [Comar SLR350NI](https://help.marinetraffic.com/hc/en-us/articles/227724587-Comar-SLR-350Ni). According to the MarineTraffic statistics the message count just prior and just after the experiment was in the area of 1350 messages/minute. We did not observe a difference in range with the MarineTraffic statistics to conclude (see pictures - left is AIS-catcher reception for a few minutes visualized with AISdispatcher, right is a screenshot from MarineTraffic).
These initial results are promising and it would be interesting to compare, in a more scientific manner, how open-source decoders with a generic RTL-SDR and dedicated AIS receiver hardware compare. Thank you Meteotoren for facilitating!

## Experimenting with recorded signals
The functionality to receive radio input from `rtl_tcp` provides a route to compare different receiver packages on a deterministic input from a file. I have tweaked the callback function in `rtl_tcp` so that it instead sends over input from a file to an AIS receiver like `AIS-catcher` and `AISrec`. The same trick can be easily done for `rtl-ais`. The sampling rate of the input file was converted using `sox` to 240K samples/second for `rtl-tcp` and 1.6M samples/second for `rtl-ais`. 
These programs, and others like `gnuais` have been the pioneers in the field of open-source AIS decoding and without them many related programs including this one would arguably not exist.
The output of the various receivers was sent via UDP to AISdispatcher which removes any duplicates and counts messages. The results in terms of number of messages/distinct vessels:

 | File | AIS-catcher v0.35  | AIS-catcher v0.33 | rtl-ais | AISrec 2.208 (trial - super fast) | AISrec 2.208 (pro - slow2)  | AISrec 2.301 (pro - slow2) | Source |
 | :--- | :--- | :---: | :---: | :---: | :---: | :---: |  :---: | 
 |Scheveningen |   44/37| 43/37  | 17/16 | 30/27 | 37/31 | 39/33 | recorded @ 1536K with `rtl-sdr` (auto gain) |
 |Moscow| 213/35 |210/32 | 146/27 |  195/31 |  183/34 | 198/35 | shared by user @ 1920K in [discussion](https://github.com/jvde-github/AIS-catcher/issues/7) |
 |Vlieland | 93/54 |93/53  | 51/31| 72/44 | 80/52 | 82/50 | recorded @ 1536K with `rtl-sdr` (auto gain) |
 |Posterholt |  39/22  |39/22 |2/2 | 13/12 | 31/21 | 31/20 | recorded @ 1536K with `rtl-sdr` (auto gain) |
 
 **Update 1:** AISrec had a version update of 2.208 (October 23, 2021) with improved stability and reception quality and the table above has been updated to include the results from this recent version. 

 **Update 2:** Feverlaysoft has kindly provided me with a license for version 2.208 of AISrec allowing access to additional decoding models. Some experimentation suggests that "Slow2" works best for these particular examples and has been included in the above overview.
 
 **Update 3:** AISrec had a version update to 2.301 (April 17, 2022) with reduced runtime and the table above has been updated to include the results from this recent version. 
 
## Some stations with AIS-catcher

A list of some stations mentioning using AIS-catcher:

- [A caruna, Spain](https://www.marinetraffic.com/en/ais/details/stations/23439)
- [Asendorf, Germany](https://www.marinetraffic.com/en/ais/details/stations/19365)
- [Blackfield 01, UK](https://www.marinetraffic.com/en/ais/details/stations/22665)
- [Boston, US](https://www.marinetraffic.com/en/ais/details/stations/22977)
- [Chaos Consulting, Germany](https://adsb.chaos-consulting.de/map/)
- [Edinburgh, UK](https://www.marinetraffic.com/en/ais/details/stations/11523)
- [Haiphong, Vietnam](https://www.marinetraffic.com/en/ais/details/stations/23016)
- [La Linea de la Concepcion, Spain](https://www.marinetraffic.com/en/ais/details/stations/13854)
- [Naha, Okinawa](https://www.marinetraffic.com/en/ais/details/stations/15306)
- [Oranjeplaat Arnemuiden, NL](https://www.marinetraffic.com/en/ais/details/stations/17136)
- [Pickwick Landing, USA](https://www.marinetraffic.com/en/ais/details/stations/25896)
- [SeaRange AIS receiver](https://www.shipxplorer.com/searange-ais-receiver)
- [Seattle Capitol Hill, US](https://www.marinetraffic.com/en/ais/details/stations/14916)
- [Troguarat, France](https://www.marinetraffic.com/en/ais/details/stations/21360)
- [Tyres, Sweden](https://www.marinetraffic.com/en/ais/details/stations/22269)
- [Vancouver North, Canada](https://www.marinetraffic.com/en/ais/details/stations/29475) with hardware description [here](https://github.com/jvde-github/AIS-catcher/discussions/182).
- [Vancouver West End, Canada](https://www.marinetraffic.com/en/ais/details/stations/7029)
- [Vasa, Finland](https://www.marinetraffic.com/en/ais/details/stations/14994)
- [Vernouillet, France](https://www.marinetraffic.com/en/ais/details/stations/10668)
- [Vlissingen, NL](https://www.marinetraffic.com/nl/ais/details/stations/17133)

AIS-catcher connected to a commercial AIS receiver via serial port:

- [Wren Road Rab 2](https://www.marinetraffic.com/en/ais/details/stations/9615)
- [Baltimore, Ireland](https://www.marinetraffic.com/en/ais/details/stations/10083/_:6fee18c796a96183f56c876a2b26bac6)