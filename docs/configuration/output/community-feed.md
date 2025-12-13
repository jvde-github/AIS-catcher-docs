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

## Summary Settings

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">sharing</span> | boolean | <span class="cmd-value">-</span> | Enable community feed sharing (CLI equivalent: `-X`) |
| <span class="cmd-setting">sharing_key</span> | string | <span class="cmd-value">-</span> | Optional sharing key to associate your station with aiscatcher.org (CLI: `-X <key>`) |
</div>