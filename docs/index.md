<div class="hero" markdown>

# <img class="hero-logo" src="assets/logo-blue.svg" alt=""> AIS-Catcher

**AIS-Catcher** is free and open-source software that turns an inexpensive **Software Defined Radio** (SDR) into a complete **AIS** receiver: receive and visualize ship traffic on a live map, and share the data over the network or with the community. The source code is available on [GitHub](https://github.com/jvde-github/AIS-catcher) under the **GPLv3** license.

[Quick Start](getting-started/overview.md){ .md-button .md-button--primary }
[Install](installation/overview.md){ .md-button .md-button--secondary }
[What's New](what-is-new.md){ .md-button .md-button--secondary }

<span class="hero-note">New to AIS? Read [What is AIS?](ais-basics.md) and [What You Need](what-you-need.md).</span>

</div>

!!! warning "Disclaimer"
    **AIS-Catcher is intended for hobbyist and research projects only. It is NOT approved for use in navigation or safety-of-life applications.** [Read the full disclaimer](disclaimer.md).

## What do you want to do?

<div class="install-grid">

<a class="install-card" href="getting-started/overview/">
<span class="install-title">See ships on a map</span>
<span class="install-desc">Install AIS-catcher, connect a receiver and watch the first ships come in.</span>
</a>

<a class="install-card" href="managed/chart-plotter/">
<span class="install-title">Send ships to a chart plotter</span>
<span class="install-desc">OpenCPN, a plotter or a navigation app on your network.</span>
</a>

<a class="install-card" href="managed/community-map/">
<span class="install-title">Share with the community map</span>
<span class="install-desc">Add what you hear to the live map at aiscatcher.org.</span>
</a>

<a class="install-card" href="managed/receivers/">
<span class="install-title">Connect more receivers</span>
<span class="install-desc">A second radio, a dAISy, or ships arriving over the network.</span>
</a>

<a class="install-card" href="managed/api/">
<span class="install-title">Build on your station</span>
<span class="install-desc">The API, an AI assistant and Home Assistant.</span>
</a>

<a class="install-card" href="advanced/troubleshooting/">
<span class="install-title">No ships yet?</span>
<span class="install-desc">Find out where the signal stops: the receiver, the radio or the map.</span>
</a>

</div>

## Two ways to run it

<div class="install-grid mode-grid">

<a class="install-card" href="managed/dashboard/">
<span class="install-title">Managed mode <span class="install-badge">Recommended</span></span>
<span class="install-desc">AIS-catcher runs in the background, and you set it up in the dashboard in your browser. The Quick Start sets it up this way.</span>
</a>

<a class="install-card" href="usage/overview/">
<span class="install-title">Manual mode</span>
<span class="install-desc">You start AIS-catcher with a configuration file or command-line options, and it does exactly what they say. For scripts, small setups and complex configurations.</span>
</a>

</div>

The guides show every step for both, in tabs: **Managed mode**, **Config file** and **Command line**. The [API](api/overview.md) works the same in both.

[AIS-catcher-control](usage/gui.md) is a separate, optional tool for Raspberry Pi and Debian. It starts and stops the AIS-catcher service and looks after the computer it runs on; the receiver itself is set up in AIS-catcher.
