import requests
from bs4 import BeautifulSoup as bs
import urllib2
import json


def scrapsearch(query):
	url = 'https://bemusic.vebto.com/secure/search/'+query+'?limit=30'
	res = requests.get(url)
	return res.content

def videoId(query):
	url = 'https://bemusic.vebto.com/secure/search/audio/'+query
	res = requests.get(url)
	return res.content

def hrefdec(href):

	res = href.replace('/watch?', '')
	params = res.split('&')
	obj = {}
	for p in params:
		t=p.split('=')
		obj[t[0]] = t[1]
	return '/watch?v='+obj['v'],obj 

def searchWithYoutube(query):
	videolinks = []
	scrape_url = "https://www.youtube.com"
	r = requests.get(scrape_url+"/results?search_query="+ query)
	soupeddata = bs(r.content, "html.parser")
	yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
	for x in yt_links:
		if "watch" in x.get("href"):
			yt_title = x.get("title")
			yt_href, yt_others = hrefdec(x.get("href"))
			yt_final = scrape_url + yt_href
			thumb = "http://img.youtube.com/vi/"+ yt_others['v'] + "/mqdefault.jpg"
			videolinks.append({"title":yt_title, "link":yt_final, "id":yt_href, "thumbnail":thumb, 'others':yt_others})
	return videolinks

#	https://teklern.blogspot.com/2017/10/web-scrape-youtube-channel-for-video.html

#	https://www.desinerd.co.in/video-scraping-with-beautiful-soup-python/

#	https://www.youtube.com/watch?v=UgiymkXulPY



# url = 'https://bemusic.vebto.com/'

# 'https://bemusic.vebto.com/secure/search/audio/Los%20Alegres%20MX/La%20Cobra%20Gay'


# /**
# * Search for artists, albums, tracks, playlists and users.
# */
# public everything(query: string, params?: {limit: number}): Observable<SearchResponse> {
# return this.http.get('search/'+encodeURIComponent(query), params);
# }

# /**
# * Search for video ID for specified artist and track.
# */
# public videoId(artists: string, track: string): Observable<{title: string, id: string}[]> {
# const artistName = this.encode(artists),
# trackName  = this.encode(track);

# return this.http.get('search/audio/'+artistName+'/'+trackName);
# }

# /**
# * Search local database for matching artists.
# */
# public localArtists(query: string, params?: {limit: number}) {
# return this.http.get('search/local/artists/'+query, params);
# }

# private encode(string: string): string {
# return encodeURIComponent(string.replace('/', '+'));
# }
# }

# content = urllib2.urlopen(url).read()
# html = content

# soup = BeautifulSoup(html)
# searchInput = soup.find_all(id="search")
# print searchInput
def test(query):
	videolinks = []
	scrape_url = "https://www.youtube.com"
	r = requests.get(scrape_url+"/results?search_query="+ query)
	soupeddata = bs(r.content, "html.parser")
	#yt_lis = soupeddata.find_all("yt-img-shadow", class_ = "style-scope")
	#yt = sd.select('a.yt-uix-tile-link' 'img')
	#sd.select("a#thumbnail" "img")
	yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
	for x in yt_links:
		print x.get("href")
		if "watch" in x.get("href"):
			yt_href = x.get("href")
			yt_title = x.get("title")
			yt_final = scrape_url + yt_href
			yt_thmb = yt_href.replace("/watch?v=","")
			thumb = "http://img.youtube.com/vi/"+ yt_thmb + "/mqdefault.jpg"
			trk = {"title":yt_title, "link":yt_final, "id":yt_href, "thumbnail": thumb}
			trk2 = yt_href
			videolinks.append(trk2)

	#return videolinks