import requests
from bs4 import BeautifulSoup

url= "https://www.billboard.com/charts/hot-100"
day = input("what year you would like to travel to in YYY-MM-DD format")
respone = requests.get(url=f"{url}/{day}")
soup = BeautifulSoup(respone.text, "html.parser")

all_songs = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")
song_titles = [song.getText().replace("\n", "").replace("\t","") for song in all_songs]

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="acf46ea54bc54b6e988f2b7adfd9f4d0",
        client_secret="e1a7c5f0c3c34586938650ac51b8f8ed",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = day.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{day} Billboard 100", public=False)
# print(playlist)
print(playlist["id"])
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)