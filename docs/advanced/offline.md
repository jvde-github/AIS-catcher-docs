# Offline web viewer

There is an option to run the web viewer without relying on online libraries. This facilitates using the web interface whilst traveling without an internet connection. The steps are simple. First, go to your home directory (say `/home/jasper`) and clone the necessary offline web assets:
```bash
git clone https://github.com/jvde-github/webassets.git
```
This will create a directory `webassets` that we need to share with AIS-catcher as an alternative location for online web content  with the CDN argument followed by the location of the web assets directory:
```bash
AIS-catcher -N 8100 CDN /home/jasper/webassets
```
Offline maps can also be included in `mbtiles` format:
```bash
AIS-catcher  -N 8100 MBTILES filename.mbtiles
```
or as an overlay
```bash
AIS-catcher  -N 8100 MBOVERLAY filename.mbtiles
```

![image](https://github.com/user-attachments/assets/3a0282b5-8e16-4fe1-bedf-7a0e97d75674)
