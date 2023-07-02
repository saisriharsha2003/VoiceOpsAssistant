import requests
import pygame
import os
import pytube
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the YouTube Data API client
api_key = 'AIzaSyDXgXZQrdvkh4ToRYO4P6fwGryNKWC5N6k'  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=api_key)


def video_url(music_name):
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
        return f'https://www.youtube.com/watch?v={video_id}'
    except HttpError as e:
        print(f'An error occurred: {e}')


def download_song(song_url, save_directory):
    youtube = pytube.YouTube(song_url)
    video = youtube.streams.get_audio_only()
    file_path = video.download(save_directory)
    return file_path


def convert_to_wav(mp3_file):
    # Generate the output WAV file path
    wav_file = os.path.splitext(mp3_file)[0] + ".wav"

    # Convert MP3 to WAV using ffmpeg
    cmd = f'ffmpeg -i "{mp3_file}" -acodec pcm_s16le -ar 44100 -ac 2 "{wav_file}"'
    os.system(cmd)

    return wav_file


def play_song(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


# Example usage
song_name = input("Enter the song name: ")
save_directory = "C:\\Users\\ranke\\Harsha\Projects\\virtual_assisstant\\songs"
# Download the song
song_file = download_song(song_name, save_directory)

# Check if the song was downloaded successfully
if song_file:
    # Play the downloaded song
    wav_file = convert_to_wav(song_file)

    # Play the converted song
    play_song(wav_file)
