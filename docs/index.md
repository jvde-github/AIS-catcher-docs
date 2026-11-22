---
title: Home
description: Receive, decode and explore AIS traffic with AIS-catcher.
hide:
  - toc
---

<div class="ais-landing">
  <aside class="ais-landing__rail" aria-label="Documentation sections">
    <div class="ais-rail__inner">
      <a class="ais-rail__brand" href="./" aria-label="AIS-catcher documentation home">
        <img src="assets/logo.svg" alt="" width="33" height="33">
        <span><strong>AIS-<em>catcher</em></strong><small>Documentation</small></span>
      </a>
      <nav class="ais-rail__nav" aria-label="Documentation navigation">
        <a class="is-current" aria-current="page" href="./"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#home"></use></svg>Home</a>
        <a href="getting-started/overview/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#rocket"></use></svg>Start Receiving</a>
        <a href="managed/dashboard/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#monitor"></use></svg>Use Your Station</a>
        <a href="guides/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#book"></use></svg>Guides</a>
        <a href="installation/overview/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#tool"></use></svg>Install &amp; Maintain</a>
        <a href="configuration/overview/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#code"></use></svg>Reference</a>
        <a href="advanced/troubleshooting/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#lifebuoy"></use></svg>Help</a>
        <a href="what-is-new/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#sparkles"></use></svg>What's New</a>
      </nav>
      <p class="ais-rail__bottom">Open source, community driven.<br><a href="https://github.com/jvde-github/AIS-catcher">AIS-catcher on GitHub <span aria-hidden="true">↗</span></a></p>
    </div>
  </aside>

  <div class="ais-landing__body">
    <section class="ais-home-hero" aria-labelledby="ais-hero-heading">
      <div class="ais-home-hero__copy">
        <h1 id="ais-hero-heading">From radio signals <br>to <span>live ships.</span></h1>
        <p class="ais-home-hero__intro">Receive and decode the messages ships send, and watch them on a map of your own. Start with one SDR dongle; add receivers and connect your own tools later.</p>
        <div class="ais-home-hero__actions">
          <a class="ais-action ais-action--primary" href="getting-started/overview/">Quick Start</a>
          <a class="ais-action ais-action--outline" href="#ais-choose">Browse the docs</a>
        </div>
        <p class="ais-home-hero__footnote">Free and open source, under the GPLv3. Runs on Raspberry Pi, Linux, Windows, macOS and Docker.</p>
      </div>
      <figure class="ais-daynight">
        <img class="day" src="assets/ais-home-viewer-day.webp" alt="The AIS-catcher web viewer: a ship card, the map and the vessel table" width="1600" height="814">
        <img class="night" src="assets/ais-home-viewer-night.webp" alt="" width="1600" height="814">
      </figure>
    </section>

    <section class="ais-home-section" id="ais-choose" aria-labelledby="ais-paths-heading">
      <h2 id="ais-paths-heading">Choose your path</h2>
      <p class="ais-intro">New to AIS, or building a bigger station? Start where you are.</p>
      <div class="ais-path-grid">
        <a class="ais-path-card" href="getting-started/overview/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#rocket"></use></svg></span><strong>Start Receiving</strong><span class="ais-path-card__desc">Install, connect your receiver and see your first ships.</span></a>
        <a class="ais-path-card" href="managed/dashboard/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#monitor"></use></svg></span><strong>Use Your Station</strong><span class="ais-path-card__desc">The dashboard, your receivers and outputs, and manual mode.</span></a>
        <a class="ais-path-card" href="guides/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#book"></use></svg></span><strong>Guides</strong><span class="ais-path-card__desc">Step by step, from a chart plotter to Home Assistant.</span></a>
        <a class="ais-path-card" href="installation/overview/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#tool"></use></svg></span><strong>Install &amp; Maintain</strong><span class="ais-path-card__desc">Install on your system, run it as a service and keep it up to date.</span></a>
        <a class="ais-path-card" href="configuration/overview/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#code"></use></svg></span><strong>Reference</strong><span class="ais-path-card__desc">Every setting: command line, configuration file, inputs, outputs and the API.</span></a>
        <a class="ais-path-card" href="advanced/troubleshooting/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#lifebuoy"></use></svg></span><strong>Help</strong><span class="ais-path-card__desc">No ships yet? Find where the signal stops, and where to ask.</span></a>
      </div>
    </section>

    <section class="ais-home-start" aria-labelledby="ais-start-heading">
      <div class="ais-home-start__intro">
        <h2 id="ais-start-heading">From hardware <br>to your first ship.</h2>
        <p class="ais-intro">Four steps. The setup wizard in the dashboard does most of the work.</p>
        <ol class="ais-start-list">
          <li><a href="getting-started/overview/#install-ais-catcher"><b>1</b>Install AIS-catcher</a></li>
          <li><a href="getting-started/overview/#open-the-dashboard"><b>2</b>Open the dashboard</a></li>
          <li><a href="getting-started/overview/#run-the-setup-wizard"><b>3</b>Run the setup wizard</a></li>
          <li><a href="getting-started/overview/#see-your-ships"><b>4</b>See your ships</a></li>
        </ol>
        <a class="ais-action ais-action--blue" href="getting-started/overview/">Follow the Quick Start</a>
      </div>
      <div class="ais-home-start__cards">
        <div class="ais-start-card">
          <div class="ais-start-card__visual ais-start-card__visual--hardware"><img src="assets/daisy-board.svg" alt="" loading="lazy"></div>
          <span class="ais-start-card__number">Step 1</span><h3>Connect and install</h3><p>An antenna, a receiver such as a dAISy-catcher or an RTL-SDR, and a computer.</p>
        </div>
        <div class="ais-start-card">
          <div class="ais-start-card__visual ais-start-card__visual--wizard"><img src="assets/qs-w2-input.webp" alt="The setup wizard's choice of receiver" loading="lazy"></div>
          <span class="ais-start-card__number">Steps 2–3</span><h3>Configure</h3><p>The setup wizard finds your receiver and starts it.</p>
        </div>
        <div class="ais-start-card">
          <div class="ais-start-card__visual ais-start-card__visual--map"><img src="assets/ais-home-viewer-day.webp" alt="" loading="lazy"></div>
          <span class="ais-start-card__number">Step 4</span><h3>See your ships</h3><p>The first ships appear on your own map within minutes.</p>
        </div>
      </div>
    </section>

    <section class="ais-home-feature" aria-labelledby="ais-feature-heading">
      <picture class="ais-home-feature__art"><source media="(max-width: 1030px)" srcset="assets/ais-home-lighthouse.webp" width="1200" height="800"><img src="assets/ais-home-lighthouse-tall.webp" alt="" width="480" height="768" loading="lazy"></picture>
      <div class="ais-home-feature__copy">
        <h2 id="ais-feature-heading">Your station, your view.</h2>
        <p class="ais-intro">Everything your receivers hear, in your own browser: ships and their tracks, charts and station statistics.</p>
        <a class="ais-text-link" href="managed/dashboard/">Getting around the dashboard</a>
      </div>
      <ul class="ais-feature-list">
        <li><a href="managed/dashboard/#the-map"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#map"></use></svg><span><strong>Map and tracks</strong><small>Ships near you and where they went</small></span></a></li>
        <li><a href="managed/input/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#signal"></use></svg><span><strong>Inputs and outputs</strong><small>Your receivers, and where the data goes</small></span></a></li>
        <li><a href="managed/dashboard/#the-map"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#chart"></use></svg><span><strong>Statistics</strong><small>Messages, range and activity over time</small></span></a></li>
        <li><a href="api/overview/"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#layers"></use></svg><span><strong>API and integrations</strong><small>Programs, assistants and Home Assistant</small></span></a></li>
      </ul>
    </section>

    <section class="ais-home-section" aria-labelledby="ais-modes-heading">
      <h2 id="ais-modes-heading">One receiver. Different ways to run it.</h2>
      <p class="ais-intro">Set it up in your browser, or write the configuration yourself.</p>
      <div class="ais-mode-grid">
        <a href="managed/dashboard/" class="ais-mode"><span class="ais-mode__icon"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#monitor"></use></svg></span><span><strong>Managed mode <em>Recommended</em></strong><small>Set up and run AIS-catcher from the dashboard in your browser.</small></span></a>
        <a href="usage/overview/" class="ais-mode"><span class="ais-mode__icon"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#terminal"></use></svg></span><span><strong>Manual mode</strong><small>A command line or a configuration file says exactly what it does.</small></span></a>
        <a href="usage/gui/" class="ais-mode"><span class="ais-mode__icon"><svg aria-hidden="true"><use href="assets/ais-home-icons.svg#layers"></use></svg></span><span><strong>AIS-catcher-control</strong><small>The optional control tool for Raspberry Pi and Debian: start, stop and update AIS-catcher from the browser.</small></span></a>
      </div>
    </section>

    <section class="ais-home-outro" aria-labelledby="ais-outro-heading">
      <h2 id="ais-outro-heading">Build. Customize. Integrate.</h2>
      <p class="ais-intro">Several receivers, geofences, the API, an AI assistant and home automation: a tutorial series on building on your station.</p>
      <a class="ais-action ais-action--blue" href="tutorials/">Read the tutorials</a>
      <div class="ais-home-outro__wave" aria-hidden="true"></div>
    </section>

    <footer class="ais-home-footer"><span>AIS-catcher is free and open source, under the GPLv3.</span><span><strong>Receive-only.</strong> Not approved for navigation or safety-of-life use. <a href="disclaimer/">Disclaimer</a></span></footer>
  </div>
</div>
