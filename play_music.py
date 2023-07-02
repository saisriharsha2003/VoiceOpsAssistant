import webbrowser
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the YouTube Data API client
api_key = 'AIzaSyDXgXZQrdvkh4ToRYO4P6fwGryNKWC5N6k'  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=api_key)


def play_music_online(music_name):
    try:
        # Search for videos based on the music name
        search_response = youtube.search().list(
            q=music_name,
            part='snippet',
            maxResults=1,
            type='video'
        ).execute()

        # Extract the video ID from the search results
        video_id = search_response['items'][0]['id']['videoId']

        # Open the video in the default web browser
        print(f'https://www.youtube.com/watch?v={video_id}')
        webbrowser.open(f'https://www.youtube.com/watch?v={video_id}')
    except HttpError as e:
        print(f'An error occurred: {e}')


# Example usage
music_name = input('Enter the name of the music: ')
play_music_online(music_name)
