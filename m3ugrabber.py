#! /usr/bin/python3

import requests

def grab(url):
	response = requests.get(url).text
	end = response.find('.m3u8') + 5
	tuner = 100
	while True:
		if 'https://' in response[end-tuner : end]:
			link = response[end-tuner : end]
			start = link.find('https://')
			end = link.find('.m3u8') + 5
			break
		else:
			tuner += 5
	print(f"{link[start : end]}")

print("#EXTM3U")
with open('channel_info.txt') as f:
	for line in f:
		line = line.strip()
		if not line:
			continue
		if 'https:' not in line:
			print(f"\n#EXTINF:-1, {line}")
		else:
			grab(line)

