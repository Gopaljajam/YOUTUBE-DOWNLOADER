from pytube import YouTube
import os
from tkinter import Tk, filedialog

# Prompt user to input video URL
video_url = input("Enter the YouTube video URL: ")

# Prompt user to choose whether to download video or audio
while True:
    choice = input("Do you want to download the video (v) or audio (a)? ")
    if choice.lower() == "v":
        download_video = True
        break
    elif choice.lower() == "a":
        download_video = False
        break
    else:
        print("Invalid choice. Please enter 'v' or 'a'.")

# Create a YouTube object from the URL
yt = YouTube(video_url)

# Prompt user to choose a directory to save the file to
root = Tk()
root.withdraw()
save_dir = filedialog.askdirectory()

if download_video:
    # Get the highest resolution video stream
    stream = yt.streams.get_highest_resolution()
    # Download the video to the specified directory
    print(f"Downloading video '{yt.title}'...")
    stream.download(output_path=save_dir)
    print("Download complete!")
else:
    # Get the highest quality audio stream
    stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4").first()
    # Download the audio to the specified directory as an mp4 file
    print(f"Downloading audio from '{yt.title}'...")
    audio_file = stream.download(output_path=save_dir)
    # Rename the audio file to have an mp3 extension
    base, ext = os.path.splitext(audio_file)
    new_file = f"{base}.mp3"
    os.rename(audio_file, new_file)
    print("Download complete!")
