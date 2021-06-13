"""
 This file will download the audio files from youtube which is necessary for data collection.
 Need to install youtube_dl using pip.
 we can specify the format of the audio along with samplerate . ffmpeg tool is mandatory for resampling
"""

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '8000'
    ],
    'prefer_ffmpeg': True,
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    path=['path1','path2''.......]
    for i in path:
      ydl.download([i])
