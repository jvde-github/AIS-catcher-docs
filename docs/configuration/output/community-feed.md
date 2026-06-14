# Community Feed

The Community Feed allows you to share received AIS messages with the AIS-catcher community.

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-X</span>
        [<span class="cmd-value">sharing_key</span>]
    </div>
</div>

On the CLI, `-X` enables sharing. If you provide a sharing key, the station is linked to your account; if omitted, sharing is anonymous.

In JSON configuration, Community Feed settings are configured via the root-level keys `sharing` and `sharing_key` (they are not part of an output array like `udp`).

## Live community map in the viewer

When the Visual Web Control is running, the community map is no longer drawn as an overlay on the local map. Opening the community map pops up a pane connected to [aiscatcher.org/livemap](https://aiscatcher.org/livemap). Pan and zoom are kept in sync in both directions, and vessels seen by the local receiver are pushed to the community view in real time.

The community-feed icon in the header indicates the current sharing state at a glance:

- **Red** — sharing is off (no data leaves the station)
- **Orange** — sharing is on, anonymously (no `sharing_key` set)
- **Green** — sharing is on and the station is identified by a `sharing_key`

## Summary Settings

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">sharing</span> | boolean | <span class="cmd-value">false</span> | Enable community feed sharing (CLI equivalent: `-X`) |
| <span class="cmd-setting">sharing_key</span> | string | <span class="cmd-value">-</span> | Optional sharing key to associate your station with aiscatcher.org (CLI: `-X <key>`) |
| <span class="cmd-setting">sharing_zone</span> | string | <span class="cmd-value">-</span> | Optional zone tag included with shared messages |
</div>