# Places

A place is a named piece of the map: a port, a berth, an anchorage, a stretch of water, or a zone you want to keep an eye on. Give AIS-catcher a directory of place files and the web viewer will show them on the map, tell you which ships are in each one, keep a record of every ship's visits, and announce arrivals and departures.

Places are optional. Without a place directory the viewer works as before.

## Switching places on

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-N</span>
        <span class="cmd-value">8100</span>
        <span class="cmd-setting">PLACES</span>
        <span class="cmd-value">/path/to/places</span>
    </div>
</div>

On the command line, `PLACES` is a setting of the web viewer (`-N`). In a JSON configuration it is the key `places` of the `server` object.

In managed mode, open the **Places** tab of the dashboard. The first time, it asks whether to enable places and creates a `places` directory beside the configuration file. The directory can be changed later under the viewer's settings (**Storage → Place Directory**).

## What you get

- **On the map.** Every place has a marker, and its outline appears when you point at it. Large ports show from far out, berths only close in (see [Place types](#place-types)).
- **On a ship's card.** The card says where the ship is now ("Gate Terminal") and lists its recent visits with entry time, exit time and duration.
- **On a place.** Clicking a marker opens the ships of that place, in tabs: **Inside**, **Left**, **Arrived**, **Visits**, **Nearby**, and for a port **Expected**, the ships that report it as their destination.
- **In the ticker.** A ship entering or leaving a port, a guard zone, a sector or a water is announced.

## A place file

A place is a GeoJSON Feature in a file ending in `.geojson`. This is a complete one:

```json
{
  "type": "Feature",
  "id": "0f2e6b1a-3c4d-4e5f-8a9b-0c1d2e3f4a5b",
  "properties": {
    "schema_version": 3,
    "revision": 1,
    "name": "Kade 1",
    "place_type": "berth"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[4.05, 52.05], [4.06, 52.05], [4.06, 52.06], [4.05, 52.05]]]
  }
}
```

One place per file is the usual layout, with the file named after the place's `id`. A file may also be a `FeatureCollection` holding many places. Coordinates are longitude, then latitude, in WGS84.

And a port with everything a port usually carries:

```json
{
  "type": "Feature",
  "id": "b47898d6-5dfc-4334-88a0-ad1ff96355ff",
  "properties": {
    "schema_version": 3,
    "revision": 1,
    "name": "Rotterdam",
    "place_type": "port",
    "codes": { "unlocode": ["NLRTM"] },
    "aliases": ["Rotterdam Europoort"],
    "rank": 3
  },
  "geometry": { "type": "Polygon", "coordinates": [[[3.95, 51.88], [4.55, 51.88], [4.55, 52.0], [3.95, 52.0], [3.95, 51.88]]] }
}
```

## Properties

The same rules are published as a JSON Schema in the source tree, [`frontend/packages/core/place.schema.json`](https://github.com/jvde-github/AIS-catcher/blob/main/frontend/packages/core/place.schema.json), for tools that write place files.

<div class="input-table" markdown>

| Property | Required | Description |
|---------|------|-------------|
| <span class="cmd-setting">id</span> | yes | A UUID in lowercase. It is the place's identity: the name, the type and the outline may all change, the `id` never does. Generate one with `uuidgen` (and lowercase it) or `python3 -c "import uuid; print(uuid.uuid4())"`. It sits beside `properties`, not inside it. |
| <span class="cmd-setting">schema_version</span> | yes | Always <span class="cmd-value">3</span>. |
| <span class="cmd-setting">revision</span> | yes | <span class="cmd-value">1</span> in a file you write yourself. The editor raises it on every save. |
| <span class="cmd-setting">name</span> | yes | Up to 120 characters. |
| <span class="cmd-setting">place_type</span> | yes | One of the [place types](#place-types). |
| <span class="cmd-setting">part_of</span> | no | The `id` of the place this one lies in: a berth in its terminal, a terminal in its port. |
| <span class="cmd-setting">codes</span> | no | Codes by scheme, each a list. `unlocode` is the one AIS-catcher uses: only a port may have it, and no two places may claim the same code. Other schemes are kept as written. |
| <span class="cmd-setting">aliases</span> | no | Other names of a port, up to 64, matched against the destinations ships report. |
| <span class="cmd-setting">category</span> | no | A free label of up to 60 characters, such as `sea`, `strait` or `restricted`. Shown in place of the type name for guard zones, sectors and waters. |
| <span class="cmd-setting">rank</span> | no | <span class="cmd-value">0</span> to <span class="cmd-value">3</span>: how prominent the place is on the map. See [Place types](#place-types). |
| <span class="cmd-setting">country</span> | no | Two capital letters. Without it a port takes the first two letters of its UN/LOCODE, and any other place the country of what it is part of. |
| <span class="cmd-setting">redirect_to</span> | no | The `id` of the place that replaced this one. See [Changing the catalogue](#changing-the-catalogue). |
| <span class="cmd-setting">no</span> | no | A number the editor gives a place on its first save and never changes. Leave it out of files you write yourself. |

</div>

Anything else you put in `properties` (an `attributes` object with notes, a source, references) is kept exactly as written and ignored by AIS-catcher, so a place file can also carry your own documentation.

## Place types

The type decides three things: whether a stay needs the ship to stop before it counts, whether a crossing is announced in the ticker and at which level, and from which zoom the marker shows.

<div class="input-table" markdown>

| Type | For | A visit needs a stop | Announced | Marker from zoom |
|---------|------|------|------|-------------|
| <span class="cmd-setting">berth</span> | One place alongside | yes | no | 14 |
| <span class="cmd-setting">mooring</span> | Buoys, dolphins, a mooring field | yes | no | 12 |
| <span class="cmd-setting">terminal</span> | A terminal, a yard, a quay with one operator | yes | no | 12 |
| <span class="cmd-setting">marina</span> | A yacht harbour | yes | no | rank-based |
| <span class="cmd-setting">anchorage</span> | Where ships wait at anchor | yes | no | rank-based |
| <span class="cmd-setting">section</span> | A basin or district of a port | yes | no | 13 |
| <span class="cmd-setting">port</span> | The port as a whole | yes | routine | rank-based |
| <span class="cmd-setting">guardzone</span> | Any zone you draw to be told who enters and leaves | no | notice | rank-based |
| <span class="cmd-setting">sector</span> | A traffic or VTS sector | no | routine | rank-based |
| <span class="cmd-setting">water</span> | A sea, strait, lake, river or canal | no | routine | no marker |

</div>

The ticker has three levels. A **routine** event is shown in its turn. A **notice** is marked with ⚠ and holds the strip longer: that is what a ship entering or leaving a guard zone gets, since a guard zone is what you asked to be told about. **Urgent** is kept for distress messages and never used for places.

Rank-based means the place's own `rank` decides: 3 shows the marker from zoom 7, 2 from zoom 9, 1 from zoom 11 and 0 (the default) from zoom 12. Give an anchorage the rank of its port if the two should appear together. The types with a fixed zoom ignore `rank`. A place with a drawn outline shows its marker from zoom 10 at the latest, whatever its rank. A water has no marker: its outline is drawn when you select it, for example from a ship's card.

Where a ship is inside several places at once, the card names them in the order of the table: the berth before the terminal, the terminal before the port, the port before the water, and the smaller place first among two of the same type.

## Outlines

`geometry` is a `Polygon`, a `MultiPolygon`, or a `Point`.

- A **polygon** is what makes a place work: ships are inside it or not. Each ring is closed (the last position repeats the first), has at least three corners, and does not cross or touch itself. A hole lies inside its polygon.
- A **multipolygon** is one place in several parts, such as a port on both banks of a river.
- A **point** gives a marker and nothing more. No ship is ever inside a point, so it has no visits; its dialog shows the ships nearby and, for a port, the ships bound for it.
- An outline that crosses the 180° meridian is split there into two parts.

A place holds up to 2,000 corners. A water may be larger: 2,000 per part and 16,000 in all. One place is limited to 512 KiB, the whole catalogue to four million corners.

## How visits are counted

- **A position has to be believable.** Only a validated position is used: one the ship can have reached from its previous one at no more than 60 knots, and, for a ship that reported itself stopped, one no more than 200 m from where it lay minutes before. A position that does not fit is left out; if the next one agrees with it, the ship really has moved and carries on from there. A single corrupted message with a wrong MMSI, a jump across the map, or an old position delivered late therefore never puts a ship in your port or takes it out of its berth.
- **A crossing is confirmed by the next position.** A ship enters when two positions in a row, at least ten seconds apart, are inside; the entry time is that of the first. Leaving works the same way, and one stray position across the line changes nothing.
- **Silence does not end a stay.** A ship that reports again after an hour or more is taken as found: if it is still inside, the stay goes on with its original entry time; if it has gone, the stay ended at the last position inside. No crossing time is made up for what nobody saw: in a place's list of ships such a time is shown as a bound, with `<` or `>`.
- **A call needs a stop.** At a port and everything in it, a stay counts as a call once the ship has been seen stopped for a minute: slower than 0.5 knots, or slower than 1 knot while reporting itself moored or at anchor. A ship steaming through a port without stopping leaves no call behind. In a guard zone, a sector or a water every passage counts.
- **Ten visits per ship** are kept: the places it is in now and its most recent calls. When the viewer keeps a backup file, they are saved in it and survive a restart.

## Destinations

A ship's reported destination is matched to your ports: first by UN/LOCODE, then by a name or alias that fits exactly one port. Matching ignores case, spaces and punctuation, and never guesses from part of a name. The **Expected** tab of a port lists the ships that match and are not yet inside.

## Changing the catalogue

In managed mode the **Places** tab is an editor: draw or reshape an outline, set the type and the port a place belongs to. A save takes effect at once, on the map and for every ship inside the changed outline.

**Import place** takes a GeoJSON Feature from anywhere. What it recognises is carried over (the name, the type, codes, the port a place belongs to, category and rank, in their current or an older spelling), everything else in the file is kept, and a Feature that says nothing about itself becomes a guard zone. The result opens for review and is stored when you save. **Import shape** and **Paste shape** replace only the outline of the place you are editing.

Files you edit by hand are read when AIS-catcher starts. There is no file watcher, so restart after changing them. A file that breaks a rule is skipped whole and the log says why:

```
Places: skipped 0f2e6b1a-3c4d-4e5f-8a9b-0c1d2e3f4a5b.geojson: Polygon edges cross or touch themselves
Places: loaded 412 definitions from /etc/AIS-catcher/places
```

Files written by earlier releases, with `schema_version` 1 or 2, load as they are. An `area` or a `custom` place is read as a guard zone, `size` as `rank` and `area_subtype` as `category`, and a port named by its UN/LOCODE becomes the place's parent once every file is loaded. The file itself changes only when the place is next saved in the editor, which writes it as schema 3. To convert a whole directory at once, run `scripts/migrate-places.py` from the source tree.

Two things to know before removing a place:

- **Deleting** a place also deletes the visits ships made to it.
- **Replacing** it keeps them. Leave the old file where it is and add `"redirect_to": "<id of the new place>"` to its properties. The old place disappears from the map, and its visits, including stays under way, continue at the new one. Use this when two outlines of the same place are merged into one.

## Summary Settings

<div class="input-table" markdown>

| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">places</span> | string | <span class="cmd-value">-</span> | Directory of place files for the web viewer (CLI: `-N <port> PLACES <directory>`; managed mode: `control.viewer.places`) |
| <span class="cmd-setting">place_geometry</span> | boolean | <span class="cmd-value">on</span> | Serve each place's outline to the map. Off keeps the outlines private to this installation: markers, lists and visits still work (CLI: `-N <port> PLACE_GEOMETRY off`) |

</div>
