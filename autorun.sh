#!/bin/bash

python3 -m pip install requests

echo "#EXTM3U" > link.m3u
echo "#EXTINF:-1 tvg-logo=\"https://www.twentyfournews.com/wp-content/themes/nextline_v3/images/logo-new.png\" tvg-chno=\"1\" group-title=\"Malayalam \(TataSky\)\",24 News Malayalam\" >> link.m3u

chmod +x m3ugrabber.py
./m3ugrabber.py >> link.m3u

echo "m3u grabbed"
