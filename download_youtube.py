import pafy

# specify the YouTube video URL
url = "https://www.youtube.com/watch?v=0n7AWxYCj9I"

# create a pafy object
video = pafy.new(url)

# get the audio stream
audio = video.getbestaudio()

# download the audio stream
audio.download(filepath="path/to/output/directory/audio_file_name.mp3")