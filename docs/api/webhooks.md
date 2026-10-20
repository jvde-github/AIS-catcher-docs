# Webhooks

A webhook posts each event to an address as it happens: a safety message, a new destination or status, a vessel arriving at or leaving a place, or something about the installation itself (the engine starting or stopping, a receiver losing its device or getting it back, a backup failing). Home Assistant, Node-RED, n8n and most automation tools take webhooks as they come.

```json
"webhooks": [
    { "url": "http://homeassistant.local:8123/api/webhook/ais-events", "events": ["safety", "place_enter", "place_exit"] },
    { "url": "https://example.org/hooks/ais", "events": ["system"], "secret": "whsec_…" }
]
```

In managed mode: **Services → Webhooks**. On the command line, `-W` takes the url and then the same keys, a list comma-separated; repeat it for more webhooks:

```bash
AIS-catcher -d 00000001 -W https://example.org/hooks/ais EVENTS safety,place_enter SECRET "$WEBHOOK_SECRET"
```

| Key | Description |
|-----|-------------|
| `url` | Where each event is posted, `http://` or `https://`. Redirects are not followed |
| `events` | The kinds posted: `safety`, `destination`, `status`, `draught`, `place_enter`, `place_exit`, `system`. Every kind when left out |
| `filter` | A ship's event only for ships that pass it, in the terms of a [server's filter](../usage/json-configuration.md#tracking-and-services-tracking-services) |
| `batch` | `true`: events that come together go in one request as `{"events": [...]}`, up to 100 |
| `secret` | Signs each request as [Standard Webhooks](https://www.standardwebhooks.com) does |
| `active` | `false` keeps the webhook in the file but sends nothing |

The body is the event as `/api/v1/events` gives it:

```json
{ "seq": 1532, "time": "2026-10-19T14:02:11Z", "kind": "place_enter", "level": "notice",
  "mmsi": 244123456, "name": "STORM", "place": "3f2c…", "text": "Rotterdam", "lat": 51.95, "lon": 4.06 }
```

and an event of the installation:

```json
{ "seq": 1533, "time": "2026-10-19T14:05:00Z", "kind": "system", "level": "urgent",
  "event": "receiver_lost", "text": "Receiver 1 lost its device", "receiver": 1, "station": 1 }
```

Every request carries `webhook-id` (the same on every try of one event, so a receiver can drop a repeat), `webhook-timestamp` and, with a `secret`, `webhook-signature`: `v1,` and the base64 HMAC-SHA256 of `id.timestamp.body` under the key. A secret starting with `whsec_` is the key in base64, as Standard Webhooks writes it; any other secret is the key itself. The libraries of [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) check it in one call.

A safety message is posted once, not every time it is broadcast: a beacon or a coast station repeats its text every minute or so for hours. While the same sender keeps sending the same text it is posted again after 30 minutes, or after 10 for a distress call. The same holds for `/api/v1/events`, MCP and the MQTT events; the viewer's ticker shows the repeats as a count.

An address that does not answer with 2xx is tried again from the event that failed: after 5 seconds, then 10, 30, a minute, and so on up to an hour between tries. The other webhooks go on meanwhile. A webhook starts at the newest event when AIS-catcher starts; events that happened while it was not running are in `/api/v1/events`.
