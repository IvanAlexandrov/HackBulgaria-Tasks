import json
from song import Song


class Playlist(object):

    LOW_BITRATE = 128

    def __init__(self, name='Untitled'):
        self.name = name
        self.songs = []
        self.file_names = {}

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        new_list = []
        for song in self.songs:
            if song_name != song.title:
                new_list.append(song)
        self.songs = new_list

    def total_length(self):
        lenght = 0
        for song in self.songs:
            lenght += song.lenght
        return lenght

    def remove_disrated(self, rating):
        new_list = []
        for song in self.songs:
            if song.rating < rating:
                continue
            else:
                new_list.append(song)
        self.songs = new_list

    def remove_bad_quality(self):
        new_list = []
        for song in self.songs:
            if song.bitrate < Playlist.LOW_BITRATE:
                continue
            else:
                new_list.append(song)
        self.songs = new_list

    def show_artists(self):
        artists = []
        for song in self.songs:
            if song.artist in artists:
                continue
            else:
                artists.append(song.artist)
        return "\n".join(artists)

    def to_string(self):
        songs = []
        for song in self.songs:
            seconds = song.lenght % 60
            minutes = (song.lenght // 60) % 60
            songs.append(str(song.artist) + "\t"
                         + str(song.title) + "\t-\t"
                         + str(minutes) + ':' + str(seconds))
        return "\n".join(songs)

    def save(self, file_name):
        with open(file_name, 'w') as output_file:
            output_file.write(json.dumps(str(self.__dict__),
                              indent=4, sort_keys=True))
            output_file.close()

    @staticmethod
    def load(file_name):
        with open(file_name, 'r') as input_file:
            contents = input_file.read()
            input_file.close()
        decoded = eval(json.loads(contents))
        playlist = Playlist(decoded['name'])
        for song in decoded['songs']:
            playlist.add_song(Song(**song))
        return playlist


# Manual Tests
"""
playlist1 = Playlist("AC/DC")
song1 = Song('The Jack', 'AC/DC', 'High Voltage', 5, 320, 192)
song2 = Song('T.N.T', 'AC/DC', 'High Voltage', 3, 332, 192)
song3 = Song('High Voltage', 'AC/DC', 'High Voltage', 3, 380, 92)
song4 = Song('Hells Bells', 'AC/DC', 'Back in Black', 4, 340, 192)
song5 = Song('Master Of Pupets', 'Metallica', 'The Black Album', 5, 600, 320)
playlist1.add_song(song1)
playlist1.add_song(song2)
playlist1.add_song(song3)
playlist1.add_song(song4)
playlist1.add_song(song5)
playlist1.save('Great_Collection.json')

playlist2 = Playlist.load('Great_Collection.json')
print(playlist2.name)
print('--------------------------------------------------------------')
print(playlist2.to_string())
"""
