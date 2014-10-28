import os.path

from mutagen.mp3 import MP3
from playlist import Playlist
from song import Song


class MusicCrawler(object):

    def __init__(self, path):
        self.path = path
        self.playlist = Playlist("Crawled")
        self.file_names = {}

    def generate_playlist(self):
        list_of_files = os.listdir(self.path)
        for fname in list_of_files:
            if fname.endswith(('mp3', 'ogg')):
                audio = MP3(self.path + '/' + fname)
                song = Song(audio['TIT2'],
                            audio['TPE1'],
                            audio['TALB'],
                            4,
                            int(audio.info.length),
                            audio.info.bitrate // 1000)
                self.playlist.add_song(song)
                if fname not in self.file_names:
                    self.file_names[str(audio['TIT2'])] = self.path + "/" +fname

# a = MusicCrawler('/home/vankel/Music')
# a.generate_playlist()
# print(a.file_names)
