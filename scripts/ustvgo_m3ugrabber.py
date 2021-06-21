banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                                                       #
#########################################################################
'''

import requests

def grab(url):
    url = url.split('?')
    data = {}
    data['stream'] = url[1].split('=')[1]
    m3u = requests.post(url[0], data=data).text
    print(m3u)


print('#EXTM3U')
print(banner)
with open('../ustvgo_channel_info.txt') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        line = line.split('|')
        name = line[0]
        link = line[1]
        print(f'\n#EXTINF:-1, {name}')
        grab(link)
