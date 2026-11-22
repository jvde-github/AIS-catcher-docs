---
title: Guides
description: Step-by-step guides for what to do with your station next.
hide:
  - toc
---

<div class="ais-page ais-learn">

<header class="ais-hero ais-hero--shot">
  <div class="ais-hero__copy">
    <h1>Do more with your <span>station.</span></h1>
    <p>Step-by-step guides for what comes after the first ships. Each one shows the steps in the dashboard, in a configuration file and on the command line.</p>
    <nav class="ais-hero__jump" aria-label="Guide groups">
      <a href="#set-up-your-station">Set up your station</a>
      <a href="#send-your-ships-on">Send your ships on</a>
      <a href="#build-on-your-station">Build on your station</a>
      <a href="#more">More</a>
      <a href="#tutorials">Tutorials</a>
    </nav>
  </div>
  <div class="ais-hero__art"><img src="../assets/guides/udp-2-form.webp" alt="The dashboard's settings, with a UDP output for a chart plotter" width="2016" height="1156"></div>
</header>

<section class="ais-guide-group" aria-labelledby="set-up-your-station">
  <div class="ais-guide-group__head">
    <span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#tower"></use></svg></span>
    <h2 id="set-up-your-station">Set up your station</h2>
    <p>Put the station on the map, with every receiver it has.</p>
  </div>
  <ul class="ais-guide-list">
    <li><a href="../managed/station/"><strong>Name and place your station</strong><span>Where the antenna stands: every distance, bearing and range is measured from there.</span></a></li>
    <li><a href="../managed/receivers/"><strong>Connect your receivers</strong><span>An input for every receiver: an SDR, a dAISy-catcher, or NMEA over the network.</span></a></li>
    <li><a href="../advanced/GPS/"><strong>Location from GPS</strong><span>On a boat or in a vehicle, the station moves with the antenna.</span></a></li>
    <li><a href="../advanced/Low-spec-devices/"><strong>Small computers</strong><span>Less load on a Pi Zero, the settings that cost the least reception first.</span></a></li>
  </ul>
</section>

<section class="ais-guide-group" aria-labelledby="send-your-ships-on">
  <div class="ais-guide-group__head">
    <span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#link"></use></svg></span>
    <h2 id="send-your-ships-on">Send your ships on</h2>
    <p>Pass what you receive to other programs and other people.</p>
  </div>
  <ul class="ais-guide-list">
    <li><a href="../managed/chart-plotter/"><strong>Send ships to your chart plotter <em class="ais-badge">A good first guide</em></strong><span>OpenCPN, a chart plotter or a navigation app on your network, over UDP.</span></a></li>
    <li><a href="../managed/community-map/"><strong>Share with the community map</strong><span>Your ships on the live map at aiscatcher.org, anonymously or with a station page.</span></a></li>
    <li><a href="../managed/home-assistant/"><strong>Vessels in Home Assistant</strong><span>Your station and the vessels you follow as entities, over MQTT.</span></a></li>
    <li><a href="../advanced/grafana/"><strong>Graph your station in Grafana</strong><span>Messages, range and signal over time, kept by Prometheus.</span></a></li>
  </ul>
</section>

<section class="ais-guide-group" aria-labelledby="build-on-your-station">
  <div class="ais-guide-group__head">
    <span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#code"></use></svg></span>
    <h2 id="build-on-your-station">Build on your station</h2>
    <p>Your station's data for your own programs.</p>
  </div>
  <ul class="ais-guide-list">
    <li><a href="../managed/api/"><strong>Ask your station, the API</strong><span>Vessels, tracks, port calls and events, as JSON over HTTP.</span></a></li>
    <li><a href="../managed/assistant/"><strong>Let an AI assistant read your station</strong><span>Which ships are near, who arrived today: asked in plain words over MCP. It only reads.</span></a></li>
  </ul>
</section>

<section class="ais-guide-group" aria-labelledby="more">
  <div class="ais-guide-group__head">
    <span class="ais-icon-tile"><svg aria-hidden="true"><use href="../assets/ais-home-icons.svg#layers"></use></svg></span>
    <h2 id="more">More</h2>
    <p>Aircraft, other radios, and ships beyond the horizon.</p>
  </div>
  <ul class="ais-guide-list">
    <li><a href="../advanced/ADSB/"><strong>Show aircraft (ADS-B) on the map</strong><span>The aircraft dump1090 or readsb receives, next to your ships.</span></a></li>
    <li><a href="../advanced/GNUradio/"><strong>Decode samples from GNU Radio</strong><span>Shift, filter or resample in GNU Radio, then decode in AIS-catcher, over ZeroMQ.</span></a></li>
    <li><a href="../advanced/offline/"><strong>Offline web viewer</strong><span>The viewer without internet, with maps from files of your own.</span></a></li>
    <li><a href="../advanced/long-range/"><strong>Long Range AIS</strong><span>The two channels meant for satellites, on a receiver of their own.</span></a></li>
  </ul>
</section>

<section class="ais-panel" aria-labelledby="tutorials">
  <div class="ais-panel__head"><h2 id="tutorials">Tutorials</h2><p>A series that builds one station up, from a second receiver to home automation.</p></div>
  <ol class="ais-steps">
    <li><a href="../tutorials/stations/"><b>1</b><strong>Multiple receivers and stations</strong><span>Several antennas, each a station of its own</span></a></li>
    <li><a href="../tutorials/places/"><b>2</b><strong>Geofencing with places</strong><span>Ports, berths and guard zones on your map</span></a></li>
    <li><a href="../tutorials/api-and-mcp/"><b>3</b><strong>The API and MCP</strong><span>Your station's data for programs and assistants</span></a></li>
    <li><a href="../tutorials/home-automation/"><b>4</b><strong>Home automation and webhooks</strong><span>A notification when a ship comes in</span></a></li>
  </ol>
</section>

</div>
