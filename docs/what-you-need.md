---
title: What You Need
description: The antenna, the receiver and the computer for an AIS station, and where the antenna goes.
hide:
  - toc
---

<div class="ais-page ais-learn">

<header class="ais-hero ais-hero--tower">
  <div class="ais-hero__copy">
    <h1>What you <span>need.</span></h1>
    <p>Three parts: an antenna outside, a receiver, and a computer that runs AIS-catcher. The software is free, and you can start simple and grow the station later.</p>
    <div class="ais-hero__actions">
      <a class="ais-action ais-action--blue" href="../getting-started/overview/#install-ais-catcher">Install AIS-catcher</a>
      <a class="ais-action ais-action--soft" href="../ais-basics/">What is AIS?</a>
    </div>
  </div>
  <div class="ais-hero__art"><img src="../assets/ais-home-lighthouse.webp" alt="" width="1200" height="800"></div>
</header>

<section class="ais-panel" aria-labelledby="the-three-parts">
  <div class="ais-panel__head"><h2 id="the-three-parts">Three parts.</h2><p>The antenna connects to the receiver, and the receiver to the computer.</p></div>
  <div class="ais-kit-grid">
    <article class="ais-kit">
      <img src="../assets/ais-learn-antenna.svg" alt="" width="220" height="145">
      <h3>A VHF antenna</h3>
      <p>Any antenna for marine VHF, around 162 MHz. Outside and as high as you can is best.</p>
      <p class="ais-buy"><b>€70–140</b>Glomex RA111AIS, from marine shops</p>
    </article>
    <article class="ais-kit">
      <img src="../assets/ais-learn-dongle.svg" alt="" width="220" height="145">
      <h3>A receiver</h3>
      <p>An RTL-SDR dongle, or a dAISy-catcher that decodes AIS on its own board. <a href="#choose-a-receiver">Which one?</a></p>
      <p class="ais-buy"><b>$35–149</b>RTL-SDR Blog V3 or dAISy-catcher</p>
    </article>
    <article class="ais-kit">
      <img src="../assets/ais-learn-computer.svg" alt="" width="220" height="145">
      <h3>A computer</h3>
      <p>A Raspberry Pi runs AIS-catcher day and night on a few watts. A PC or a Mac works too. You watch the ships in your browser.</p>
      <p class="ais-buy"><b>from $35</b>Raspberry Pi 4, with its power supply and a 32&nbsp;GB card</p>
    </article>
  </div>
  <div class="ais-done">
    <span class="ais-done__mark" aria-hidden="true">✓</span>
    <p><strong>That is the whole station.</strong> AIS-catcher is free and open source: no subscription, and no special display.</p>
    <a href="../getting-started/overview/">Set it up</a>
  </div>
</section>

<section class="ais-section" aria-labelledby="choose-a-receiver">
  <div class="ais-panel__head"><h2 id="choose-a-receiver">Which receiver?</h2><p>Both work with AIS-catcher. They differ in where the radio work happens.</p></div>
  <div class="ais-choice-grid">
    <article class="ais-choice">
      <div class="ais-choice__top"><img src="../assets/ais-learn-dongle.svg" alt="" width="220" height="145"><div><h3>RTL-SDR Blog V3</h3><p>A radio on a USB stick</p></div></div>
      <p>AIS-catcher tunes it to AIS and decodes both channels on the computer, so its settings and decoding models are yours to try. Its TCXO keeps it on frequency as it warms up, where the cheapest sticks drift.</p>
      <ul>
        <li>The cheapest way in</li>
        <li>The computer does the radio work</li>
        <li>Linux, Windows and macOS</li>
      </ul>
      <p class="ais-buy"><b>$35–40</b><a href="https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/">RTL-SDR Blog ↗</a></p>
    </article>
    <article class="ais-choice">
      <div class="ais-choice__top"><img class="ais-choice__photo" src="../assets/daisy-catcher-photo.webp" alt="The dAISy-catcher board" width="720" height="508"><div><h3>dAISy-catcher</h3><p>A receiver made for AIS alone</p></div></div>
      <p>Developed by Wegmatt with the AIS-catcher project. It decodes both AIS channels on the board, and AIS-catcher reads the messages over its serial line.</p>
      <ul>
        <li>No tuning and no driver</li>
        <li>Leaves the computer almost idle</li>
        <li>Over USB, or stacked on a Raspberry Pi</li>
      </ul>
      <p class="ais-buy"><b>$149</b><a href="https://shop.wegmatt.com/products/daisy-catcher-high-performance-ais-receiver">Wegmatt ↗</a></p>
    </article>
  </div>
  <p class="ais-fine">Prices from November 2026, before shipping, tax and import duties.</p>
