# AIS Basics

The Automatic Identification System (AIS) is the radio system with which ships continuously broadcast who they are, where they are and where they are heading. Every commercial vessel — and many leisure craft — carries a transponder that transmits these reports on the marine VHF band, where anyone with a receiver can pick them up. AIS-catcher turns an inexpensive SDR dongle into exactly such a receiver.

<div class="fact-grid">
  <div class="fact-card"><div class="value">162 MHz</div><div class="label">Marine VHF band</div></div>
  <div class="fact-card"><div class="value">2 channels</div><div class="label">Shared by all vessels</div></div>
  <div class="fact-card"><div class="value">9,600 bit/s</div><div class="label">GMSK per channel</div></div>
  <div class="fact-card"><div class="value">Line of sight</div><div class="label">Range set by antenna height</div></div>
</div>

## How AIS Works

AIS is a broadcast system: there are no connections and no acknowledgements. Each vessel transmits short messages in time slots on two shared channels — every minute holds 2,250 slots per channel, and transponders organize among themselves who uses which slot (a scheme called SOTDMA). A receiver simply listens to both channels and decodes every message it can hear.

Two classes of transponder exist:

| Class | Carried by | Transmit power | Position reports |
|-------|-----------|----------------|------------------|
| **Class A** | Commercial vessels (mandatory) | 12.5 W | Every 2–10 s under way, every 3 min at anchor |
| **Class B** | Leisure craft and small vessels (voluntary) | 2–5 W | Every 30 s under way, every 3 min below 2 knots |

The difference in transmit power is why large ships are typically received much farther out than small craft.

## The Radio Channels

AIS operates just above the marine VHF voice channels, around 162 MHz:

| Channel | Frequency | Use |
|---------|-----------|-----|
| AIS 1 (Channel A) | 161.975 MHz | Standard position reports and data, ship-to-ship and ship-to-shore |
| AIS 2 (Channel B) | 162.025 MHz | Standard position reports and data, ship-to-ship and ship-to-shore |
| AIS 3 (Channel C) | 156.775 MHz | Long-range reports for satellite reception |
| AIS 4 (Channel D) | 156.825 MHz | Long-range reports for satellite reception |

Channels A and B carry virtually all traffic and are the two that AIS-catcher receives simultaneously by default.

## What Ships Transmit

Every vessel is identified by its **MMSI**, a nine-digit number included in every message. The content falls into three groups:

| Data | Examples | How often |
|------|----------|-----------|
| **Dynamic** | Position, speed and course over ground, heading, rate of turn | Every 2 s – 3 min, depending on class and speed |
| **Static** | Name, call sign, MMSI, ship type, dimensions | Every 6 min |
| **Voyage** | Destination, ETA, draught, navigational status | Every 6 min |

This is why a ship often appears on the map before its name shows up: position reports arrive every few seconds, but the name travels in the static report that is only sent every six minutes.

## How Far Will You Receive?

VHF signals travel in essentially straight lines, so the curvature of the earth sets a hard limit on range: the **radio horizon**. How far away that horizon lies depends on the height of both antennas:

<figure class="horizon-figure">
<svg viewBox="0 0 640 200" role="img" aria-label="Diagram of the radio horizon between a shore antenna and a ship over the curved sea">
  <path d="M0,150 Q320,95 640,150 L640,200 L0,200 Z" fill="#dbe9f8"/>
  <path d="M0,150 Q320,95 640,150" fill="none" stroke="#9fb8d4" stroke-width="2"/>
  <line x1="70" y1="139" x2="70" y2="70" stroke="#42566e" stroke-width="3"/>
  <line x1="58" y1="82" x2="82" y2="82" stroke="#42566e" stroke-width="2"/>
  <line x1="61" y1="93" x2="79" y2="93" stroke="#42566e" stroke-width="2"/>
  <circle cx="70" cy="66" r="4" fill="#1976d2"/>
  <text x="90" y="105" fill="#42566e" font-size="14">h&#8321;</text>
  <path d="M545,139 L595,139 L585,128 L555,128 Z" fill="#42566e"/>
  <line x1="570" y1="128" x2="570" y2="103" stroke="#42566e" stroke-width="2.5"/>
  <circle cx="570" cy="100" r="3.5" fill="#1976d2"/>
  <text x="540" y="118" fill="#42566e" font-size="14" text-anchor="end">h&#8322;</text>
  <line x1="70" y1="66" x2="570" y2="100" stroke="#1976d2" stroke-width="2" stroke-dasharray="7 5"/>
  <text x="320" y="70" fill="#1976d2" font-size="13" text-anchor="middle">line of sight</text>
</svg>
<figcaption>d &#8776; 4.12 &#183; (&#8730;h&#8321; + &#8730;h&#8322;) &#8201;km &mdash; with antenna heights h&#8321;, h&#8322; in metres</figcaption>
</figure>

For a large ship with its antenna around 15 m above the water, your antenna height translates into range roughly as follows:

| Your antenna height | Radio horizon |
|--------------------|---------------|
| 2 m — window sill | ~22 km / 12 nmi |
| 5 m — rooftop | ~25 km / 14 nmi |
| 10 m — mast on the roof | ~29 km / 16 nmi |
| 20 m — apartment building | ~34 km / 19 nmi |
| 50 m — hill or tower | ~45 km / 24 nmi |

Two practical consequences:

- **Height beats everything.** Raising the antenna does more for your range than any amplifier or premium receiver — a clear view of the water matters more than gain.
- **Ranges beyond the horizon do occur.** Under certain atmospheric conditions VHF signals bend along the earth's surface (ducting) and ships hundreds of kilometres away appear briefly. See [Long Range AIS](../advanced/long-range.md).

## Antenna and Cable

Any antenna tuned for the marine VHF band works; a simple quarter-wave whip or a dedicated AIS antenna outperforms the stock telescopic antenna of most SDR bundles. What is often overlooked is the cable: coax loss adds up quickly at 162 MHz, and every 3 dB of loss halves the signal power reaching the receiver.

| Cable | Loss per 10 m at ~160 MHz |
|-------|---------------------------|
| RG-58 | ~2.0 dB |
| RG-8X | ~1.5 dB |
| RG-213 | ~0.9 dB |
| LMR-400 | ~0.5 dB |

!!! tip
    Long coax runs can be avoided entirely: place the receiver (for example a Raspberry Pi with the SDR dongle) close to the antenna and run a network cable instead — network cables have no signal loss. See [What You'll Need](what-you-need.md) for hardware suggestions.

## Receiving AIS with an SDR

A traditional AIS receiver is dedicated hardware. A Software Defined Radio does the same job in software: the dongle digitizes a slice of the VHF band and AIS-catcher demodulates and decodes both AIS channels from it simultaneously — at a fraction of the cost of dedicated equipment, on hardware that can also receive many other signals.

!!! warning "Not for navigation"
    SDR-based AIS reception is intended for hobby and research use only. It must **not** be used for navigation, safety-of-life applications or commercial vessel operations — those require type-approved equipment meeting international maritime standards. [Read the full disclaimer](../disclaimer.md).

## Learn More

- [What You'll Need](what-you-need.md) — hardware to build your own receiving station
- [Long Range AIS](../advanced/long-range.md) — receiving beyond the radio horizon
- [Wikipedia: Automatic Identification System](https://wikipedia.org/wiki/Automatic_Identification_System) — history and technical background
