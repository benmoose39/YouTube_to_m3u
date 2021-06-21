#!/bin/bash

python3 -m pip install requests

cd scripts/

python3 youtube_m3ugrabber.py > ../youtube.m3u
python3 ustvgo_m3ugrabber.py > ../ustvgo.m3u

echo m3u grabbed
