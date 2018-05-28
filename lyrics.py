from tkinter import *
import win32gui
import PIL.ImageGrab
from win32api import GetKeyState, GetAsyncKeyState
import time

from musixmatch import Musixmatch
musixmatch = Musixmatch('ba0fb43d46a01bba9cb74907c46620f6')

class MyGUI:
    def __init__(self, root):
        self.root = root
        root.title("Lyrics")
        root.resizable(False,False)
        root.geometry('+%d+%d' % (root.winfo_screenwidth()-300, 30))
        root.attributes("-topmost", True)
        root.attributes("-alpha", 0.5)
		
        self.label = Label(root, text="Artics: ", width=15).grid(row=0, column=0)
        self.label = Label(root, text="Song :", width=15).grid(row=1, column=0)
        
        self.artist = StringVar(root, value='RHCP')
        self.artistBox = Entry(root, textvariable=self.artist)
        self.artistBox.focus()
        self.artistBox.grid(row=0, column=1)
        self.artistBox.bind('<Return>', self.getLyrics)

        self.song = StringVar(root, value='Californication')
        self.songBox = Entry(root, textvariable = self.song)
        self.songBox.grid(row=1, column=1)
        self.songBox.bind('<Return>', self.getLyrics)
		
        self.lyrics = Label(root, text="")
        self.lyrics.grid(row=3, columnspan=2)
		
        self.downloadButton = Button(root, text="Donwload", command=self.getLyrics)
        self.downloadButton.grid(row=2, columnspan=2)
		
    def getLyrics(self, key=''):
        self.lyrics['text'] = downloadLyrics(self.artist.get(), self.song.get())

def downloadLyrics(artist, song):
    print('Artist: ' + artist + "; Song: " + song)
    try:
        track_response = musixmatch.matcher_track_get(song, artist)
        track_id = track_response['message']['body']['track']['track_id']
        
        lyrics_response = musixmatch.track_lyrics_get(track_id)
        lyrics = lyrics_response['message']['body']['lyrics']['lyrics_body']
        
        subtitles = musixmatch.track_subtitle_get(track_id)
        newLines = [pos for pos, char in enumerate(lyrics) if char == '\n']
        lyrics = lyrics[:newLines[-3]]
        
        return lyrics
        
    except Exception as e:
        print(str(e))
        return 'Sorry. We could not found your song\n'
		
root = Tk()
my_gui = MyGUI(root)
root.mainloop()