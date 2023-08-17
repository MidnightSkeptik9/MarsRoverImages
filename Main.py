import requests
import os

API_KEY = '' # Replace with your API key

def getRoverImages(sol, numImages):
    baseUrl = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        'sol': sol, # Martian sol (day)
        'api_key': API_KEY,
        'page': 1 # images from the first page of results
    }

    response = requests.get(baseUrl, params=params)

    if not response.status_code == 200:
        print(f'Failed to fetch data. Status code : {response.status_code}')
    else:
        images = response.json()['photos']

        for i, image in enumerate(images[:numImages]):
            imageUrl = image['img_src']
            imageName = os.path.basename(imageUrl)
            response = requests.get(imageUrl)

            if response.status_code == 200:
                with open(imageName, 'wb') as file:
                    file.write(response.content)
                print(f'Downloaded image {i+1}: {imageName}')
            else:
                print(f'Failed to download image {i+1}')

if __name__ == '__main__':
    sol = 1000 # Martian sol (day) for which you want images
    numImages = 5
    getRoverImages(sol, numImages)