import pandas as pd 
import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import time

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

scope =  "playlist-modify-private"

sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
)

sp = spotipy.Spotify(auth_manager=sp_oauth)

user = sp.current_user()

playlist_name = "Apple Music Library"
playlist_description = "All my Apple Music songs migrated to Spotify"



playlist = sp.user_playlist_create(
    user = sp.current_user()['id'],
    name=playlist_name,
    public=False,
    description=playlist_description
)

playlist_id = playlist['id']

df = pd.read_csv(
   "combined_library.csv",
    encoding="utf-8",                     
    usecols=["Track name", "Artist name"], 
)

search_queries = []

for index, row in df.iterrows():
    track_list = f"{row['Track name']} {row['Artist name']}"
    search_queries.append(track_list)


uri_list = []
not_found = []

total_songs = len(search_queries)
for idx, song in enumerate(search_queries, start=1):
    try:
        result = sp.search(q=song, type="track", limit=1)
        tracks = result['tracks']['items']
        if tracks:
            uri_list.append(tracks[0]['uri'])
        else:
            not_found.append(song)
        print(f"Searching song {idx} of {total_songs}...")
        time.sleep(0.2)
    except Exception as e:
        print(f"Error searching for {song}: {e}")


for i in range(0, len(uri_list), 100):
    sp.playlist_add_items(playlist_id, uri_list[i:i+100])
    print(f"Added {i+100 if i+100 < len(uri_list) else len(uri_list)} songs so far...")

print(f"Playlist creation complete: {len(uri_list)} tracks added.")

if not_found:
    print(f"{len(not_found)} songs not found. They’re saved in 'not_found.txt'.")


with open("not_found.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(not_found))