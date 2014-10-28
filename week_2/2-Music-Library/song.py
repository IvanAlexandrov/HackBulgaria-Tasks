class Song(object):
    MIN_RATING = 1
    MAX_RATING = 5

    def __init__(self, title, artist, album, rating, lenght, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.lenght = lenght
        self.bitrate = bitrate
        self.set_rating(rating)

    def set_rating(self, rating):
        if rating < Song.MIN_RATING or rating > Song.MAX_RATING:
            raise ValueError("Your rating must be between {} and {}"
                             .format(Song.MIN_RATING, Song.MAX_RATING))
        else:
            self.rating = rating

    def __repr__(self):
        return str(self.__dict__)
