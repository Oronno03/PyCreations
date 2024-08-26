from pytubefix import YouTube


def download(link):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    input(f"Downloading {ys.title}...")
    ys.download()


url = input("Enter the video link: ")
try:
    download(url)

except:
    print(
        "An error occurred. Please check the link and make sure you have an active internet connection and try again."
    )
    quit()
print("The video has been downloaded successfully!")
input("Press Enter to exit")
