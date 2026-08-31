# Input as TCP client
<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">url</span>
        <span class="cmd-flag">-gt</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>

    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gt</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
    <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-t</span>
        <span class="cmd-value">protocol</span>
        <span class="cmd-value">host</span>
        <span class="cmd-value">port</span>
        <span class="cmd-flag">-gt</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

Input over TCP with various protocols can be done with `-t` followed by the URL of the server. AIS-catcher connects out to that server; to receive a feed that is pushed to you instead, see [Input as UDP server](udp.md). As an example, to read raw NMEA from a TCP server we can use:
```bash
AIS-catcher -t txt://192.168.1.120:5011
```

Various protocols are supported as input. The table below lists the available protocols and their descriptions:

| Protocol | Description                                  | Protocol | Description                                   |
| :------- | :------------------------------------------- |------- | :------------------------------------------- |
| `txt`    | NMEA0183                                     | `mqtt`   | MQTT                                       |
| `gpsd`   | GPSD server                                  | `wsmqtt` | MQTT over WebSocket                       |
| `ws`     | Plain WebSocket                              | `rtltcp` | RTL-TCP server (raw I/Q)                    |
| `wss`    | WebSocket over TLS                           | `none`   | Raw sample stream, no protocol layer          |
| `basestation` | BaseStation (ADS-B SBS-1)              | `beast` | Beast binary (ADS-B)                          |
| `raw1090`| Raw 1090 MHz frames (ADS-B)                  |          |                                              |

Use the appropriate protocol based on your server's configuration and data format. 

### Secure WebSocket and authentication

`wss://` connects over TLS (port 443 unless given) and sends the URL's path and query with the handshake, so services that select a feed by URL parameters work directly. Credentials in the URL become an `Authorization` header: `user:password@` sends HTTP Basic, a bare `token@` sends `Bearer`. For example, to read the NMEA stream of [Open Waters](https://openwaters.io/ais/) for a bounding box with a personal token:
```bash
AIS-catcher -t "wss://<token>@ais.openwaters.io/v1/nmea?bbox=59.75,29.4,60.15,30.4"
```
The same can be given as settings instead of a URL — `username` alone sends a Bearer token, `username` with `password` sends Basic:
```bash
AIS-catcher -t ais.openwaters.io 443 protocol wss username <token>
```
Each sentence's NMEA 4.10 TAG block (`s:` station, `c:` time) is parsed as usual, so the source's time arrives in `toa`. For a `wss://` endpoint with a self-signed certificate add `ssl_verify off`. Credentials are never written to the log.

### Raw sample streams without a protocol

Some servers simply pipe raw I/Q samples down a socket, with no handshake and no framing. Select `none` — the connection is then a plain socket — and state the sample format and rate yourself:
```bash
AIS-catcher -t none 192.168.1.20 1234 format cs16 -s 1536K
```

With the default protocol (`rtltcp`) AIS-catcher performs the rtl_tcp handshake instead: it sends tuner commands and expects a 12-byte `RTL0` header in return. A raw stream provides neither, so the connection is closed with `RTLTCP: no or invalid response, likely not an rtl-tcp server.`

Two things to keep in mind:

- **Give `format` after `protocol`.** Selecting a protocol also sets the format that protocol implies — `none` implies NMEA text — so `-t 192.168.1.20 1234 protocol none format cs16` is right and the reverse order silently leaves the text parser in place.
- **The sample rate is not part of the stream.** Set it with `-s` to whatever the server sends; the device default is 288K.

A URL takes no settings after it (`-t` reads a lone argument as the URL), so pass them with `-gt`:
```bash
AIS-catcher -t none://192.168.1.20:1234 -gt format cs16 -s 1536K
```

Note the difference with file input, where the format is a positional argument: `AIS-catcher -r CS16 file.raw`.

