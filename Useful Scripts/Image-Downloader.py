import os, requests


def get_extension(image_url):
    extensions = [".png", ".jpeg", ".jpg", ".gif", ".svg"]
    for extension in extensions:
        if extension in image_url:
            return extension


def download_image(url, name, folder=None):
    if extension := get_extension(url):
        if folder:
            image_name = f"{folder}/{name}{extension}"
        else:
            image_name = f"{name}{extension}"
    else:
        raise Exception("Could not locate the extension of the image")

    if os.path.isfile(image_name):
        raise Exception("File already exists")

    try:
        content = requests.get(url).content
        with open(image_name, "wb") as f:
            f.write(content)
            print(f"Downloaded {image_name} successfully")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = input("Enter the url: ")
    name = input("What do you want the image to be named? ")

    print("Downloading the image.....")
    download_image(url, name)
    input("Press Enter to exit")
