# Input as UDP or TCP server
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-x</span>
        <span class="cmd-value">server</span>
        <span class="cmd-value">port</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-x</span>
        <span class="cmd-value">udp/tcp</span>
        <span class="cmd-value">server</span>
        <span class="cmd-value">port</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>
AIS-catcher can listen for data that other devices send to it, as a UDP input or a TCP server.

## UDP

UDP takes NMEA, one datagram after another:
```bash
AIS-catcher -x 192.168.1.235 4002
```
In a JSON configuration:
```json
{ "input": "udpserver", "udpserver": { "server": "192.168.1.235", "port": 4002 } }
```

## TCP server

A TCP server is for senders that connect and push their data, such as another AIS-catcher with `-P`, OpenCPN, an NMEA 2000 gateway, or a transponder in "TCP client" mode:
```bash
AIS-catcher -x tcp 0.0.0.0 4002
```
It takes NMEA unless `FORMAT` says otherwise: `TXT` (NMEA), `N2K` (NMEA 2000 frame lines from a gateway), `BASESTATION` or `RAW1090`. For example, for an NMEA 2000 gateway:
```bash
AIS-catcher -x tcp 0.0.0.0 4002 FORMAT N2K
```
In a JSON configuration the TCP server is an input of its own:
```json
{ "input": "tcpserver", "tcpserver": { "server": "0.0.0.0", "port": 4002, "format": "n2k" } }
```

Each connection is read in whole lines, so lines from several senders never mix. Lines end in a line feed. A connection that sends more than 8192 bytes without a line end is closed. A quiet connection is never closed. The server address must be an IPv4 address or `localhost`; `0.0.0.0` listens on every interface.

Messages sent in parts (AIS two-part messages, NMEA 2000 fast packets) are put together across all senders of one input, so two senders that send parts with the same sequence number at the same moment can lose one of them. Give such senders an input each.

Anyone who can reach the port can send ships to it, over UDP and TCP alike: listen on `127.0.0.1` or a local network address unless the port must be open.

## Summary Settings


| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">Device-specific</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| Specific Options | | | |
| <span class="cmd-setting">format</span> | string | <span class="cmd-value">TXT</span> | TCP server only: `TXT`, `N2K`, `BASESTATION` or `RAW1090` |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">-</span> | Port to listen on |
| <span class="cmd-setting">server</span> | string | <span class="cmd-value">-</span> | Address to listen on |