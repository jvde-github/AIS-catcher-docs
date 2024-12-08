# Purpose

**AIS-catcher** is designed to be a dynamic platform that fosters the continuous improvement of AIS receiver models. We highly value and welcome any suggestions, observations, or shared recordings, especially from setups where current models face challenges.

---

## Join the aiscatcher.org Community

**AIS-catcher** is a free and open-source project dedicated to transforming computers equipped with Software-Defined Radios (SDRs) into robust Automatic Identification System (AIS) receivers. Our mission is to enhance AIS data decoding, provide a versatile tool that supports various input and output methods, and aggregate AIS data at [aiscatcher.org](https://aiscatcher.org) to enable real-time global visualization. Integrating this aggregated data into local web viewers offers a powerful tool to calibrate and improve station performance by identifying its limitations and blind spots.

### How to Get Involved

<div class="steps" markdown>
<div class="step" markdown>
**Update to the Latest Version:**   
Ensure your AIS-catcher installation is up-to-date to benefit from the latest features and improvements.
</div>

<div class="step" markdown> 
**Add Your Station:**   
Register your station by visiting [Register Station](https://aiscatcher.org/addstation_ac). Upon registration, you will receive a unique sharing key.
</div>

<div class="step" markdown>
**Share Your AIS Data:**   
Run AIS-catcher using the `-X` option followed by your sharing key:
     ```bash
     ais-catcher -X YOUR_SHARING_KEY
     ```
This command shares your station's raw AIS data with the community hub/ More details can be found in the [Configuration](configuration/output/community-feed.md) section.
</div>

<div class="step" markdown>
**Explore Community Data in local Web Viewer**   
Sharing activates additional features. Start exploring in your station's web viewer, see below. 
</div>

</div>
---

## Web Viewer Benefits

Enhancing your AIS-catcher experience, the Web Viewer offers two additional map overlays when sharing a community feed: 

### 1. Community Feed

![Community Feed](https://github.com/user-attachments/assets/ef73fabd-91e2-49be-8723-e186703631d4)

**Features:**

  - Displays vessels and objects reported by the AIS-catcher community using grey icons.
  - Helps identify potential blind spots and assess the reception area of your station.

**Benefits:**

  - Improved situational awareness by visualizing community-reported AIS data.
  - Enhanced understanding of your station's coverage and limitations.

### 2. AIS Tropo Ducting Conditions

![AIS Tropo Ducting](https://github.com/user-attachments/assets/72590ae3-bc09-47e4-8951-3bedab22fa3d)

**Features:**

  - Provides an overlay of AIS tropo ducting conditions, refreshed every six hours.
  - Explains AIS observations that typically occur beyond the line-of-sight, extending into hundreds of miles.

**Benefits:**

  - Enhances the interpretation of long-range AIS signals.
  - Assists in distinguishing between direct and ducted AIS receptions.

---

## Get Started Today

Become a part of the **AIS-catcher** community to contribute to and benefit from a collaborative effort in improving AIS reception and data visualization. Together, we can enhance maritime situational awareness and advance AIS technology for everyone.

For more information and to join, visit [aiscatcher.org](https://aiscatcher.org).

---
