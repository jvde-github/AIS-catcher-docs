---
hide:
  - toc
---

# Decode Samples from GNU Radio

GNU Radio can send its samples to AIS-catcher over ZeroMQ (ZMQ). Use it to shift, filter or resample a signal before AIS-catcher decodes it, or to share one SDR between several programs.

**You need:** GNU Radio with its ZMQ blocks, and AIS-catcher started with a configuration file or the command line. The dashboard has no ZMQ input.

!!! tip "No ZeroMQ library needed"
    The ZMQ input is part of AIS-catcher. It connects over `tcp://` to a publisher on ZeroMQ 4 or later. `ipc://` endpoints do not work.

<div class="stepper" data-eyebrow="Guide" markdown>

<div class="stepper-step" markdown>

## Prepare the signal

AIS-catcher decodes the samples as it would those of an SDR. In the flowgraph, bring the signal to this form before it leaves GNU Radio:

- **Centre:** 162.000 MHz. Channel A, at 161.975 MHz, then lies 25 kHz below the centre, and channel B, at 162.025 MHz, 25 kHz above it.
- **Rate:** from 96,000 to 12,288,000 samples a second. AIS-catcher decodes 96K, 192K, 288K, 384K, 768K, 1536K, 3072K, 6144K and 12288K as they are. It resamples any other rate up to the next one in this list.
- **Pace:** from a recording, add a **Throttle** block at the rate of the recording. Without it, GNU Radio sends faster than AIS-catcher decodes, and samples are dropped.

For example, a recording made at 62,500 samples a second and centred on 161.985 MHz holds channel A only, 10 kHz below its centre. Three blocks between the source and the sink make it ready:

1. **Throttle**, with **Sample Rate** 62500.
2. **Rational Resampler**, with **Interpolation** 192 and **Decimation** 125. This gives 62,500 × 192 / 125 = 96,000 samples a second.
3. **Frequency Xlating FIR Filter**, with **Taps** `[1]`, **Center Frequency** 15000 and **Sample Rate** 96000. This moves 162.000 MHz, 15 kHz above the old centre, to the centre, and channel A with it to 25 kHz below.

Resample before you shift. At 62,500 samples a second there is no room for channel A 25 kHz from the centre.

</div>

<div class="stepper-step" markdown>

## Add a ZMQ PUB Sink

End the flowgraph in a **ZMQ PUB Sink**. It publishes the samples, and AIS-catcher subscribes to them.

| Setting | Value |
|---------|-------|
| **IO Type** | **Complex**. AIS-catcher reads it as `CF32`. |
| **Address** | `tcp://*:5555` lets AIS-catcher connect from any computer on your network. With `tcp://127.0.0.1:5555`, only from this computer. |
| **Pass Tags** | **No**. With tags, each message carries a header that AIS-catcher would read as samples. |
| **Filter Key** | Empty. A key goes out with every message, and AIS-catcher would read it as samples. |
| **Connection** | **Bind**, under **Advanced**. AIS-catcher connects to the sink, not the other way round. |

Some versions of GNU Radio have no **Filter Key** or **Connection**. Set the others as above.

</div>

<div class="stepper-step" markdown>

## Add a ZMQ input

=== "Managed mode"

    The dashboard has no ZMQ input: the **Device Type** list does not offer one, and **Network client (RTL-TCP, TCP, MQTT)** has no ZMQ protocol.

    Run AIS-catcher in manual mode for this, with a configuration file or the command line: see [How Manual Mode Works](../usage/overview.md).

=== "Config file"

    Add an entry to the `receiver` list:

    ```json
    {
      "config": "aiscatcher",
      "version": 1,
      "receiver": [
        { "input": "zmq", "zmq": { "endpoint": "tcp://127.0.0.1:5555", "format": "CF32" }, "sample_rate": 96000, "description": "GNU Radio" }
      ],
      "server": [
        { "port": 8100 }
      ]
    }
    ```

    | Key | What it does |
    |-----|--------------|
    | `input` | `zmq`: AIS-catcher subscribes to a ZMQ publisher. |
    | `endpoint` | The **Address** of the sink, as `tcp://host:port`. On another computer, put its address in place of `127.0.0.1`. |
    | `format` | The format of the samples: `CF32` for **Complex**. Without it, AIS-catcher reads `CU8`. |
    | `sample_rate` | The rate the flowgraph sends, in samples a second. The stream does not carry it. |
    | `description` | The input's name in the statistics. |
    | `server` | The [web viewer](../configuration/output/web-viewer.md), whose map shows the ships. |

    Then restart AIS-catcher with the file:

    ```bash
    AIS-catcher -C config.json
    ```

=== "Command line"

    Add `-z` with the format and the endpoint, and `-s` with the sample rate:

    ```bash
    AIS-catcher -z CF32 tcp://127.0.0.1:5555 -s 96000 -N 8100
    ```

    `CF32` is the format of **Complex**. Without a format, AIS-catcher reads `CU8`. The endpoint is the **Address** of the sink: on another computer, put its address in place of `127.0.0.1`. `-s` gives the rate the flowgraph sends, which the stream does not carry. `-N 8100` starts the [web viewer](../configuration/output/web-viewer.md).

    !!! tip "From the command line to a configuration file"
        Add `-J` to print your command line as a configuration file instead of running it: `AIS-catcher -z CF32 tcp://127.0.0.1:5555 -s 96000 -J`.

</div>

<div class="stepper-step" markdown>

## Check it works

Start the flowgraph and AIS-catcher, in either order: AIS-catcher keeps trying to connect until the sink is there.

- In an area with traffic, AIS-catcher shows each message it decodes on the screen.
- With the [web viewer](../configuration/output/web-viewer.md) on, open **Statistics**. Under **System**, **Message rate** shows what comes in. Under **This Session**, **Channel A** and **Channel B** count the messages of each channel.

!!! question "Nothing decoded?"
    - **The log says AIS-catcher is not connected:** nothing publishes at that endpoint. Check that the flowgraph runs, the address and the port, and that **Connection** is **Bind**.
    - **The log says "not a ZeroMQ publisher of version 4 or later":** another program answers on that port, or a ZeroMQ older than version 4.
    - **Connected, but no messages:** check the format and the sample rate you gave AIS-catcher against the flowgraph, that the signal is centred on 162.000 MHz, that **Pass Tags** is **No** and that **Filter Key** is empty.

</div>

</div>

## More

**One channel.** AIS-catcher can also decode a single channel that lies at the centre of the stream, at 12,000 to 192,000 samples a second. The recording above then needs no resampler: in the **Frequency Xlating FIR Filter**, set **Center Frequency** to -10000 and **Sample Rate** to 62500 to move channel A to the centre, and give AIS-catcher the rate 62500.

=== "Config file"

    Add `"channel": "X"` to the `receiver` entry.

=== "Command line"

    Add `-c X` to the command.

- **Several decoders:** a ZMQ PUB Sink serves every subscriber that connects. Several copies of AIS-catcher can decode one stream at the same time.
- **Every setting:** the ZMQ input is a kind of [TCP client](../configuration/input/tcp.md), and that page lists its settings, such as `endpoint`. On the command line, `-gz` sets them.
