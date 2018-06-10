from urllib.request import Request, urlopen, quote
import requests, socket, json
from bs4 import BeautifulSoup

def _make_api_request(request_term_and_type, page=1):
	api_request = _format_api_request(request_term_and_type, page=page)        
	request = Request(api_request)        
	request.add_header("Authorization", 'Bearer ZobAWw7oAUD3OD_OT2qlOmJX0VFhhiED8E0nmA6_MXvTAnWmtWEHxww_gb0XRTNe')
	request.add_header("User-Agent","LyricsGenius")
	
	try:
		response = urlopen(request, timeout=4) #timeout set to 4 seconds; automatically retries if times out
		raw = response.read().decode('utf-8')
	except socket.timeout:
		print("Timeout raised and caught")
							
	return json.loads(raw)['response']

def _format_api_request(term_and_type, page=1):
	_API_URL = "https://api.genius.com/"  
	_API_REQUEST_TYPES = {'song': 'songs/', 'artist': 'artists/', 'artist-songs': 'artists/songs/','search': 'search?q='}
	
	request_term, request_type = str(term_and_type[0]), term_and_type[1]                
	assert request_type in _API_REQUEST_TYPES, "Unknown API request type"
	
	if request_type=='artist-songs':
		return _API_URL + 'artists/' + quote(request_term) + '/songs?per_page=50&page=' + str(page)
	else:        
		return _API_URL + _API_REQUEST_TYPES[request_type] + quote(request_term)
		
def _scrape_song_lyrics_from_url(URL, remove_section_headers=False):
	page = requests.get(URL)    
	html = BeautifulSoup(page.text, "html.parser")
	
	# Scrape the song lyrics from the HTML
	lyrics = html.find("div", class_="lyrics").get_text()
	if remove_section_headers:
		lyrics = re.sub('(\[.*?\])*', '', lyrics) # Remove [Verse] and [Bridge] stuff
		lyrics = re.sub('\n{2}', '\n', lyrics) # Remove gaps between verses
	
	return lyrics.strip('\n')
		
def downloadLyrics(artist, song):
	request = artist + ' ' + song
	result = _make_api_request((request, 'search'))
	songURL = result['hits'][0]['result']['url'];
	lyrics = _scrape_song_lyrics_from_url(songURL)
	return lyrics