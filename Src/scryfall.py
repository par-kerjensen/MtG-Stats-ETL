import pandas as pd
import requests
import json
from bs4 import BeautifulSoup

def get_scryfall_data():
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'MtG Stats ETL Project'
    }
    url = "https://api.scryfall.com/bulk-data/oracle-cards"
    try:
        response = requests.get(url, headers = headers)
    except:
        raise Exception(f'The scryfall request went wrong')
    
    bulk_info = response.json()
    bulk_download_uri = bulk_info.get("download_uri")
    try:
        response = requests.get(bulk_download_uri)
    except:
        raise Exception(f'The scryfall request went wrong')

    cards = json.loads(response.content)
    scryfall_cards = pd.DataFrame(cards)
    return scryfall_cards