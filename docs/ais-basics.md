---
title: What is AIS?
description: How ships broadcast who and where they are, and how AIS-catcher receives it.
hide:
  - toc
---

<div class="ais-page ais-learn">

<header class="ais-hero">
  <div class="ais-hero__copy">
    <h1>What is <span>AIS?</span></h1>
    <p>Ships broadcast who they are, where they are and where they are heading. With an antenna and a receiver, AIS-catcher lets you listen in and see the traffic around you.</p>
    <div class="ais-hero__actions">
      <a class="ais-action ais-action--blue" href="../getting-started/overview/">Start receiving</a>
      <a class="ais-action ais-action--soft" href="../what-you-need/">What you need</a>
    </div>
  </div>
  <div class="ais-hero__art"><img src="../assets/ais-qs-harbour.webp" alt="" width="1600" height="697"></div>
</header>

<section class="ais-minute" aria-label="AIS in one minute">
  <p class="ais-minute__label"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#signal"></use></svg></span><strong>AIS in one minute</strong></p>
  <p>The <strong>Automatic Identification System</strong> is the radio system ships use to say who and where they are. Every commercial vessel, and many leisure craft, carries a transponder that keeps sending short reports on the marine VHF band. Anyone nearby with a receiver can pick them up, without an internet connection.</p>
</section>

<section class="ais-panel ais-panel--flow" aria-labelledby="how-it-works">
  <div class="ais-panel__head">
    <h2 id="how-it-works">From ship to live map.</h2>
    <p>AIS-catcher turns the radio messages your antenna picks up into ships on a map.</p>
  </div>
  <img class="ais-flow-art" src="../assets/ais-learn-flow.svg" alt="A ship broadcasts by radio, an antenna on shore picks it up, a computer decodes it and a map shows the ships" width="1120" height="255">
  <ol class="ais-steps">
    <li><b>1</b><strong>Ships broadcast</strong><span>Short reports on marine VHF, around 162 MHz</span></li>
    <li><b>2</b><strong>Your antenna hears</strong><span>Best high and outside, with a view of the water</span></li>
    <li><b>3</b><strong>AIS-catcher decodes</strong><span>From an SDR dongle or a dAISy-catcher, both channels at once</span></li>
    <li><b>4</b><strong>You see the ships</strong><span>On your own map, or passed on to a chart plotter and your own tools</span></li>
  </ol>
</section>

<div class="ais-two">
  <section class="ais-panel" aria-labelledby="what-a-ship-tells-you">
    <div class="ais-panel__head"><h2 id="what-a-ship-tells-you">More than a position.</h2><p>Every message carries the ship's MMSI, a nine-digit number. The rest comes in three kinds of report.</p></div>
    <ul class="ais-rows">
      <li><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#map"></use></svg></span><div><strong>Where is the ship?</strong><span>Position, speed and course over ground, heading, rate of turn</span><small>Every 2 s to 3 min, by class and speed</small></div></li>
      <li><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#ship"></use></svg></span><div><strong>Which vessel is it?</strong><span>Name, call sign, ship type and dimensions</span><small>Every 6 min</small></div></li>
      <li><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#globe"></use></svg></span><div><strong>Where is it going?</strong><span>Destination, ETA, draught and navigational status</span><small>Every 6 min</small></div></li>
    </ul>
    <p class="ais-fine">That is why a ship often shows on the map before its name does: the name comes in the static report, sent only every six minutes.</p>
  </section>
  <section class="ais-panel" aria-labelledby="quick-facts">
    <div class="ais-panel__head"><h2 id="quick-facts">Four quick facts.</h2></div>
    <div class="ais-facts">
      <div><strong>162 MHz</strong><span>The marine VHF band</span></div>
      <div><strong>2 channels</strong><span>AIS 1 and AIS 2, shared by every ship</span></div>
      <div><strong>Receive-only</strong><span>AIS-catcher never transmits</span></div>
      <div><strong>Line of sight</strong><span>Antenna height sets the range</span></div>
    </div>
    <p class="ais-notice"><strong>No internet needed to receive.</strong> AIS-catcher decodes on your own computer. The internet is only for installing it and for sharing with the community map.</p>
  </section>
</div>

