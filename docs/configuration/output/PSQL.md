# Writing AIS messages to a database

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-D</span>
        <span class="cmd-value">connection string</span>
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>

AIS-catcher can write decoded messages to a database. Three backends are supported and all three write the same tables with the same settings:

| backend | for |
| :--- | :--- |
| **PostgreSQL** | a shared or networked database |
| **SQLite** | a local file, no server to run |
| **CSV** | plain files, no database at all |

All three are compiled into the official packages and the Docker image, so there is nothing to install or rebuild. If you build from source, `libpq-dev` and `libsqlite3-dev` need to be present at configure time; the `PSQL` and `SQLITE` CMake options are on by default. CSV has no dependency.

On the command line the backend follows from the connection string. A plain string is a PostgreSQL connection; a `sqlite:` or `csv:` prefix selects the other two:

```bash
AIS-catcher -D dbname=ais
AIS-catcher -D sqlite:/var/lib/ais/ais.db
AIS-catcher -D csv:/var/log/ais/
```

!!! warning "Schema change"
    The schema was reorganised and the old per-message-type tables (`ais_vessel_pos`, `ais_basestation`, `ais_sar_position`, `ais_aton`, `ais_vessel_static`, `ais_vessel`, `ais_property`, `ais_keys`) were replaced. The settings that selected them (`v`, `msgs`, `vp`, `vs`, `bs`, `sar`, `aton`) were removed and now produce an error naming their replacement. Run the new `create_pg.sql` to migrate; it drops the old tables for you.

## Setting up

=== "PostgreSQL"

    Create an empty database, e.g. on Ubuntu:
    ```bash
    sudo -u postgres createdb ais
    ```
    Create the tables:
    ```bash
    sudo -u postgres psql ais < create_pg.sql
    ```
    Make sure the user running AIS-catcher may write to the database, or give credentials in the connection string:
    ```bash
    AIS-catcher -D postgresql://[user[:password]@][netloc][:port][/dbname]
    ```

=== "SQLite"

    Create the file and its tables in one step:
    ```bash
    sqlite3 /var/lib/ais/ais.db < create_sqlite.sql
    ```
    No server, no user setup. The file is created if it does not exist, but the tables are not, so run the script first.

=== "CSV"

    Point it at a directory that already exists and is writable **by the user AIS-catcher runs as** — the managed/systemd install runs as `aiscatcher`, which cannot write into a home directory:
    ```bash
    sudo mkdir -p /var/lib/ais-catcher/csv
    sudo chown aiscatcher: /var/lib/ais-catcher/csv
    ```
    The files then appear on the first flush:
    ```
    ais_message-2026-08-08.csv
    ais_position-2026-08-08.csv
    ais_static-2026-08-08.csv
    ais_state.csv
    ais_stats_hourly.csv
    ```
    The three logs rotate daily, so deleting old files is how retention works. `ais_state.csv` and `ais_stats_hourly.csv` are rewritten whole on each flush rather than appended, because a per-MMSI row is merged in place and an hourly bucket is corrected until its hour ends.

The two SQL scripts live in the `DBMS` directory of the source tree, or in `/etc/AIS-catcher/DBMS` if you installed from a package or with the install script.

## Tables

| Table | Description | Setting | Default |
| :--- | :--- | :--- | :--- |
| `ais_state` | one row per MMSI with the latest known values, merged across every message type, plus counters | `state` | **on** |
| `ais_stats_hourly` | reception statistics per hour: message and vessel counts, per channel counts, signal level range | `stats` | **on** |
| `ais_message` | one row per received message with its metadata, and the raw sentences when `nmea` is on | written when any of `position`, `static` or `nmea` is on | |
| `ais_position` | dynamic fields from types 1, 2, 3, 4, 9, 18, 19, 21 and 27 | `position` | off |
| `ais_static` | static and voyage fields from types 5, 19, 21 and 24 | `static` | off |

**Only `ais_state` and `ais_stats_hourly` are written by default**, and neither grows without bound: the first holds one row per distinct MMSI, the second one row per hour. A default install can therefore be left running indefinitely without filling the disk.

`position` and `static` are the history tables and are opt-in, because they grow with every message received. `ais_position` for a single MMSI, ordered by time, is that vessel's track.

`ais_message` is written whenever any of the three needs it, since `ais_position` and `ais_static` hold only payload columns and reference it through `msg_id`. Deleting from `ais_message` cascades to both.

