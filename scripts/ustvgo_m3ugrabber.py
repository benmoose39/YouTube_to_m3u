import requests

def grab(url):
    url = url.split('?')
    data = {}
    data['stream'] = url[1].split('=')[1]
    m3u = requests.post(url[0], data=data).text
    print(m3u)


print('#EXTM3U')
with open('ustvgo_channel_info.txt') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        line = line.split('|')
        name = line[0]
        link = line[1]
        print(f'\n#EXTINF:-1, {name}')
        grab(link)
