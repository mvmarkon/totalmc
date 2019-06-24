from storage import connect, get_content
from flask_restful import Resource
from scraper import scrapsearch, videoId, searchWithYoutube
import json


#def local_audios():
#	return json.dumps(l_audio)
#
#def local_videos():
#	return json.dumps(l_video)

def search(query):
	return json.dumps(scrapsearch(query))

def search2(query):
	return json.dumps(searchWithYoutube(query))

def video_data(artistplustrack):
	return json.dumps(videoId(artistplustrack))

def localstorage():
	return json.dumps(connect())