</section>

<section class="ais-panel ais-place" aria-labelledby="where-the-antenna-goes">
  <div>
    <h2 id="where-the-antenna-goes">Give your antenna a view of the water.</h2>
    <p>Where the antenna goes decides what you receive, more than any part you can buy. VHF travels in a line of sight: water you can see from the antenna is water you can hear.</p>
    <ul class="ais-checks">
      <li><strong>High and outside.</strong> Every metre of height pushes the <a href="../ais-basics/#how-far-will-you-receive">radio horizon</a> further out.</li>
      <li><strong>A short cable.</strong> Coax loses signal at 162 MHz. Or put the Pi next to the antenna and run a network cable: see <a href="../ais-basics/#antenna-and-cable">antenna and cable</a>.</li>
      <li><strong>What to expect.</strong> From 5–10 m up, large ships typically come in from 25–30 km away.</li>
      <li><strong>Just trying it out?</strong> The dongle's telescopic antenna, pulled out to about 44 cm, in a window facing the water shows the first ships in a busy area.</li>
    </ul>
  </div>
  <img src="../assets/ais-learn-coast.svg" alt="" width="400" height="262">
</section>

<section class="ais-deep" aria-labelledby="hardware-notes">
  <div class="ais-panel__head"><h2 id="hardware-notes">Practical hardware notes.</h2><p>Skip these if you are ready to install.</p></div>

  <details class="ais-more" id="antenna-and-connectors">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#link"></use></svg></span>Antenna and connectors</summary>
    <div class="ais-more__body">
      <p>The Glomex RA111AIS is a 14&nbsp;cm marine antenna tuned to AIS, sold with a mounting bracket and its cable. Its cable ends in a PL-259 plug, so add an adapter to SMA for the receiver. Wegmatt sells an SMA to SO-239 adapter for it.</p>
      <p>Any marine VHF antenna works too.</p>
    </div>
  </details>

  <details class="ais-more" id="the-daisy-catcher-up-close">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#cpu"></use></svg></span>The dAISy-catcher up close</summary>
    <div class="ais-more__body">
      <p>Plug it in as a USB device, or stack it on a Raspberry Pi as a HAT. There is no driver to install and no filter or amplifier to try: the RF front end, the radio and the decoding sit on one board.</p>
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
      <p><strong>From the same shop:</strong> a Pi 4 case made for it ($14), a stacking kit for the Pi (from $4) and the SMA to SO-239 adapter for the Glomex cable ($5). One stacking kit, USB cable or RF adapter comes free with the receiver.</p>
      <p>The setup wizard in the <a href="../getting-started/overview/">Quick Start</a> finds it.</p>
    </div>
  </details>

  <details class="ais-more" id="already-have-something">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#monitor"></use></svg></span>Already have a receiver or a computer?</summary>
    <div class="ais-more__body">
      <p><strong>Another receiver.</strong> AIS-catcher also works with AirSpy, SDRplay, HackRF and others, and with receivers on your network. See <a href="../configuration/input/overview/">inputs</a>.</p>
      <p><strong>Another computer.</strong> It runs on Linux, Windows and macOS, and in Docker. A Pi Zero 2 W is enough; a Pi 3 or newer is comfortable.</p>
      <p><strong>The internet.</strong> Only needed to install AIS-catcher and to share with the community map. Receiving and decoding run on your own machine.</p>
    </div>
  </details>
</section>

<section class="ais-cta" aria-label="Next">
  <div><h2>Got the three parts?</h2><p>Install AIS-catcher and run the setup wizard: it finds your receiver.</p></div>
  <div class="ais-cta__actions"><a class="ais-action ais-action--primary" href="../getting-started/overview/#install-ais-catcher">Install AIS-catcher</a><a href="../ais-basics/">What is AIS?</a></div>
</section>

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
(function () {
    function openTarget() {
        var el = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
        if (el && el.tagName === 'DETAILS') { el.open = true; el.scrollIntoView(); }
    }
    window.addEventListener('hashchange', openTarget);
    openTarget();
})();
</script>
