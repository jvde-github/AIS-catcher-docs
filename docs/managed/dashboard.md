---
title: Getting Around
description: "The dashboard of managed mode, in your browser: the map, the control bar, the settings and places."
hide:
  - toc
---

<div class="ais-page ais-learn">

<header class="ais-hero ais-hero--night">
  <div class="ais-hero__copy">
    <span class="ais-eyebrow">Use your station · Managed mode</span>
    <h1>Your station, <span>at a glance.</span></h1>
    <p>In managed mode, AIS-catcher runs in the background and you run your station from the dashboard, in your browser: the ships it receives, the receiver, and every setting.</p>
    <p class="ais-chips"><span class="ais-chips__live">Web dashboard</span><span>Port 8118: <code>localhost:8118</code></span></p>
  </div>
</header>

<p class="ais-notice"><strong>Already installed?</strong> Open port 8118 of the computer that runs AIS-catcher, for example <code>http://localhost:8118</code>. First time? The <a href="../../getting-started/overview/">Quick Start</a> covers the first start and the setup wizard.</p>

<ol class="ais-steps ais-steps--3" aria-label="On this page">
  <li><a href="#the-map"><b>1</b><strong>Explore the map</strong><span>Live ships and the map's menus</span></a></li>
  <li><a href="#the-control-bar"><b>2</b><strong>Run your station</strong><span>Start, stop and see it working</span></a></li>
  <li><a href="#settings"><b>3</b><strong>Change settings</strong><span>Receivers, outputs and more</span></a></li>
</ol>

<section aria-labelledby="meet-your-dashboard">
  <div class="ais-panel__head">
    <span class="ais-eyebrow">The dashboard</span>
    <h2 id="meet-your-dashboard">Meet your dashboard</h2>
    <p>The map fills the screen. Its menus sit at the top; the bar that runs the station sits at the bottom.</p>
  </div>
  <figure class="ais-shot">
    <div class="ais-shot__frame">
      <img src="../../assets/managed/dashboard-overview.webp" alt="The dashboard: the approaches to Hook of Holland on the map with the ships the station receives, the menus at the top and the control bar at the bottom" width="2880" height="1800">
      <span class="ais-shot__pin" style="left: 19%; top: 24%">1</span>
      <span class="ais-shot__pin" style="left: 36.5%; top: 2.9%">2</span>
      <span class="ais-shot__pin" style="left: 38%; top: 96.4%">3</span>
    </div>
  </figure>
  <ol class="ais-steps ais-steps--3" aria-label="What the numbers show">
    <li><b>1</b><strong>The map</strong><span>The ships your station receives, live</span></li>
    <li><b>2</b><strong>The menus</strong><span>The ship list, statistics and the map's settings</span></li>
    <li><b>3</b><strong>The control bar</strong><span>Start, stop, settings and how the station is doing</span></li>
  </ol>
</section>

<section class="ais-panel ais-two" aria-labelledby="the-map">
  <div>
    <span class="ais-eyebrow">1 · The map</span>
    <h2 id="the-map">Watch the ships around you</h2>
    <p class="ais-fine">The map shows the ships your station receives, live. Its menus at the top open the ship list, statistics and the map's own settings.</p>
  </div>
  <p class="ais-endnote"><strong>The dashboard's map is a plain one.</strong> It loads no plugins and no about page, and it has no log tab: the log is under <strong>Settings → System → Log</strong>. For a map with plugins or an about page, add a server under <strong>Settings → Services</strong> and open that map instead.</p>
</section>

<section aria-labelledby="the-control-bar">
  <div class="ais-panel__head">
    <span class="ais-eyebrow">2 · The control bar</span>
    <h2 id="the-control-bar">Run your station from the bar</h2>
    <p>The bar at the bottom of the dashboard runs the station.</p>
  </div>
  <img class="ais-bar-shot" src="../../assets/managed/dashboard-controlbar.webp" alt="The control bar: the channel lights, Stop, Settings, Running with the time since the start, and the community map icon" width="2880" height="130">
  <div class="ais-path-grid">
    <div class="ais-path-card"><strong>Channel lights</strong><span class="ais-path-card__desc">A light for each AIS channel, A B C D, which flashes as messages arrive.</span></div>
    <div class="ais-path-card"><strong>Start or Stop</strong><span class="ais-path-card__desc">Starts and stops the receiver.</span></div>
    <div class="ais-path-card"><strong>Settings</strong><span class="ais-path-card__desc">Opens the settings.</span></div>
    <div class="ais-path-card"><strong>Running or Stopped</strong><span class="ais-path-card__desc">With the time since the start. A count of warnings and errors appears next to it; press it to open the log.</span></div>
    <div class="ais-path-card"><strong>The community map icon</strong><span class="ais-path-card__desc">On the right. Its colour shows whether the station shares with the community map; it links to aiscatcher.org.</span></div>
    <div class="ais-path-card"><strong>The arrow</strong><span class="ais-path-card__desc">On the left, it hides the bar. <strong>Controls</strong> brings it back.</span></div>
  </div>
</section>

