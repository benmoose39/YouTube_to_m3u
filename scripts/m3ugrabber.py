#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __				#
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___	#
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \	#
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/	#
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|	#
#                   |__/						#
#	      								#
#########################################################################
'''

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
print(banner)
with open('channel_info.txt') as f:
	for line in f:
		line = line.strip()
		if not line:
			continue
		if 'https:' not in line:
			line = line.split('|')
			print(f'\n#EXTINF:-1 group-title="{line[1].strip().title()}", {line[0].strip()}')
		else:
			grab(line)

