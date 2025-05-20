from pytube import YouTube
import time

while True:

    SAVE_PATH = input("Enter the save path: ")
    print(SAVE_PATH)
    print("\n")
    link = str(input("Enter the video link: "))
    print(link)
    print("\n")

    try:
        yt = YouTube(link)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='720p').first()

        if video_stream:
            video_stream.download(SAVE_PATH)
            print("Downloaded:", yt.title)
            print("\n")
            time.sleep(1)
            print("Closing app...")
            break
        else:
            print("No suitable stream found for video and audio.")
            print("\n")
            print("Restarting...")
            time.sleep(1)
    except Exception as e:
        print("Error:", str(e))
        print("\n")
        print("Restarting...")
        time.sleep(1)
