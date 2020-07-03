import requests

CAT_API = 'https://api.thecatapi.com/v1/images/search'
DOGO_API = 'https://dog.ceo/api/breeds/image/random'

def get_random_cat():
    response = requests.get(CAT_API)
    if response.status_code == 200:
        obj= response.json()
        return obj[0]['url']  

def get_random_dog():
    response = requests.get(DOGO_API)
    if response.status_code == 200:
        obj= response.json()
        return obj['message'] 

