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

    scryfall_cards = pd.DataFrame(json.loads(response.content))

    #Add price columns to each row
    price_frame = pd.json_normalize(scryfall_cards['prices'])
    scryfall_cards = pd.merge(scryfall_cards, price_frame, left_index = True, right_index = True)
    
    #Get all cards legal in standard
    legality_frame = pd.json_normalize(scryfall_cards['legalities'])
    standard_cards = scryfall_cards[legality_frame['standard'] == 'legal']

    #Trim useless fields to only the ones used for analytics, clean output
    standard_cards = standard_cards[['name', 'cmc', 'mana_cost', 'type_line', 'color_identity', 'oracle_text', 'power', 'toughness', 'card_faces', 'usd']]
    standard_cards = standard_cards.set_index('name').sort_values(by='name').rename(columns = {'usd': 'price'})

    return scryfall_cards