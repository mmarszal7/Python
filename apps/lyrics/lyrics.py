from tkinter import *
import win32gui
import PIL.ImageGrab
import time
import geniusAPI

from musixmatch import Musixmatch
musixmatch = Musixmatch('ba0fb43d46a01bba9cb74907c46620f6')

class MyGUI:
    def __init__(self, root):
        self.root = root
        root.title("Lyrics")
        root.resizable(False,False)
        root.geometry('+%d+%d' % (root.winfo_screenwidth()-300, 30))
        root.attributes("-topmost", True)
        root.attributes("-alpha", 0.8)

        self.label = Label(root, text="Artist: ", width=10).grid(row=0, column=0, sticky='w', pady=5)
        self.label = Label(root, text="Song :", width=10).grid(row=1, column=0, sticky='w')
        
        self.artist = StringVar(root, value='red hot')
        self.artistBox = Entry(root, textvariable=self.artist)
        self.artistBox.focus()
        self.artistBox.grid(row=0, column=1, columnspan=2, sticky='ew', pady=5)
        self.artistBox.bind('<Return>', self.getLyrics)

        self.song = StringVar(root, value='Californication')
        self.songBox = Entry(root, textvariable = self.song)
        self.songBox.grid(row=1, column=1, columnspan=2, sticky='ew')
        self.songBox.bind('<Return>', self.getLyrics)
		
        self.lyrics = Listbox(root)
        self.lyrics.config(height = 20, width=0)
        self.lyrics.grid(row=3, columnspan=3, sticky='ew', padx = 10, pady = 10)

        self.scroll = Scrollbar(root, orient='vertical', command=self.lyrics.yview)
        self.scroll.grid(row = 3, column=3, sticky='ns')
        self.lyrics.config(yscrollcommand=self.scroll.set)
		
        self.downloadButton = Button(root, text="Donwload", command=self.getLyrics)
        self.downloadButton.grid(row=2, column=1, columnspan=2, sticky='e', pady=5)
		
    def getLyrics(self, key=''):
        #self.lyrics['text'] = downloadLyrics(self.artist.get(), self.song.get())
        lyrics = geniusAPI.downloadLyrics(self.artist.get(), self.song.get()).split("\n")
        self.lyrics.insert(END, *lyrics)

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