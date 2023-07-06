import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication with client ID, client secret, redirect URI, and scope
scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', redirect_uri='YOUR_REDIRECT_URI'))

# Get the authorization URL
auth_url = sp.auth_manager.get_authorize_url()

# Redirect the user to the authorization URL
print(f"Please visit the following URL to authorize your Spotify account: {auth_url}")

# After authorization, extract the authorization code from the redirect URI and assign it to the 'authorization_code' variable

# Set up authentication with client ID, client secret, redirect URI, and authorization code
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='94f7557244984fa5bfc55d09cbbde52d', client_secret='6ac60ca65d9f48df9f259b1cb6004838', redirect_uri='https"//localhost:3000'))

# Search for a song
track_name = "Enter the name of the song you want to play"
results = sp.search(q=track_name, type="track", limit=1)

# Get the URI of the first result
uri = results["tracks"]["items"][0]["uri"]

# Play the song
sp.start_playback(uris=[uri])