### Summary Settings

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| Generic Options | | | |
| <span class="cmd-setting">sample_rate</span> | integer | <span class="cmd-value">288K</span> | Sampling rate in Hz (0-20,000,000) |
| <span class="cmd-setting">bandwidth</span> | integer | <span class="cmd-value">0</span> | Tuner bandwidth in Hz (0-1,000,000) |
| <span class="cmd-setting">freqoffset</span> | integer | <span class="cmd-value">0</span> | Frequency correction in PPM (-150 to +150) |
| Specific Options | | | |
| <span class="cmd-setting">host</span> | string | <span class="cmd-value">-</span> | Remote host address |
| <span class="cmd-setting">port</span> | string | <span class="cmd-value">-</span> | Remote port number |
| <span class="cmd-setting">protocol</span> | string | <span class="cmd-value">rtltcp</span> | Protocol (rtltcp/txt/mqtt/wsmqtt/ws/wss/gpsd/basestation/beast/raw1090/none) |
| <span class="cmd-setting">url</span> | string | <span class="cmd-value">-</span> | Complete URL: protocol, optional `user:password@` or `token@`, host, port, path and query |
| <span class="cmd-setting">format</span> | string | <span class="cmd-value">CU8</span> | Format of the incoming data: `CU8`, `CS8`, `CS16` or `CF32` for raw I/Q, or `TXT`, `BASESTATION`, `BEAST`, `RAW1090`. Implied by `protocol`, so set it after that setting — see [Raw sample streams without a protocol](#raw-sample-streams-without-a-protocol) |
| <span class="cmd-setting">ssl_verify</span> | boolean | <span class="cmd-value">true</span> | Verify the TLS certificate on `wss://` |
| | | | |
| TCP Options | | | |
| <span class="cmd-setting">persist</span> | boolean | <span class="cmd-value">true</span> | Keep reconnecting after errors |
| <span class="cmd-setting">keep_alive</span> | boolean | <span class="cmd-value">true</span> | Enable TCP keepalive |
| <span class="cmd-setting">reset</span> | integer | <span class="cmd-value">0</span> | Periodically reset the connection after N minutes to recover wedged links (0=never; range 0-3600). A ±10% random jitter is applied to avoid synchronised reconnects. |
| <span class="cmd-setting">timeout</span> | integer | <span class="cmd-value">0</span> | Connection timeout in seconds (range 0-3600) |
| | | | |
| WebSocket Options | | | |
| <span class="cmd-setting">protocols</span> | string | <span class="cmd-value">-</span> | WebSocket sub-protocols (forced to `mqtt` for `wsmqtt`) |
| <span class="cmd-setting">binary</span> | boolean | <span class="cmd-value">off</span> | Enable binary WebSocket mode (forced on for `wsmqtt`) |
| <span class="cmd-setting">origin</span> | string | <span class="cmd-value">-</span> | Origin header for WebSocket |
| <span class="cmd-setting">username</span> | string | <span class="cmd-value">-</span> | With `ws`/`wss`: sent as `Authorization: Bearer` when no password is set |
| <span class="cmd-setting">password</span> | string | <span class="cmd-value">-</span> | With `ws`/`wss`: `username:password` sent as HTTP Basic |
| | | | |
| MQTT Options | | | |
| <span class="cmd-setting">topic</span> | string | <span class="cmd-value">ais/data</span> | MQTT topic |
| <span class="cmd-setting">client_id</span> | string | <span class="cmd-value">-</span> | MQTT client identifier |
| <span class="cmd-setting">username</span> | string | <span class="cmd-value">-</span> | MQTT username |
| <span class="cmd-setting">password</span> | string | <span class="cmd-value">-</span> | MQTT password |
| <span class="cmd-setting">qos</span> | integer | <span class="cmd-value">0</span> | MQTT QoS level (0-2) |
| <span class="cmd-setting">subscribe</span> | boolean | <span class="cmd-value">true</span> | Subscribe to `topic` (vs publish-only) |
| | | | |
| RTLTCP Options | | | |
| <span class="cmd-setting">tuner</span> | auto/float | <span class="cmd-value">auto</span> | Tuner gain/AGC (0-50 dB or AUTO) |
| <span class="cmd-setting">rtlagc</span> | boolean | <span class="cmd-value">false</span> | Enable RTL AGC |
| <span class="cmd-setting">frequency</span> | integer | <span class="cmd-value">0</span> | Frequency in Hz |
| <span class="cmd-setting">lossless</span> | boolean | <span class="cmd-value">false</span> | RTLTCP is normally a live feed, so the default drops samples when the decoder cannot keep up. Set to `true` when the other end is replaying a recorded stream and you want every sample decoded — the reader will then pause to avoid overflow instead of dropping data. |
</div>