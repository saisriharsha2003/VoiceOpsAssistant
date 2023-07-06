import requests


def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return access_token
    else:
        return None


def play_song(access_token, song_id):
    url = "https://api.spotify.com/v1/me/player/play"
    headers = {
        "Authorization": "Bearer {}".format(access_token),
    }
    data = {
        "uris": [song_id],
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code


def get_song_id(song_name):
    url = "https://api.spotify.com/v1/search"
    params = {
        "q": song_name,
        "type": "track",
    }
    response = requests.get(url, params=params)
    print(response)
    if response.status_code == 200:
        results = response.json()["tracks"]["items"]
        if len(results) > 0:
            song_id = results[0]["id"]
            return song_id
        else:
            return None
    else:
        return None


def play_song_auto(song_name):
    client_id = "94f7557244984fa5bfc55d09cbbde52d"
    client_secret = "6ac60ca65d9f48df9f259b1cb6004838"
    access_token = get_access_token(client_id, client_secret)
    print(access_token)
    song_id = get_song_id(song_name)
    print(song_id)
    status_code = play_song(access_token, song_id)
    return status_code


song_name = "Sehari Sehari"
play_song_auto(song_name)
