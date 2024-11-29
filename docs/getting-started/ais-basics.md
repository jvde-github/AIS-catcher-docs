# Introduction to Automatic Identification System (AIS)

The **Automatic Identification System (AIS)** is a maritime technology designed to improve safety and efficiency in navigation. It provides real-time information about a vessel's identity, position, speed, and heading to nearby ships and coastal monitoring stations. AIS operates on **very high frequency (VHF)** radio waves, ensuring reliable transmission over significant distances.

## Key Details

- **Frequency Range**:
  AIS operates in the **VHF band around 162 MHz**, specifically on the following channels:
  - **161.975 MHz** (AIS 1)
  - **162.025 MHz** (AIS 2)

- **Data Transmission**:
  AIS messages are transmitted in a standardized digital format, enabling vessels and shore-based stations to share crucial navigation data.

- **Applications**:
  - Collision avoidance in crowded waterways.
  - Monitoring by port authorities and maritime traffic services.
  - Enhanced navigation in poor visibility conditions.
  - Search-and-rescue operations and fleet tracking.

## Receiving AIS with Software Defined Radio (SDR)

With modern **Software Defined Radio (SDR)** hardware, it is possible to receive and process AIS messages without the need for expensive, dedicated equipment. By tuning an SDR device to the AIS frequencies (around **162 MHz**), users can monitor and decode AIS signals.

### Why Use SDR for AIS?

1. **Cost-Effective**: 
   SDR devices are affordable and versatile compared to specialized AIS receivers.

2. **Flexible**:
   SDR can be used for a wide range of applications, including AIS and other VHF/UHF monitoring.

3. **Customizable**:
   Open-source software like **AIS-catcher** enables users to decode and analyze AIS signals, view vessel information, and integrate with other systems.

## Learn More

To dive deeper into AIS and its functionality, you can visit the [Wikipedia page on Automatic Identification System](https://en.wikipedia.org/wiki/Automatic_identification_system).
