import requests

CAT_API = 'https://api.thecatapi.com/v1/images/search'
DOGO_API = 'https://dog.ceo/api/breeds/image/random'

def get_ramdon_cat():
    response = requests.get(CAT_API)
    if response.status_code == 200:
        obj= response.json()
        return obj[0]['url']  

def get_ramdon_dog():
    response = requests.get(DOGO_API)
    if response.status_code == 200:
        obj= response.json()
        return obj['message'] 

"""
for i in range(10):
    if i%2 == 0:
        print(get_ramdon_cat())
    else:
        print(get_ramdon_dog())
"""