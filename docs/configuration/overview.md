# Settings Overview

AIS-catcher follows a modular architecture: one or more **inputs** feed a decoding **model**, which distributes the messages to any number of **outputs**. Every setting in this reference belongs to one of these three stages — click a stage to jump to its settings:

<div class="flow-diagram">
<a class="flow-node flow-node--input" href="../input/overview/">Input</a>
<span class="flow-arrow">→</span>
<a class="flow-node flow-node--model" href="../model/">Model</a>
<span class="flow-arrow">→</span>
<a class="flow-node flow-node--output" href="../output/overview/">Output</a>
</div>

- [**Input**](input/overview.md) — SDR devices (RTL-SDR, AirSpy, …), network streams, serial devices and files.
- [**Model**](model.md) — message decoding and processing; AIS-catcher includes various decoder models for experimentation.
- [**Output**](output/overview.md) — community feed, UDP/TCP/HTTP/MQTT, web viewers, PostgreSQL and the screen.

Each setting is documented with its JSON key and command-line switch. In managed mode the most common settings appear as fields in the [dashboard](../managed/dashboard.md); this reference covers the complete set.

!!! note "Key casing (CLI vs JSON)"
    In JSON configuration files, keys are case-sensitive and should be lowercase. On the command line, setting names passed after a device/output switch (e.g. `-gr`, `-gm`, `-u`, `-H`) are not case-sensitive. Tables in this documentation show setting names in lowercase to match JSON.

## Usage Profiles

The same three stages scale from simple to complex setups:

<div class="profile-grid">
  <div class="profile-card">
    <div class="profile-title">Receiver</div>
    <p class="profile-desc">Minimal decode & output</p>
  </div>
  <div class="profile-card">
    <div class="profile-title">Aggregator</div>
    <p class="profile-desc">Route & filter streams</p>
  </div>
  <div class="profile-card">
    <div class="profile-title">Database</div>
    <p class="profile-desc">Log to PostgreSQL</p>
  </div>
  <div class="profile-card">
    <div class="profile-title">Experimenter</div>
    <p class="profile-desc">Multi-SDR testing</p>
  </div>
  <div class="profile-card">
    <div class="profile-title">Map Viewer</div>
    <p class="profile-desc">Built-in visualization</p>
  </div>
</div>

## Advanced Architecture

For more complex setups, AIS-catcher supports multiple inputs with input-specific models: multiple input sources operate independently, each input can use several specialized models for decoding, and each model can send its data to one or more outputs.

<div class="arch-diagram">
<svg viewBox="0 0 470 186" xmlns="http://www.w3.org/2000/svg" font-family="Roboto, sans-serif" font-size="13">
  <defs>
    <marker id="arrow" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
      <polygon points="0 0, 9 3.5, 0 7" fill="#8aa0ba"/>
    </marker>
  </defs>
  <!-- Inputs -->
  <rect x="1" y="16" width="100" height="42" rx="8" fill="#e3f2fd" stroke="#1976d2" stroke-width="1.5"/>
  <text x="51" y="42" text-anchor="middle" fill="#0d47a1">Input 1</text>
  <rect x="1" y="128" width="100" height="42" rx="8" fill="#e3f2fd" stroke="#1976d2" stroke-width="1.5"/>
  <text x="51" y="154" text-anchor="middle" fill="#0d47a1">Input 2</text>
  <!-- Models -->
  <rect x="185" y="1" width="100" height="38" rx="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="235" y="25" text-anchor="middle" fill="#1b5e20">Model A1</text>
  <rect x="185" y="74" width="100" height="38" rx="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="235" y="98" text-anchor="middle" fill="#1b5e20">Model A2</text>
  <rect x="185" y="147" width="100" height="38" rx="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="235" y="171" text-anchor="middle" fill="#1b5e20">Model B</text>
  <!-- Outputs -->
  <rect x="369" y="1" width="100" height="38" rx="8" fill="#fff3e0" stroke="#e65100" stroke-width="1.5"/>
  <text x="419" y="25" text-anchor="middle" fill="#bf360c">Output 1</text>
  <rect x="369" y="74" width="100" height="38" rx="8" fill="#fff3e0" stroke="#e65100" stroke-width="1.5"/>
  <text x="419" y="98" text-anchor="middle" fill="#bf360c">Output 2</text>
  <rect x="369" y="147" width="100" height="38" rx="8" fill="#fff3e0" stroke="#e65100" stroke-width="1.5"/>
  <text x="419" y="171" text-anchor="middle" fill="#bf360c">Output 3</text>
  <!-- Input to model arrows -->
  <path d="M101,37 L183,22" stroke="#8aa0ba" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
  <path d="M101,37 L183,91" stroke="#8aa0ba" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
  <path d="M101,149 L183,164" stroke="#8aa0ba" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
  <!-- Model to output arrows -->
  <path d="M285,20 L367,20" stroke="#8aa0ba" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
  <path d="M285,20 L367,90" stroke="#8aa0ba" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
  <path d="M285,93 L367,93" stroke="#8aa0ba" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
  <path d="M285,166 L367,96" stroke="#8aa0ba" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
  <path d="M285,166 L367,166" stroke="#8aa0ba" stroke-width="1.5" fill="none" marker-end="url(#arrow)"/>
</svg>
</div>
