from __future__ import unicode_literals
import youtube_dl
import json
from config import Config as cfg

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


mp3_opts = {
	'outtmpl': cfg.basedir+'/audio/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger()
}
    #'progress_hooks': [my_hook],
video_opts = {
	'videoformat' : "mp4",
	'outtmpl': cfg.basedir+'/video/%(title)s.%(ext)s'
}

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s'})
ytdlMP3 = youtube_dl.YoutubeDL(mp3_opts)
ytdlVIDEO = youtube_dl.YoutubeDL(video_opts)

def videodata(videourl):
	with ydl:
			result = ydl.extract_info(videourl,download=False)
			# We just want to extract the info
	if 'entries' in result:
			# Can be a playlist or a list of videos
			video = result['entries'][0]
	else:
			# Just a video
			video = result
	return json.dumps(video)

def downloadMP3(videourl):
	with ytdlMP3:
		result = ytdlMP3.download([videourl]) # We just want to extract the info

	return json.dumps(result)

def downloadMP3list(videourl):
	ytdlMP3 = youtube_dl.YoutubeDL(mp3_opts)
	with ytdlMP3:
		result = ytdlMP3.download(videourl) # We just want to extract the info
	return json.dumps(result)

def downloadVIDEO(videourl):
	with ytdlVIDEO:
			result = ytdlVIDEO.download([videourl]) # We just want to extract the info

	return json.dumps(result)

def downloadVIDEOlist(videourl):
	with ytdlVIDEO:
		result = ytdlVIDEO.download(videourl) # We just want to extract the info
	return json.dumps(result)
