import spotipy
import sys
import spotipy
import spotipy.util as util
import datetime
from dateutil import parser


today = datetime.date.today()
last_month = today - datetime.timedelta(days=30)

# Mitis
urn = 'spotify:artist:16yUpGkBRgc2eDMd3bB3Uw'
sp = spotipy.Spotify()

sp.trace = True # turn on tracing
sp.trace_out = True # turn on trace out


scope = 'user-library-read'
username = '<Your username here>'
token = util.prompt_for_user_token(username, scope)

def check_release():
    new_album = 0
    if token:
        sp = spotipy.Spotify(auth=token)
        artist_albums = sp.artist_albums(urn)
        for album in artist_albums['items']:
            album_info = sp.album(album['uri'])
            if __name__ == "__main__":
                print("Type:", album_info['album_type'].title()), 
                print("Name:", album_info['name'] )
                print("Release Date:", album_info['release_date'] )
            album_time = parser.parse(album_info['release_date'])
            album_time = album_time.date()
            if album_time > last_month:
                if __name__ == "__main__":
                    print("Status: New ALBUM!")
                new_album = 1
        
    else:
        print("Can't get token for", username)

    return 1 if new_album else 2

if __name__ == "__main__":
    check_release()