<section class="ais-deep" aria-labelledby="go-deeper">
  <div class="ais-panel__head"><h2 id="go-deeper">Want to go deeper?</h2><p>None of this is needed before you install.</p></div>

  <details class="ais-more" id="how-far-will-you-receive">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#eye"></use></svg></span>How far will you receive?</summary>
    <div class="ais-more__body">
      <p>VHF signals travel in essentially straight lines, so the curve of the earth sets a hard limit on range: the <strong>radio horizon</strong>. How far away it lies depends on the height of both antennas.</p>
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
        <figcaption>d &#8776; 4.12 &#183; (&#8730;h&#8321; + &#8730;h&#8322;) &#8201;km, with the antenna heights h&#8321; and h&#8322; in metres</figcaption>
      </figure>
      <p>For a large ship with its antenna around 15 m above the water, your antenna height gives roughly this range:</p>
      <div class="ais-range">
        <span>Window sill, 2 m<strong>22 km</strong></span>
        <span>Rooftop, 5 m<strong>25 km</strong></span>
        <span>Mast on the roof, 10 m<strong>29 km</strong></span>
        <span>Apartment block, 20 m<strong>34 km</strong></span>
        <span>Hill or tower, 50 m<strong>45 km</strong></span>
      </div>
      <p><strong>Height beats everything.</strong> Raising the antenna does more for your range than any amplifier or better receiver: a clear view of the water matters more than gain.</p>
      <p><strong>Ranges beyond the horizon do occur.</strong> In some weather VHF signals bend along the earth's surface (ducting), and ships hundreds of kilometres away show up for a while. See <a href="../advanced/long-range/">Long Range AIS</a>.</p>
    </div>
  </details>

  <details class="ais-more" id="antenna-and-cable">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#link"></use></svg></span>Antenna and cable</summary>
    <div class="ais-more__body">
      <p>Any antenna tuned for the marine VHF band works. A simple quarter-wave whip or a dedicated AIS antenna does better than the telescopic antenna that comes with most SDR dongles. What is often overlooked is the cable: coax loses signal quickly at 162 MHz, and every 3 dB of loss halves the power that reaches the receiver.</p>
      <table>
        <thead><tr><th>Cable</th><th>Loss per 10 m at about 160 MHz</th></tr></thead>
        <tbody><tr><td>RG-58</td><td>2.0 dB</td></tr><tr><td>RG-8X</td><td>1.5 dB</td></tr><tr><td>RG-213</td><td>0.9 dB</td></tr><tr><td>LMR-400</td><td>0.5 dB</td></tr></tbody>
      </table>
      <p>A long coax run can be avoided altogether: put the receiver, for example a Raspberry Pi with the SDR dongle, next to the antenna and run a network cable to the house instead. A network cable loses no signal. See <a href="../what-you-need/">What You Need</a> for the parts.</p>
    </div>
  </details>

  <details class="ais-more" id="time-slots-and-transponder-classes">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#layers"></use></svg></span>Time slots and transponder classes</summary>
    <div class="ais-more__body">
      <p>AIS is a broadcast system: there are no connections and no acknowledgements. Each vessel sends short messages in time slots on two shared channels. Every minute holds 2,250 slots per channel, and the transponders agree among themselves who uses which slot, a scheme called SOTDMA. A receiver simply listens to both channels and decodes every message it hears.</p>
      <table>
        <thead><tr><th>Class</th><th>Carried by</th><th>Power</th><th>Position reports</th></tr></thead>
        <tbody>
          <tr><td><strong>Class A</strong></td><td>Commercial vessels, required</td><td>12.5 W</td><td>Every 2–10 s under way, every 3 min at anchor</td></tr>
          <tr><td><strong>Class B</strong></td><td>Leisure craft and small vessels, voluntary</td><td>2–5 W</td><td>Every 30 s under way, every 3 min below 2 knots</td></tr>
        </tbody>
      </table>
      <p>The difference in power is why large ships come in from much further away than small craft.</p>
    </div>
  </details>

  <details class="ais-more" id="the-radio-channels">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#signal"></use></svg></span>The radio channels</summary>
    <div class="ais-more__body">
      <p>AIS sits just above the marine VHF voice channels, around 162 MHz. Each channel carries 9,600 bit/s, with GMSK modulation.</p>
      <table>
        <thead><tr><th>Channel</th><th>Frequency</th><th>Use</th></tr></thead>
        <tbody>
          <tr><td>AIS 1 (channel A)</td><td>161.975 MHz</td><td>Position reports and data, ship to ship and ship to shore</td></tr>
          <tr><td>AIS 2 (channel B)</td><td>162.025 MHz</td><td>Position reports and data, ship to ship and ship to shore</td></tr>
          <tr><td>AIS 3 (channel C)</td><td>156.775 MHz</td><td>Long-range reports for reception by satellite</td></tr>
          <tr><td>AIS 4 (channel D)</td><td>156.825 MHz</td><td>Long-range reports for reception by satellite</td></tr>
        </tbody>
      </table>
      <p>Channels A and B carry nearly all traffic. They are the two AIS-catcher receives at once by default.</p>
    </div>
  </details>

  <details class="ais-more" id="why-an-sdr-works">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#cpu"></use></svg></span>Why an SDR works as an AIS receiver</summary>
    <div class="ais-more__body">
      <p>A traditional AIS receiver is dedicated hardware. A software-defined radio does the same job in software: the dongle digitizes a slice of the VHF band, and AIS-catcher demodulates and decodes both AIS channels from it at once. It costs a fraction of dedicated equipment, and the same dongle can receive many other signals.</p>
      <p>A dAISy-catcher does the radio work on its own board instead. See <a href="../what-you-need/#choose-a-receiver">which receiver</a> for the difference in practice, and <a href="https://wikipedia.org/wiki/Automatic_Identification_System">Wikipedia</a> for the history of AIS.</p>
    </div>
  </details>
</section>

<p class="ais-endnote"><strong>Receive-only, for hobby and research use.</strong> AIS-catcher is not approved for navigation, safety-of-life use or commercial vessel operations: those need type-approved equipment. <a href="../disclaimer/">Read the disclaimer</a></p>

<section class="ais-cta" aria-label="Next">
  <div><h2>Ready to listen?</h2><p>You need an antenna, a receiver and a computer.</p></div>
  <div class="ais-cta__actions"><a class="ais-action ais-action--primary" href="../getting-started/overview/#install-ais-catcher">Install AIS-catcher</a><a href="../what-you-need/">What you need</a></div>
</section>

</div>

<script>
(function () {
    function openTarget() {
        var el = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
        if (el && el.tagName === 'DETAILS') { el.open = true; el.scrollIntoView(); }
    }
    window.addEventListener('hashchange', openTarget);
    openTarget();
})();
</script>
