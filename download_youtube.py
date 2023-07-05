import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication
scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Search for a song
song_name = "Enter Sandman"  # Replace with the name of the song you want to play
results = sp.search(q=song_name, type="track", limit=1)
if len(results["tracks"]["items"]) > 0:
    song_uri = results["tracks"]["items"][0]["uri"]
    # Play the song
    sp.start_playback(uris=[song_uri])
    print("Playing:", song_name)
else:
    print("Song not found.")
