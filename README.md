## 📡 From Global Playlist to Personalized Streaming — Introducing [M3USe](https://m3use.projectmoose.xyz)

Hey folks — if you've used or followed this repo in the past, you might remember it started as an automated GitHub Actions workflow that created a public M3U playlist of livestreams (mostly YouTube). You could request channels, and I'd manually add them to the playlist for everyone.

But things have evolved.

### 🎉 Meet [M3USe](https://m3use.projectmoose.xyz) — A Web App for Custom Livestream Playlists

✅ Add livestreams from **YouTube**, **Twitch**, and **Dailymotion**  
✅ Build your **own playlist** — no more global list  
✅ Use with **any IPTV player** (VLC, Kodi, TiviMate, etc.)  
✅ Your playlist, your links, your rules

💡 No more waiting for manual updates or one-size-fits-all playlists. You just paste the channel URL, and the backend takes care of the rest.

---

> This is an indie passion project powered by the [Project Moose Discord](https://discord.gg/dmgYmAEdee) — and it’s live now.  
> 🚀 Try it out: [https://m3use.projectmoose.xyz](https://m3use.projectmoose.xyz)

Got ideas, feedback, or requests? Drop by the Discord or open a discussion here!

---

[![Live App](https://img.shields.io/badge/Live%20App-M3USe-green?style=flat-square)](https://m3use.projectmoose.xyz)


--------------------------- END (old content below) ---------------------------

<h1 align="center"> YouTube_to_m3u </h1>

[![M3U generator for YouTube](https://github.com/benmoose39/YouTube_to_m3u/actions/workflows/m3u_Generator.yml/badge.svg)](https://github.com/benmoose39/YouTube_to_m3u/actions/workflows/m3u_Generator.yml)

`https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/youtube.m3u`

Updated m3u links of YouTube live channels, **auto-updated every 3 hours**.


### Add more channels
Edit `youtube_channel_info.txt` to add your favourite YouTube livestreams

Create a pull request or connect: https://discord.gg/dmgYmAEdee

### Usage
Paste this URL: `https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/youtube.m3u` to any player which supports M3U playlists

### Run the tool on your local machine
``` bash
git clone https://github.com/benmoose39/YouTube_to_m3u.git
cd YouTube_to_m3u
chmod +x autorun.sh
./autorun.sh
```

Do not forget to add a cron job set for every 4 hours(or 5) if you plan to run the script locally.

### Support

🙂 https://www.buymeacoffee.com/benmoose39
