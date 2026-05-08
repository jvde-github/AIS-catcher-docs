# Python — `aiscat`

[`aiscat`](https://pypi.org/project/aiscat/) is a Python package that exposes the AIS-catcher decoder as a library. Output dictionaries match the [AIS-catcher JSON format](../references/JSON-decoding.md) field-for-field, so anything you've built around the documented JSON output works the same when the source becomes a Python iterator.

It is built for fast, complete decoding of AIS NMEA from Python: all standard message types (1–28), multi-part AIVDM reassembly, country-code resolution from MMSI prefix, lookup-table text fields populated from the same tables AIS-catcher uses, and decoding of binary application messages (type 6 and 8 ASMs across IMO, IALA, USA, and inland-waterway DAC/FID payloads).

## Install

```bash
pip install aiscat
```

Pre-built wheels are published on PyPI for Linux (x86_64, aarch64, armv7l), macOS (Apple Silicon), and Windows (x86_64, ARM64), Python 3.9–3.14.

## Quickstart

One-shot decoding:

```python
import aiscat

aiscat.decode("!AIVDM,1,1,,A,15MgK45P3@G?fl0E`JbR0OwT0@MS,0*4E")
# {'type': 1, 'mmsi': 366730000, 'channel': 'A', 'rxuxtime': 1777739134.027,
#  'lat': 37.803802, 'lon': -122.392532, 'speed': 20.8, 'course': 51.3,
#  'status': 5, 'status_text': 'Moored', ...}
```

Streaming from a file, stdin, TCP, or UDP source — the helpers wire up the I/O loop and yield decoded messages:

```python
for msg in aiscat.from_file("session.nmea"):
    print(msg["mmsi"], msg["lat"], msg["lon"])

for msg in aiscat.from_tcp("ais.example.com", 4001):
    handle(msg)
```

For full control, use `Decoder` directly: `feed(bytes)` parses NMEA / JSON / binary input out of the buffer, and `next()` pops one decoded message.

## Output formats

The `format=` kwarg selects what `next()` (and the helpers) return. Dict-shaped formats are convenient for in-Python consumption; bytes-shaped formats skip the `dict` allocation and are several times faster — useful when forwarding the data to a file, socket, database, or another AIS-catcher instance.

| Format | Returns | Equivalent to | Notes |
|---|---|---|---|
| `"dictionary"` *(default)* | `dict` | AIS-catcher `-o 5` (parsed) | Full decoded fields. |
| `"annotated"` | `dict` | AIS-catcher `-o 6` (parsed) | Each scalar wrapped as `{value, unit, description, text}`. |
| `"json"` | `bytes` | AIS-catcher `-o 5` | Full decoded JSON, ready to write/send. |
| `"json_nmea"` | `bytes` | AIS-catcher `-o 3` | Slim JSON envelope wrapping the original NMEA — the relay/passthrough format. |
| `"nmea"` | `bytes` | AIS-catcher `-n` / `-o 1` | The raw AIVDM/AIVDO line(s). |
| `"nmea_tag"` | `bytes` | — | NMEA prefixed with an IEC 61162-450 tag block carrying source + timestamp. |
| `"binary"` | `bytes` | — | AIS-catcher's native 0xac binary packet format (compact, suitable for inter-process transport). |

## When to use it

For live decode of a single station (~50 msg/s) any AIS library is fast enough. `aiscat` earns its keep when throughput matters: historical replay, multi-receiver aggregation, batch analysis, and research workloads on millions to billions of messages. On a single Apple M-series core it tracks the native AIS-catcher CLI within ~13 % (≈1.9 M msg/s for `dictionary` output, ≈6 M msg/s for `nmea`/`binary`).

## More

- Source, examples (CSV, MQTT, Kafka, TCP relay), benchmarks, and the full API reference: [github.com/jvde-github/AIS-catcher/tree/main/python](https://github.com/jvde-github/AIS-catcher/tree/main/python)
- Licence is GPLv3, inherited from AIS-catcher.
