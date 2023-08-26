import os
import random
import time
import uuid


import pytest
import requests

def test_populate_db():
        REST_API_ID = os.environ.get("REST_API_ID")
        STAGE_NAME = os.environ.get("STAGE_NAME")
        REGION = os.environ.get("REGION")
        api_gateway_base_url = f"https://{REST_API_ID}.execute-api.{REGION}.amazonaws.com/{STAGE_NAME}"

        pop_size = 10
        colors = ['red', 'blue', 'green', 'orange', 'rainbow', 'holographic']
        classes = ['Ethereal', 'Fire', 'Water', 'Angelic', 'Grass', 'Psychic', 'Magic']
        temperaments = ['friendly','not friendly','very not friendly']
        names = [
            'Rosalie',
            'Meghan',
            'Sheri',
            'Fernando',
            'Lowell',
            'Albert',
            'Floyd',
            'Annette',
            'Jackie',
            'Mona'
        ]
        for entry in range(pop_size):
            unicorn = {
                'unicornId': str(10 + entry),
                'unicornName': names[entry],
                'unicornClass': random.choice(classes),
                'hornCount': 1,
                'color': random.choice(colors),
                'temperament': random.choice(temperaments),
                'mass': 50 + random.random()*50
            }
            print(unicorn)
            response = requests.post(f"{api_gateway_base_url}/unicorns", json = unicorn)
            time.sleep(2)
            print(response.json)

# def test_api_gateway():
#         REST_API_ID = os.environ.get("REST_API_ID")
#         STAGE_NAME = os.environ.get("STAGE_NAME")
#         REGION = os.environ.get("REGION")
        
#         api_gateway_base_url = f"https://{REST_API_ID}.execute-api.{REGION}.amazonaws.com/{STAGE_NAME}"

#         response = requests.get(f"{api_gateway_base_url}/unicorns/1")
#         assert response.json() == {'unicornId': '1', 'unicornName': 'Amalthea', 'unicornClass': 'Ethereal'}

#         myobj = {'unicornId': '3', 'unicornName': 'MewTwo', 'unicornClass': 'Psychic'}
#         response = requests.post(f"{api_gateway_base_url}/unicorns", json = myobj)
#         print("put Unicorn response")
#         print(response.json())
#         response = requests.get(f"{api_gateway_base_url}/unicorns/3")
#         print(response.json())
#         assert response.json() == myobj
        
