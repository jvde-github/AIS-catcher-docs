---
hide:
  - toc
---

# What you need

A station is three parts on one cable run: an antenna outside, a receiver, and a small computer that runs AIS-catcher. For the receiver there are two good choices: a radio dongle that AIS-catcher tunes and decodes itself, or a receiver that decodes AIS on its own board.

<div class="kit-wrap">
<div class="kit">
  <section class="kit-part" aria-label="The antenna">
    <p class="kit-role">The antenna</p>
    <h3>Glomex RA111AIS</h3>
    <p>A 14&nbsp;cm marine antenna tuned to AIS, sold with a mounting bracket and its cable. Mount it outside, as high as you can. Its cable ends in a PL-259 plug, so add an adapter to SMA for the receiver.</p>
    <p>Any marine VHF antenna works too.</p>
    <div class="kit-buy"><span class="kit-price">€70–140</span><span class="kit-where">marine shops</span></div>
  </section>
  <div class="kit-joint" aria-hidden="true"><span>coax</span><span>PL-259<br>to SMA</span></div>
  <section class="kit-part kit-pick" aria-label="The receiver">
    <p class="kit-role">The receiver<span class="kit-chip">Pick one</span></p>
    <div class="kit-opt">
    <h3>RTL-SDR Blog V3</h3>
    <p>A radio on a USB stick. AIS-catcher tunes it to AIS and decodes the signal on the Pi. Its TCXO keeps it on frequency as it warms up, where the cheapest sticks drift.</p>
    <div class="kit-buy"><span class="kit-price">$35–40</span><a href="https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/">RTL-SDR&nbsp;Blog&nbsp;&nearr;</a></div>
    </div>
    <p class="kit-or">or</p>
    <div class="kit-opt">
    <h3>dAISy-catcher</h3>
    <p>A receiver made for AIS alone, developed by Wegmatt with the AIS-catcher project. It decodes both AIS channels on the board. Plug it in over USB, or stack it on the Pi.</p>
    <div class="kit-buy"><span class="kit-price">$149</span><a href="https://shop.wegmatt.com/products/daisy-catcher-high-performance-ais-receiver">Wegmatt&nbsp;&nearr;</a></div>
    </div>
  </section>
  <div class="kit-joint" aria-hidden="true"><span>USB</span><span>or stacked</span></div>
  <section class="kit-part" aria-label="The computer">
    <p class="kit-role">The computer</p>
    <h3>Raspberry Pi 4</h3>
    <p>Runs AIS-catcher day and night on a few watts. The smallest model is plenty. Add the official power supply and a 32&nbsp;GB memory card.</p>
    <div class="kit-buy"><span class="kit-price"><small>from</small> $35</span><a href="https://www.raspberrypi.com/products/raspberry-pi-4-model-b/">Raspberry&nbsp;Pi&nbsp;&nearr;</a></div>
  </section>
</div>
<p class="kit-note">Prices from November 2026, before shipping, tax and import duties.</p>
</div>

<div class="kit-budget" markdown>

**Which receiver?** The dongle is the cheapest way in. AIS-catcher does all the radio work on the Pi, so its settings and decoding models are yours to try. The dAISy-catcher suits a station that should simply run: it decodes on the board, needs no tuning, and leaves the computer almost idle.

</div>

## The dAISy-catcher up close

Plug it in as a USB device, or stack it on a Raspberry Pi as a HAT. There is no driver to install and no filter or amplifier to try: the RF front end, the radio and the decoding sit on one board, and AIS-catcher reads the messages over its serial line.

