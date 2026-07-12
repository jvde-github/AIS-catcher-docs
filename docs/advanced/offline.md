# Offline web viewer

The web viewer works without an internet connection out of the box: all web assets (libraries, styles and fonts) are baked into the AIS-catcher executable. This facilitates using the web interface whilst traveling without an internet connection.

!!! note "Deprecated: CDN setting"
    Older versions relied on online libraries and offered the `CDN` setting to point at a locally cloned copy of the web assets. This is deprecated — no separate download is needed anymore.

The one thing that still requires a connection is the background map. For a fully offline experience, include offline maps in `mbtiles` format:

```bash
AIS-catcher -N 8100 MBTILES filename.mbtiles
```

or as an overlay:

```bash
AIS-catcher -N 8100 MBOVERLAY filename.mbtiles
```

![image](https://github.com/user-attachments/assets/3a0282b5-8e16-4fe1-bedf-7a0e97d75674)
