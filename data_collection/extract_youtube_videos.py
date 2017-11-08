from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

# import subprocess
# subprocess.call(['youtube-dl','-o',output_path+'/%(title)s.(ext)s',"--extract-audio","--audio-format","mp3",decoded_url])
