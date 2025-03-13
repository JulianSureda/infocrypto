import os
import requests
from dotenv import load_dotenv
import json

#ENV SETTINGS

load_dotenv()

# API SETUP
API_KEY = os.getenv("CC_API_KEY")
BASE_URL = "https://api.coincap.io/v2/"

def CoinData(COIN_ID):
    #GET PROTOCOL
    url = f"{BASE_URL}assets/{COIN_ID}"
    response = requests.get(url)
    data = response.json()
    return data

