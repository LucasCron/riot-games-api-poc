import os

import requests

api_key = os.environ['API_KEY']
parameters = {"api_key": api_key}


def get_from_riot_api(url):
    return requests.get(url, parameters).json()
