# What You'll Need

A complete AIS receiving station needs three pieces of hardware — roughly €60 when starting from nothing, and chances are you already own half of it.

<div class="gear-grid">
  <div class="gear-card">
    <svg viewBox="0 0 24 24" fill="none" stroke="#1976d2" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="5" width="18" height="12" rx="1.5"/>
      <path d="M12 17v3M8 20h8"/>
    </svg>
    <div class="gear-title">Computer</div>
    <div class="gear-desc">Raspberry Pi, PC or Mac</div>
  </div>
  <div class="gear-card">
    <svg viewBox="0 0 24 24" fill="none" stroke="#1976d2" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <rect x="9" y="8" width="6" height="13" rx="1.5"/>
      <rect x="10.5" y="3" width="3" height="5" rx="0.5"/>
    </svg>
    <div class="gear-title">SDR receiver</div>
    <div class="gear-desc">RTL-SDR or dAISy-catcher</div>
  </div>
  <div class="gear-card">
    <svg viewBox="0 0 24 24" fill="none" stroke="#1976d2" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="9" r="1.4" fill="#1976d2" stroke="none"/>
      <path d="M12 10.5V20"/>
      <path d="M8.5 12.5a4.9 4.9 0 0 1 0-7"/>
      <path d="M15.5 12.5a4.9 4.9 0 0 0 0-7"/>
      <path d="M6 14.5a8 8 0 0 1 0-11"/>
      <path d="M18 14.5a8 8 0 0 0 0-11"/>
    </svg>
    <div class="gear-title">VHF antenna</div>
    <div class="gear-desc">tuned for ~162 MHz</div>
  </div>
</div>

## The SDR Receiver

An **RTL-SDR dongle** is the standard choice: inexpensive, well supported and more than capable — a single dongle receives both AIS channels simultaneously. When buying new, pick a current model (RTL-SDR Blog v3 or v4) with a **TCXO** (temperature-compensated oscillator, ±1 ppm): the very cheapest DVB-T sticks drift with temperature, which costs sensitivity on AIS.

Already have other receiving hardware? AIS-catcher also supports AirSpy, AirSpy HF+, SDRPlay, HackRF and several network sources — see the [input options](../configuration/input/overview.md).

## The Antenna

The antenna — and where you put it — determines what you will receive far more than any other component.

- **Starting out**: the telescopic antenna included with most SDR bundles, extended to about 44 cm (a quarter wavelength at 162 MHz) and placed at a window facing the water, is enough to see your first ships in a busy area.
- **Upgrading**: a dedicated AIS or marine VHF antenna mounted outside — as high as you can manage, with a clear view of the water — is the single most effective improvement you can make. [Height beats everything](ais-basics.md#how-far-will-you-receive): the radio horizon grows with antenna height, not with amplifier gain.
- **The cable counts too**: coax loss at 162 MHz adds up quickly, so keep the run short and the cable quality high — see [Antenna and Cable](ais-basics.md#antenna-and-cable). Or skip the problem: mount the computer near the antenna and run a network cable instead.

## The Computer

Almost anything works — AIS decoding is light work:

| Option | Notes |
|--------|-------|
| **Raspberry Pi** | The classic choice for a 24/7 station: a Pi Zero 2 W is sufficient, a Pi 3 or newer is comfortable. Draws only 2–3 W. |
| **Linux / Windows / macOS** | Native packages and builds for all of them. |
| **Docker** | Ready-made images for containerized setups. |

An internet connection is needed for installation and for [sharing your data](../community.md) — the receiving and decoding itself runs entirely locally.

## The Location

VHF signals travel line of sight: water you can see (or nearly see) is water you can receive.

- **Distance to shipping**: a station near a harbour, river or shipping lane sees traffic even with modest equipment; far inland, even a perfect setup has nothing to hear.
- **Elevation and obstructions**: every metre of height extends your [radio horizon](ais-basics.md#how-far-will-you-receive), and buildings or hills between you and the water block signals. A rooftop or attic facing the water beats a ground-floor window on the wrong side.
- **What to expect**: a rooftop antenna at 5–10 m typically receives large ships out to 25–30 km (14–16 nmi) — and considerably farther from an elevated site.

---

[Start Installation](../installation/overview.md){ .md-button .md-button--primary }
[Estimate Your Range](ais-basics.md#how-far-will-you-receive){ .md-button .md-button--muted }
