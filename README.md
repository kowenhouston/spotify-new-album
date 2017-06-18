# spotify-new-album
Do something when your favourite artist releases a new album

# Details
50 min code challenge: Create a program that alerts when your favourite artist adds a new album.
<br>
Code is dodgy but it works.

# Install / Run
1. Install prerequisites by running ```pip install python-dateutil spotipy```
1. Go to https://developer.spotify.com/my-applications/ and create an application
1. Set the Redirect URI to http://localhost
1. Export your settings from the my-application page on spotify in your linux terminal:
```
export SPOTIPY_CLIENT_ID='<YOUR_SPOTIFY_CLIENT_ID>'
export SPOTIPY_CLIENT_SECRET='<YOUR_SPOTIFY_CLIENT_SECRET>'
export SPOTIPY_REDIRECT_URI='http://localhost/'
```
5. Edit spotify-new-album.py to enter your username
6. Run python spotify-new-album.py

# Notes
Only tested on Python 3.4
<br>
If you import this into another python app you could probably do something cool like text you or whatever. But I had 50 minutes.

# Sample output
```
(v_spotify) root@not-windows:~/spotify-new-album# python spotify-new-album.py


            User authentication requires interaction with your
            web browser. Once you enter your credentials and
            give authorization, you will be redirected to
            a url.  Paste that url you were directed to to
            complete the authorization.


Opened https://accounts.spotify.com/authorize?client_id=<trash>&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%2F&scope=user-library-read in your browser


Enter the URL you were redirected to: http://localhost/?code=<trash>


Type: Single
Name: For Miles & Miles
Release Date: 2017-04-15
Type: Single
Name: Frameworks
Release Date: 2016-12-19
Type: Single
Name: Beautiful Life
Release Date: 2016-09-05
...
```
