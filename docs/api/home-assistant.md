# Home Assistant and MQTT state

!!! tip "Step-by-step guide"
    **[Vessels in Home Assistant](https://www.aiscatcher.org/guides/home-assistant)** on aiscatcher.org walks through this with screenshots: in the control panel, in the configuration file and on the command line.

AIS-catcher can keep its state on an MQTT broker: whether it is up, how many vessels it sees, how each station and receiver is doing, where the vessels you watch are, and each event as it happens. The state topics are retained, so whoever subscribes gets the latest at once. With discovery on, Home Assistant finds the sensors by itself; any other MQTT client reads the same topics.

```json
"mqtt_state": {
    "url": "mqtt://homeassistant.local:1883",
    "username": "ais",
    "password": "secret",
    "topic": "ais-catcher",
    "watch": [244123456]
}
```

In managed mode: **Services → Home Assistant**. On the command line, `-W` with the broker's url takes the same keys, a list comma-separated:

```bash
AIS-catcher -d 00000001 -W mqtt://homeassistant.local:1883 USERNAME ais PASSWORD secret WATCH 244123456
```

| Key | Default | Description |
|-----|---------|-------------|
| `url` | | The broker: `mqtt://`, `mqtts://`, `ws://` or `wss://`. Empty publishes nothing |
| `username`, `password` | | For the broker |
| `topic` | `ais-catcher` | Everything goes under this topic |
| `discovery` | `true` | Home Assistant discovery under `homeassistant/` |
| `watch` | | MMSIs whose position is published, each a device tracker in Home Assistant |
| `client_id` | the topic | The MQTT client id |

| Topic | Retained | Content |
|-------|----------|---------|
| `<topic>/availability` | yes | `online`, or `offline` when AIS-catcher stops; the broker says `offline` for it when the connection dies |
| `<topic>/state` | yes | `vessels`, `messages_per_minute`, `engine_running`, `receivers` |
| `<topic>/station/<id>` | yes | `name`, `online` (heard in the last five minutes), `vessels` heard in the last hour, `last_heard` |
| `<topic>/receiver/<n>` | yes | `state` (`streaming`, `stopped`, `lost`), `station`, `input`, `messages_per_minute` |
| `<topic>/vessel/<mmsi>` | yes | `latitude`, `longitude`, `name`, `speed_kn`, `in_range`, `last_seen` |
| `<topic>/event` | no | Each event as a [webhook](webhooks.md) gets it, with `event_type` for Home Assistant's event entity |

Station positions are not published here. The state is sent when it changes, at most every 10 seconds, and in full every minute.

In Home Assistant the device **AIS-catcher &lt;topic&gt;** then has: Vessels, Message rate, Receiving, and per station its online state and vessels, per receiver whether it streams, an Events entity to trigger automations on, and a device tracker per watched vessel.
