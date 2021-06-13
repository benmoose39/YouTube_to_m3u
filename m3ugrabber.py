#! /usr/bin/python3

import requests

url = 'https://www.youtube.com/watch?v=zcrUCvBD16k'
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
