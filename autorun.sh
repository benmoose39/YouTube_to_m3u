#!/bin/bash

python3 -m pip install requests

cd scripts
chmod +x youtube_m3ugrabber.py
chmod +x ustvgo_m3ugrabber.py

./youtube_m3ugrabber.py > ../youtube.m3u
./ustvgo_m3ugrabber.py > ../ustvgo.m3u

echo m3u grabbed

