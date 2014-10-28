import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.test_song = Song(
            'Hells Bells',
            'AC/DC',
            'rough and though',
            5,
            520,
            256)

    def test_song_init(self):
        self.assertEqual(self.test_song.title, 'Hells Bells')
        self.assertEqual(self.test_song.artist, 'AC/DC')
        self.assertEqual(self.test_song.album, 'rough and though')
        self.assertEqual(self.test_song.rating, 5)
        self.assertEqual(self.test_song.lenght, 520)
        self.assertEqual(self.test_song.bitrate, 256)

    def test_rating(self):
        self.test_song.set_rating(4)
        self.assertEqual(self.test_song.rating, 4)

    def test_rating_out_of_range(self):
        with self.assertRaises(ValueError):
            self.test_song.set_rating(8)


if __name__ == '__main__':
    unittest.main()
