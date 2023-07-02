import subprocess


def download_audio(url):
    # Command to download audio using ffmpeg
    command = ['ffmpeg', '-i', url, '-vn', '-acodec', 'copy', 'audio.mp3']

    try:
        # Execute the command
        subprocess.check_output(command)
        print("Audio downloaded successfully!")
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)


download_audio("https://www.youtube.com/watch?v=t_aO4EMP-i0")
