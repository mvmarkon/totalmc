import json

from flask import Flask, request, url_for
from flask_restful import Api
from core import search, search2, localstorage
from flask_cors import CORS
import storage
from config import Config as cfg

from services.ytdl import videodata, downloadVIDEO, downloadMP3, downloadMP3list, downloadVIDEOlist

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.debug=True
app.config.from_object('config')

@app.route('/')
def api_root():
    return 'Welcome'

#@app.route('/localvideos')
#def api_local_videos():
#    return local_videos()
#
#@app.route('/localaudios')
#def api_local_audios():
#    return local_audios()

@app.route('/getvideodata/')
def api_getvideodata():
    videourl = request.args.get('videourl', '')
    return videodata(videourl)

@app.route('/search/<query>')
def api_search(query):
    print('Buscando')
    return search2(query)

@app.route('/downloadmp3/')
def api_dl_mp3():
    print(cfg.basedir)
    print('Descargando MP3')
    videourl = request.args.get('videourl', '')
    return downloadMP3(videourl)

@app.route('/downloadvideo/')
def api_dl_video():
    print('Descargando VIDEO')
    videourl = request.args.get('videourl', '')
    return downloadVIDEO(videourl)

@app.route('/downloadvideolist/')
def api_dl_videolist():
    urlarray = request.args.get('urlarray', '')
    urls = urlarray.split(',')
   
    return downloadVIDEOlist(urls)

@app.route('/downloadmp3list/')
def api_dl_mp3list():
    urlarray = request.args.get('urlarray', '')
    urls = urlarray.split(',')
#    arr = [str(r) for r in urls]

    return downloadMP3list(urls)

@app.route('/connect/')
def connect():
    return localstorage()

#with app.test_request_context():
#    print url_for('/')
#    print url_for('/getvideodata/')
#    print url_for('login', next='/')
#    print url_for('profile', username='John Doe')


if __name__ == '__main__':
     app.run(port='5002')