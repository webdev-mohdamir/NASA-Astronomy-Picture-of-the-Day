import requests  # import requests for calling api
from PIL import Image  # using PIl to make

# Create  NASA API Key
apiKey = "DEMO_KEY"

# Geting info of the image from NASA API


def genPicOfTheDay():

    try:
        # Making Request
        req = requests.get(
            url=f"https://api.nasa.gov/planetary/apod?api_key={apiKey}",
            stream=True
        )

        # Storing data form the website and returing it
        data = req.json()
        return data

    except Exception as e:
        print(f"There is an error: {e}")
        return None

# Saving Images from the web url


def generateImage(url):
    if url:
        img = Image.open(requests.get(url, stream=True).raw)

        img.save("Picture_Of_The_Day.png")
        print("The Picture is saved succesfully.")


if __name__ == "__main__":

    print("""
<===================>
Programme is Running
<===================>"""
          )

    picData = genPicOfTheDay()
    picUrl = picData['url']

    # Calling the generateImage to generate image
    generateImage(picUrl)
