from music_crawler import MusicCrawler
from playlist import Playlist
from subprocess import call


def main():
    file_names = {}
    print("Welcome to buggy console Audio Player!")
    print("You can use the following commands:")
    print('-------------------------------------------')
    print("load <directory> - makes new playslist\n"
          "load <playlist> - load existing playlist"
          " /*json extensions only*/\n"
          "save <file name> - saves loaded playlist\n"
          "show - shows the current playlist\n"
          "play --<song> - plays the given song\n"
          "qiut or exit - closes the player\n")

    while True:
        selection = input('Enter a command > ')

        if selection == 'exit' or selection == 'quit':
            exit()
        elif selection.startswith('load'):
            params = selection.split(' ')
            if params[1].endswith('.json'):
                my_playlist = Playlist.load(params[1])
            else:
                my_playlist = MusicCrawler(params[1])
                my_playlist.generate_playlist()
                file_names = my_playlist.file_names
                my_playlist = my_playlist.playlist
            print(my_playlist.to_string())
        elif selection.startswith('play'):
            params = selection.split('--')
            print('Now playng ' + params[1])
            print('Press "n" to stop song\n'
                  '"m" to Mute or Unmute song\n'
                  '"*"" or "/" to Increase/Decrease Volume')
            # The player in quiet mode with Keys control
            call(['mpg123', file_names[params[1]], '-qK'])
            print(my_playlist.to_string())

if __name__ == '__main__':
    main()
