#!/bin/bash

python3 -m pip install requests

python3 scripts/youtube_m3ugrabber.py > youtube.m3u
python3 scripts/ustvgo_m3ugrabber.py > ustvgo.m3u

echo m3u grabbed