<section aria-labelledby="settings">
  <div class="ais-panel__head">
    <span class="ais-eyebrow">3 · Settings</span>
    <h2 id="settings">Everything under Settings</h2>
    <p><strong>Settings</strong> opens a list on the left. Each item opens a page.</p>
  </div>
  <div class="ais-path-grid">
    <a class="ais-path-card" href="../station/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#tower"></use></svg></span><strong>Stations</strong><span class="ais-path-card__desc">Your station's name and position.</span></a>
    <a class="ais-path-card" href="../input/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#signal"></use></svg></span><strong>Inputs</strong><span class="ais-path-card__desc">Your receivers.</span></a>
    <a class="ais-path-card" href="../output/"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#link"></use></svg></span><strong>Outputs</strong><span class="ais-path-card__desc">The community map and the programs that get your data.</span></a>
    <div class="ais-path-card"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#layers"></use></svg></span><strong>Flow</strong><span class="ais-path-card__desc">Which input reaches which output.</span></div>
    <div class="ais-path-card"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#globe"></use></svg></span><strong>Services</strong><span class="ais-path-card__desc">The map servers, Home Assistant and webhooks.</span></div>
    <a class="ais-path-card" href="#places"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#map"></use></svg></span><strong>Places</strong><span class="ais-path-card__desc">Ports, berths, anchorages and zones on the map.</span></a>
    <a class="ais-path-card" href="#system"><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#cpu"></use></svg></span><strong>System</strong><span class="ais-path-card__desc">Status, data and history, the log, the configuration file, access and about.</span></a>
  </div>
  <p class="ais-notice"><strong>Saving.</strong> Each page ends with <strong>Cancel</strong> and <strong>Save changes</strong>. A saved change is used at once; the receiver restarts by itself when a change needs it.</p>
  <details class="ais-more" id="system">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#cpu"></use></svg></span>What is under System?</summary>
    <div class="ais-more__body">
      <p><strong>Status</strong> shows the receiver and the computer. <strong>Copy for bug report</strong> copies both.</p>
      <p><strong>Data &amp; history</strong> sets whether ships and statistics are kept over a restart.</p>
      <p><strong>Log</strong> holds the log, which the dashboard's map does not show.</p>
      <p><strong>Config file</strong> shows the file the dashboard writes.</p>
      <p><strong>Access</strong> sets the password and HTTPS. See <a href="../remote-access/">Remote Access and Security</a>.</p>
      <p><strong>About</strong> has <strong>Run setup</strong>, which runs the setup wizard again.</p>
    </div>
  </details>
</section>

<section class="ais-panel ais-panel--flow" aria-labelledby="places">
  <div class="ais-panel__head">
    <span class="ais-eyebrow">Settings · Places</span>
    <h2 id="places">Draw your own places</h2>
    <p><strong>Settings → Places</strong> is an editor for the places on the map: ports, berths, anchorages, terminals, guard zones and more.</p>
  </div>
  <ol class="ais-steps ais-steps--3">
    <li><b>1</b><strong>Open Places</strong><span>The first time, it asks to enable places and shows the folder they are saved in. Press <b>Save and continue</b>.</span></li>
    <li><b>2</b><strong>Pick or draw a place</strong><span>Pick one from the list or on the map, or press <b>New place</b>. Draw or reshape its outline, and set its <b>Type</b> and its <b>Parent</b>.</span></li>
    <li><b>3</b><strong>Save the place</strong><span>Press <b>Save place</b>. It takes effect at once, on the map and for every ship inside the changed outline.</span></li>
  </ol>
  <details class="ais-more">
    <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#layers"></use></svg></span>Import a place, or keep places in a folder</summary>
    <div class="ais-more__body">
      <p><strong>Import…</strong>, in the place menu, takes a GeoJSON Feature from anywhere. What it recognises is carried over: the name, the type, codes, the parent, category and rank. Everything else in the file is kept, and a Feature that says nothing about itself becomes a guard zone. The result opens for review and is stored when you save.</p>
      <p><strong>Import shape</strong> and <strong>Paste shape</strong>, in the map's toolbar, replace only the outline of the place you are editing.</p>
      <p>To use a folder of place files instead, enter it under <strong>System → Data &amp; history → Files → Place directory</strong>.</p>
    </div>
  </details>
</section>

<section aria-label="Start managed mode yourself">
<details class="ais-more" id="start-it-yourself">
  <summary><span class="ais-icon-tile"><svg aria-hidden="true"><use href="../../assets/ais-home-icons.svg#terminal"></use></svg></span>Start managed mode yourself</summary>
  <div class="ais-more__body">
    <p>The installs start AIS-catcher in managed mode for you. Started by hand, it takes <code>-E</code> with its configuration file and the address the dashboard listens on:</p>
    <div class="language-console highlight"><pre><span></span><code>AIS-catcher -E ~/aiscatcher.json 127.0.0.1:8118</code></pre></div>
    <p>With <code>127.0.0.1</code>, only this computer can open the dashboard. See <a href="../remote-access/">Remote Access and Security</a> to open it to your network. Prefer a configuration file or the command line? See <a href="../../usage/overview/">Manual Mode</a>.</p>
  </div>
</details>
</section>

<section class="ais-cta" aria-label="Next">
  <div><span class="ais-eyebrow">Keep exploring</span><h2>What's next for your station?</h2></div>
  <div class="ais-cta__actions"><a class="ais-action ais-action--primary" href="../receivers/">Connect your receivers</a><a class="ais-action ais-action--primary" href="../output/">Outputs</a><a class="ais-action ais-action--primary" href="../remote-access/">Access and security</a></div>
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
