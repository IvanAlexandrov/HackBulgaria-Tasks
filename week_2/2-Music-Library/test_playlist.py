import unittest
from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist('my_playlist')
        self.untitled = Playlist()
        self.song_1 = Song(
            'Hells Bells',
            'AC/DC',
            'rough and though',
            4,
            400,
            256)
        self.song_2 = Song(
            'For Whom the Bell Tolls',
            'Metallica',
            'For Whom the Bell Tolls',
            5,
            500,
            320)

    def test_playlist_init(self):
        self.assertEqual(self.playlist.name, 'my_playlist')
        self.assertEqual(self.untitled.name, 'Untitled')

    def test_add_song(self):
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)

    def test_remove_song(self):
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)
        self.playlist.remove_song('Hells Bells')
        self.assertEqual(len(self.playlist.songs), 1)

    def test_total_length(self):
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)
        self.assertEqual(self.playlist.total_length(), 2100)

    def test_remove_disrated(self):
        self.song_1.set_rating(3)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)
        self.playlist.remove_disrated(4)
        self.assertEqual(len(self.playlist.songs), 1)

    def test_remove_bad_quality(self):
        self.song_1.bitrate = 92
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)
        self.playlist.remove_bad_quality()
        self.assertEqual(len(self.playlist.songs), 1)

    def test_show_artists(self):
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)
        # print(self.playlist.show_artists())

    def test_to_string(self):
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)

        print(self.playlist.to_string())

    def test_save(self):
        # pass
        self.playlist.add_song(self.song_2)
        self.playlist.add_song(self.song_1)
        self.playlist.add_song(self.song_2)
        self.playlist.save('playlist.json')

    def test_load(self):
        # pass
        plst = Playlist.load('playlist.json')
        print(plst.to_string)

if __name__ == '__main__':
    unittest.main()
