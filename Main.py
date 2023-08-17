import requests

API_KEY = '' # Replace this with your api key

url = "https://api.nasa.gov/mars-photos"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)