<div class="dz-wrap">
<div class="dz" id="dz" role="img" aria-label="Annotated drawing of the dAISy-catcher board: SMA antenna connection; plug-and-play USB device; use as Raspberry Pi HAT; highly sensitive digital radio receiver; RF front end tuned for AIS; advanced signal processing, proven in practice">
<div class="dz-stage">
<img class="dz-board" src="../assets/daisy-board.svg" alt="" width="1000" height="676">
<svg class="dz-lines dz-stacked" viewBox="0 0 1000 716" aria-hidden="true"><g class="dz-p" style="--i:0"><path class="dz-lead" pathLength="1" d="M526.9 630.3Q504.9 670.4 500 716"/><circle class="dz-dot" cx="526.9" cy="630.3" r="9"/></g><g class="dz-p" style="--i:1"><path class="dz-lead" pathLength="1" d="M170.3 331.4Q207 524 166.7 716"/><circle class="dz-dot" cx="170.3" cy="331.4" r="9"/></g><g class="dz-p" style="--i:2"><path class="dz-lead" pathLength="1" d="M379.7 170.1Q290.2 63.7 166.7 0"/><circle class="dz-dot" cx="379.7" cy="170.1" r="9"/></g><g class="dz-p" style="--i:3"><path class="dz-lead" pathLength="1" d="M764.7 336.3Q765.4 161.3 833.3 0"/><circle class="dz-dot" cx="764.7" cy="336.3" r="9"/></g><g class="dz-p" style="--i:4"><path class="dz-lead" pathLength="1" d="M501.5 395Q635.3 588.7 833.3 716"/><circle class="dz-dot" cx="501.5" cy="395" r="9"/></g><g class="dz-p" style="--i:5"><path class="dz-lead" pathLength="1" d="M434.3 260.6Q441.1 123.8 500 0"/><circle class="dz-dot" cx="434.3" cy="260.6" r="9"/></g></svg>
<svg class="dz-lines dz-beside" viewBox="0 0 1000 440" aria-hidden="true"><g class="dz-p" style="--i:0"><path class="dz-lead" pathLength="1" d="M515.3 370.1Q368.8 343.7 228 392"/><circle class="dz-dot" cx="515.3" cy="370.1" r="5.5"/></g><g class="dz-p" style="--i:1"><path class="dz-lead" pathLength="1" d="M312.1 199.8Q245.9 224.6 176 214"/><circle class="dz-dot" cx="312.1" cy="199.8" r="5.5"/></g><g class="dz-p" style="--i:2"><path class="dz-lead" pathLength="1" d="M431.4 107.9Q328.2 54.4 212 58"/><circle class="dz-dot" cx="431.4" cy="107.9" r="5.5"/></g><g class="dz-p" style="--i:3"><path class="dz-lead" pathLength="1" d="M650.8 202.6Q737.5 176.5 826 196"/><circle class="dz-dot" cx="650.8" cy="202.6" r="5.5"/></g><g class="dz-p" style="--i:4"><path class="dz-lead" pathLength="1" d="M500.9 236Q623.5 337.3 780 366"/><circle class="dz-dot" cx="500.9" cy="236" r="5.5"/></g><g class="dz-p" style="--i:5"><path class="dz-lead" pathLength="1" d="M462.6 159.5Q612.5 59.9 792 46"/><circle class="dz-dot" cx="462.6" cy="159.5" r="5.5"/></g></svg>
</div>
<p class="dz-label dz-l-sma" style="--i:0" aria-hidden="true">SMA antenna connection</p>
<p class="dz-label dz-l-usb" style="--i:1" aria-hidden="true">Plug-and-play USB device</p>
<p class="dz-label dz-l-gpio" style="--i:2" aria-hidden="true">Use as Raspberry Pi HAT</p>
<p class="dz-label dz-l-radio" style="--i:3" aria-hidden="true">Highly sensitive digital radio receiver</p>
<p class="dz-label dz-l-shield" style="--i:4" aria-hidden="true">RF front end tuned for AIS</p>
<p class="dz-label dz-l-mcu" style="--i:5" aria-hidden="true">Advanced signal processing, proven in practice</p>
</div>
</div>

<script>
(function () {
    var dz = document.getElementById('dz');
    if (!dz || !('IntersectionObserver' in window) || (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) return;
    dz.classList.add('armed');
    var seen = new IntersectionObserver(function (entries) {
        if (!entries.some(function (e) { return e.isIntersecting; })) return;
        seen.disconnect();
        dz.classList.add('in');
    }, { threshold: 0.5 });
    seen.observe(dz);
})();
</script>

<div class="kit-addons" markdown>

**From the same shop:** a Pi 4 case made for it ($14), a stacking kit for the Pi (from $4) and an SMA to SO-239 adapter for the Glomex cable ($5). One stacking kit, USB cable or RF adapter comes free with the receiver.

</div>

The setup wizard in the [Quick Start](getting-started/overview.md) finds it.

## Where the antenna goes

The antenna's height and view decide what you receive, more than any part you can buy. VHF travels in a line of sight: water you can see from the antenna is water you can hear.

- **High and outside.** Every metre of height pushes the [radio horizon](ais-basics.md#how-far-will-you-receive) further out. A rooftop facing the water beats a window on the wrong side.
- **A short cable.** Coax loses signal at 162 MHz, so keep the run short. Or put the Pi next to the antenna and run a network cable instead. See [antenna and cable](ais-basics.md#antenna-and-cable).
- **What to expect.** From 5–10 m up, large ships typically come in from 25–30 km (14–16 nmi) away, and further from a higher site.
- **Just trying it out?** The telescopic antenna that comes with many dongles, pulled out to about 44 cm and put in a window facing the water, shows the first ships in a busy area.

## Already have something?

- **Another receiver.** AIS-catcher also works with AirSpy, SDRplay, HackRF and others, and with receivers on your network. See [inputs](configuration/input/overview.md).
- **Another computer.** It runs on Linux, Windows and macOS, and in Docker. A Pi Zero 2 W is enough; a Pi 3 or newer is comfortable.
- **The internet** is only needed to install AIS-catcher and to share with the community map. Receiving and decoding run on your own machine.

[Install AIS-catcher](installation/overview.md){ .md-button .md-button--primary }
