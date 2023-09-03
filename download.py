from pytube import YouTube

# path to save in
SAVE_PATH = "E:/"

# link of youtube video
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

try:
    yt = YouTube(link)

    #configuring file type and resolution
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='720p').first()

    if video_stream:
        # downloading the video
        video_stream.download(SAVE_PATH)
        print("Downloaded:", yt.title)
    else:
        print("No suitable stream found for video and audio.")
except Exception as e:
    print("Error:", str(e))

print('Task Completed!')
