#!/bin/bash

python3 -m pip install requests

cat info.txt > 24.m3u

chmod +x m3ugrabber.py
./m3ugrabber.py >> 24.m3u

echo m3u grabbed
