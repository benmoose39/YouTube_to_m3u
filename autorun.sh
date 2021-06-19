#!/bin/bash

python3 -m pip install requests

cd scripts
chmod +x m3ugrabber.py
./m3ugrabber.py > ../youtube.m3u

echo m3u grabbed

