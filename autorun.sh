#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/

python3 youtube_m3ugrabber.py > ../youtube.m3u

echo m3u grabbed
