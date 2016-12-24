from gmusicapi import Mobileclient
from secrets import un
from secrets import pw

PLAYLIST_MAX_SONGS = 1000

api = Mobileclient()
if api.login(un, pw, Mobileclient.FROM_MAC_ADDRESS):
    print 'login success'
    library = api.get_all_songs()
    playlist = 'Download'
    genres = ['Electronic',
              'Post-Rock',
              'Indie Folk',
              'Folk Rock',
              'Folk',
              'World',
              'Jazz',
              'Progressive Rock',
              'Alternative']

    i = 0
    while len(library) > 0:
        sample = library[:1000]
        sweet_track_ids = [track['id'] for track in sample 
                               if track['genre'] in genres]
        playlist_id = api.create_playlist(playlist+str(i))
        api.add_songs_to_playlist(playlist_id, sweet_track_ids)
        print 'uploaded ' + len(sample) + ' songs to ' + playlist + str(i);
        del library[:1000]
        i = i + 1


    print 'added genres to ' + playlist + ": " + genres
else:
    print 'login fail'
