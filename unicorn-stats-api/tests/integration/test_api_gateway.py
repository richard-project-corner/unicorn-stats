import os

import pytest
import requests

def test_api_gateway():
        REST_API_ID = os.environ.get("REST_API_ID")
        STAGE_NAME = os.environ.get("STAGE_NAME")
        REGION = os.environ.get("REGION")
        
        api_gateway_base_url = f"https://{REST_API_ID}.execute-api.{REGION}.amazonaws.com/{STAGE_NAME}"

        response = requests.get(f"{api_gateway_base_url}/unicorns/1")
        assert response.json() == {'unicornId': '1', 'unicornName': 'Amalthea', 'unicornClass': 'Ethereal'}

        myobj = {'unicornId': '3', 'unicornName': 'MewTwo', 'unicornClass': 'Psychic'}        
        response = requests.post(f"{api_gateway_base_url}/unicorns", json = myobj)
        print("put Unicorn response")
        print(response.json())
        response = requests.get(f"{api_gateway_base_url}/unicorns/3")
        print(response.json())
        assert response.json() == myobj
        
