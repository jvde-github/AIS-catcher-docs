# Web Viewer

<div class="command-container">
      <div class="command-syntax">
        <span class="cmd-name">AIS-catcher</span>
        <span class="cmd-flag">-N</span>
        <span class="cmd-value">port</span> 
        [<span class="cmd-setting">setting</span> <span class="cmd-value">value</span>]
        ...
    </div>
</div>


![image](https://github.com/jvde-github/AIS-catcher/assets/52420030/54eea1c6-2f72-4c23-91c4-dd289753d4cc)

AIS-catcher includes a simple web interface. A live demo is available for [East Boston, US](https://kx1t.com/ais/). The web interface gratefully uses the following libraries: [chart.js](https://www.chartjs.org/docs/latest/charts/line.html), chart.js [annotation plugin](https://www.chartjs.org/chartjs-plugin-annotation/latest/), [leaflet](https://leafletjs.com/), [Material Design Icons](https://m3.material.io/styles/icons/overview), tabulator, [marked](https://github.com/markedjs/marked) and [flag-icons](https://github.com/lipis/flag-icons). 

Make sure you use the latest version and start the web viewer as follows:
```bash
AIS-catcher -N 8100
```
where ``8100`` is the port number. If your machine network name is raspberrypi, e.g.,  then enter ``raspberrypi:8100`` in your browser.  On the web page, you will find several sections with information related to the station and received messages.

For users wishing to include a station name and a link to an external website in the Statistics section:
```bash
AIS-catcher -N STATION Southwood STATION_LINK http://example.com
```
This could be a useful option if you want to offer the interface externally. To display the reception range and distances from your station, provide the program with the station coordinates and permission to share the location with the web viewer:
```bash
AIS-catcher -N LAT 50 LON 3.141592 SHARE_LOC on
```
The last option `share_loc` (default is off) will allow the web viewer to access and display the location.

 The user can make a page in [markdown format](https://www.markdownguide.org/basic-syntax/). The content will be shown in the About tab of the web viewer:
```bash
AIS-catcher -N 8100 ABOUT about.md
```
All these options can be captured in the configuration file (in a section with name ``server``), see below. 

## Menu structure

The main menu behind the hamburger icon in the top left corner navigates between different functional areas. Context-sensitive menus, accessible through right-click, long press on iOS, or the vertical dot icon on the map, offer more functionalities. Here you can set options like activating the "dark mode" theme, displaying the station range on the map, locking/unlocking the map center, toggling text-only ship labels, decluttering ship labels, and viewing details of the last message received from a vessel, amongst others.

## Visualization

When AIS-catcher receives data containing a vessel's dimensions but can not determine the direction it is pointing (heading), it will display a circle that accommodates the ship's dimensions regardless of heading. Missing heading information is common for Class B ships. If there's a decent approximation available for the heading, such as course-over-ground above certain speeds, it will be used. Shapes plotted using this approximation will have a dashed border, indicating incomplete information. An example is the USS Constitution docked in Boston.

<p align="center">
  <img src="https://user-images.githubusercontent.com/52420030/219856857-e0965190-1468-47b6-88ad-423b77c455ff.png" width="50%"/>
</p>

In the map section, clicking on a vessel will open a  **ship card** with details of the vessel. For smaller screens it can be minimized in the top bar (via the `^` symbol or by clicking on the header bar). The ship card will open minimized on mobile devices. In its maximized form, users can choose which rows will be visible in the minimized state. Additional options, such as looking up the vessel on aggregator sites, are available by clicking the three-dot icon on the ship card header.

## Validation
The web-interface shows a "validation" indication at the left border of the ship card header.
<p align="center">
  <img src="https://user-images.githubusercontent.com/52420030/212470486-8987fa96-5324-41d8-a782-dbcbdc18aca0.png" width="25%"/>
</p>

AIS-catcher analyzes an enormous stream of bits per day for both AIS channels (2 to the power 33 to be precise). To avoid erroneous messages, the AIS system employs a 16-bit CRC and matching of other bit patterns. Unfortunately, purely statistically this cannot prevent that there will be an occasional technically correct but nonsense message. These are typically easy to recognize (e.g. looking at the signal level, and location on the map) and aggregator sites like MarineTraffic will filter these out. 

To reliably measure the reception range for the station in the web interface, AIS-catcher has implemented a "validation function" that checks the location of the vessel for consistency between messages and flags if there is an inconsistency. Practically speaking, if we receive a position from an MMSI that is relatively close to the last received position, the "validation" indicator will be green and the distance to the station will be included to determine the station range. Please note that messages within 50 NMi from the receiving station will always be included for range setting. The validation indicator will be grey if validation for the location cannot be performed and red if it is not successful. 

## Plots
The Plot section contains several visualizations to assess the performance of the receiver:

<p align="center">
  <img src="https://user-images.githubusercontent.com/52420030/219856922-33404fe8-dc54-4bc2-a1a6-84f4ce5dd72a.png" width="50%"/>
</p>
 Restarting AIS-catcher typically erases history in the graphs. To retain plot "state" and backup the information to a file use the following:

```bash
AIS-catcher -N 8100 FILE stat.bin BACKUP 10
```
This will back up the plots when the program closes and every 10 minutes in a file `stat.bin`. The minimum backup interval is 5 minutes.

## Custom plugins and styles...

To give the user the option to tweak the look-and-feel and functionality of the web viewer and/or modify for example the color scheme or regional preferences, the program provides the option to inject custom plugins (JavaScript) and CSS into the website, with a command like:
```bash
AIS-catcher -N 8100 PLUGIN plugin1.js PLUGIN plugin2.js STYLE mystyle.css
```
You can also include all plugin files from a specific directory using the command:
```bash
AIS-catcher -N 8100 PLUGIN_DIR /usr/share/aiscatcher/plugins
```
Files need to have the extension ``.pjs`` and ``.pss`` for respectively JavaScript and CSS style plugins. The repository includes a few example plugins that demonstrate how to add additional maps or cater to regional preferences. Examples of plugins can be found in [another](https://github.com/jvde-github/AIS-Catcher-PLUGINS) GitHub repository.

## Offline web viewer
There is an option to run the web viewer without relying on online libraries. This facilitates using the web interface whilst traveling without an internet connection. The steps are simple. First, go to your home directory (say `/home/jasper`) and clone the necessary offline web assets:
```bash
git clone https://github.com/jvde-github/webassets.git
```
This will create a directory `webassets` that we need to share with AIS-catcher as an alternative location for online web content  with the CDN argument followed by the location of the web assets directory:
```bash
AIS-catcher -x 192.168.1.120 4002 -N 8100 CDN /home/jasper/webassets
```

## Sending data to Prometheus for use in Grafana dashboards

You can add the option `PROME on` to the web configuration command to start rendering Prometheus-compatible statistics at `/metrics`. For example:

```bash
AIS-catcher -N 8100 PROME on
```

For more information on how to configure Prometheus and Grafana to get an initial dashboard, see [README-grafana.md](../../advanced/grafana.md).

## Summary Settings

Server Options:

<div class="input-table" markdown>
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| <span class="cmd-setting">PORT</span> | integer | <span class="cmd-value">-</span> | Single port for web server |
| <span class="cmd-setting">PORT_MIN</span> | integer | <span class="cmd-value">-</span> | Minimum port in binding range |
| <span class="cmd-setting">PORT_MAX</span> | integer | <span class="cmd-value">-</span> | Maximum port in binding range |
| <span class="cmd-setting">IP_BIND</span> | string | <span class="cmd-value">-</span> | Server binding IP address |
| <span class="cmd-setting">REUSE_PORT</span> | boolean | <span class="cmd-value">false</span> | Enable port reuse |
| <span class="cmd-setting">ZLIB</span> | boolean | <span class="cmd-value">true</span> | Enable response compression |
| | | | |
| Location Settings | | | |
| <span class="cmd-setting">LAT</span> | float | <span class="cmd-value">-</span> | Station latitude |
| <span class="cmd-setting">LON</span> | float | <span class="cmd-value">-</span> | Station longitude |
| <span class="cmd-setting">SHARE_LOC</span> | boolean | <span class="cmd-value">false</span> | Share station location |
| <span class="cmd-setting">USE_GPS</span> | boolean | <span class="cmd-value">false</span> | Use GPS data |
| <span class="cmd-setting">OWN_MMSI</span> | integer | <span class="cmd-value">-</span> | Own vessel MMSI |
| | | | |
| Data Management | | | |
| <span class="cmd-setting">HISTORY</span> | integer | <span class="cmd-value">-</span> | History retention (5-43200 sec) |
| <span class="cmd-setting">CUTOFF</span> | integer | <span class="cmd-value">-</span> | Data retention threshold (0-10000) | 
| <span class="cmd-setting">BACKUP</span> | integer | <span class="cmd-value">-1</span> | Backup interval (5-2880 min) |
| <span class="cmd-setting">FILE</span> | string | <span class="cmd-value">-</span> | Statistics file path |
| <span class="cmd-setting">REALTIME</span> | boolean | <span class="cmd-value">false</span> | Enable real-time updates |
| | | | |
| Output Formats | | | |
| <span class="cmd-setting">KML</span> | boolean | <span class="cmd-value">false</span> | Enable KML output |
| <span class="cmd-setting">GEOJSON</span> | boolean | <span class="cmd-value">false</span> | Enable GeoJSON output |
| <span class="cmd-setting">PROME</span> | boolean | <span class="cmd-value">false</span> | Enable Prometheus metrics |
| <span class="cmd-setting">MESSAGE</span> | boolean | <span class="cmd-value">false</span> | Enable message saving |
| | | | |
| UI Customization | | | | 
| <span class="cmd-setting">STATION</span> | string | <span class="cmd-value">-</span> | Station display name |
| <span class="cmd-setting">STATION_LINK</span> | string | <span class="cmd-value">-</span> | Station info URL |
| <span class="cmd-setting">CDN</span> | string | <span class="cmd-value">-</span> | Local CDN resources path |
| <span class="cmd-setting">PLUGIN</span> | string | <span class="cmd-value">-</span> | JavaScript plugin path |
| <span class="cmd-setting">STYLE</span> | string | <span class="cmd-value">-</span> | CSS style path |
| <span class="cmd-setting">PLUGIN_DIR</span> | string | <span class="cmd-value">-</span> | Plugins directory |
| <span class="cmd-setting">ABOUT</span> | string | <span class="cmd-value">-</span> | About page path |
</div>