Retention is built in: set `retention` to a number of days and every backend prunes daily — the SQL backends delete expired messages, stats and state rows in small chunks, CSV deletes expired daily log files and stats hours. The default `0` keeps everything.

## Controlling volume

The history tables can produce a lot of rows. The message filter settings apply to `-D` like any other output and are the intended way to keep them manageable:

```bash
AIS-catcher -D dbname=ais position on unique on position_interval 60
```

`unique on` drops messages repeated within three seconds, and `position_interval 60` keeps at most one position per MMSI per minute. On a busy capture the two together reduced stored positions by around 95% while leaving tracks perfectly usable.

## Configuration file

All backends share the `db` key and name themselves with `type`. It is an array, so several can run at once:

```json
{
    "db": [
        {
            "active": true,
            "type": "postgres",
            "conn_str": "dbname=ais",
            "station_id": 17,
            "position": true,
            "static": true
        },
        {
            "active": true,
            "type": "sqlite",
            "conn_str": "/var/lib/ais/ais.db",
            "position": true,
            "position_interval": 60
        }
    ]
}
```

`type` defaults to `postgres`. The `sqlite:` and `csv:` prefixes are a command-line convenience only — in a configuration file `type` already says which backend it is, so `conn_str` is just the path or connection string.

## Examples

Default, a bounded snapshot and hourly statistics only:
```bash
AIS-catcher -D dbname=ais station_id 17
```

Full history to a local file, thinned to one position per vessel per minute:
```bash
AIS-catcher -D sqlite:ais.db position on static on position_interval 60
```

Everything including raw sentences:
```bash
AIS-catcher -D dbname=ais position on static on nmea on
```

The `station_id` setting is optional and stamps every row, so several feeders can share one database.

A failing database never stops the receiver, even when it is unavailable at startup: the output keeps retrying with exponential backoff (up to five minutes between attempts), reconnects and re-prepares its statements when the database returns, and drops only its own oldest queued messages in the meantime.

## Summary Settings

<div class="input-table" markdown>
| Setting (JSON key / CLI setting name) | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">type</span> | enum | <span class="cmd-value">postgres</span> | Backend: `postgres`, `sqlite` or `csv` (configuration file only) |
| <span class="cmd-setting">conn_str</span> | string | <span class="cmd-value">dbname=ais</span> | libpq connection string, SQLite file path, or CSV directory |
| <span class="cmd-setting">station_id</span> | integer | <span class="cmd-value">0</span> | Station identifier stamped on every row, lets multiple feeders share one database |
| <span class="cmd-setting">interval</span> | integer | <span class="cmd-value">60</span> | Database write interval in seconds (5-1800) |
| <span class="cmd-setting">groups_in</span> | integer | <span class="cmd-value">all</span> | Bitmask of input groups feeding this output |
| | | | |
| Table Options | | | |
| <span class="cmd-setting">state</span> | boolean | <span class="cmd-value">true</span> | Latest known values per MMSI, bounded by the number of distinct targets |
| <span class="cmd-setting">stats</span> | boolean | <span class="cmd-value">true</span> | Hourly reception statistics |
| <span class="cmd-setting">position</span> | boolean | <span class="cmd-value">false</span> | Log position reports, grows with traffic |
| <span class="cmd-setting">static</span> | boolean | <span class="cmd-value">false</span> | Log static and voyage reports, grows with traffic |
| <span class="cmd-setting">nmea</span> | boolean | <span class="cmd-value">false</span> | Store the raw sentences alongside each message |
| <span class="cmd-setting">retention</span> | integer | <span class="cmd-value">0</span> | Days of history kept, pruned daily; 0 keeps everything |
| | | | |
| CSV Only | | | |
| <span class="cmd-setting">capacity</span> | integer | <span class="cmd-value">8192</span> | Targets kept in `ais_state.csv` before the least recently heard is dropped |
</div>

!!! note "CSV differences"
    `ais_state.csv` is bounded by `capacity` and recycles the least recently heard target, where the SQL backends keep a row per MMSI indefinitely. Message ids restart with the process, which is why the log files carry a date. Newlines inside a multipart sentence are written as spaces so every record stays one line.

    The state and stats tables are journalled: changes are appended to a `.csv.journal` sidecar and merged back into the always-deduplicated main file at startup, at clean shutdown and at the day rollover. After a crash the journal is simply replayed, so at most the final line of it can be lost.
