import subprocess

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pytube
import moviepy.editor as mp
import pygame
from pydub import AudioSegment

# Set up the YouTube Data API client
api_key = 'AIzaSyDXgXZQrdvkh4ToRYO4P6fwGryNKWC5N6k'  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=api_key)


def search_youtube_videos(query):
    search_response = youtube.search().list(
        q=music_name,
        part='snippet',
        maxResults=1,
        type='video'
    ).execute()

    # Extract the video ID from the search results
    video_id = search_response['items'][0]['id']['videoId']
    return f'https://www.youtube.com/watch?v={video_id}'


def download_audio(video_url):
    try:
        command = f'youtube-dl -x --audio-format mp3 --output "audio.%(ext)s" {video_url}'
        subprocess.call(command, shell=True)

        return 'audio.mp3'

    except Exception as e:
        print(f'An error occurred: {e}')

#
#
# def play_music(file_path):
#     pygame.mixer.init()
#     pygame.mixer.music.load(file_path)
#     pygame.mixer.music.play()
#     # Wait until the music finishes playing
#     while pygame.mixer.music.get_busy():
#         continue

music_name="na roja nuvve"
video_url=search_youtube_videos(music_name)
video_file=download_audio(video_url)
print(video_file)
