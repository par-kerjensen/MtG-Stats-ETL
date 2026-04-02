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
    #Add Exception Handling Here

    response = requests.get(bulk_download_uri)

    cards = json.loads(response.content)
    scryfall_cards = pd.DataFrame(cards)
    return scryfall_cards

# def get_spicerack_data():
#     headers = {
#         'Accept': 'application/json',
#         'User-Agent': 'MtG Stats ETL Project'
#     }
#     parameters = {
#         'num_days': 365,
#         'event_format': 'Standard',
#         'decklist_as_text': True
#     }
#     url = "https://api.spicerack.gg/api/export-decklists/"
#     try:
#         response = requests.get(url, headers = headers, params = parameters)
#     except:
#         raise Exception(f'The spicerack.gg request went wrong')
#     events = json.loads(response.content)
#     events_data = pd.DataFrame(events)
#     return events_data

# def get_topdeck_data():
#     headers = {
#         'Accept': 'application/json',
#         'User-Agent': 'MtG Stats ETL Project',
#         'Authorization': 'b0bae8ad-e4b8-4ea3-814d-0bcb1d49d66f'    
#     }
#     parameters = {
#         'game': 'Magic: The Gathering',
#         'format': 'Standard',
#         'last': 14
#     }
#     url = "https://topdeck.gg/api/v2/tournaments"
#     try:
#         response = requests.post(url, headers = headers, json = parameters)
#     except:
#         raise Exception(f'The topdeck.gg request went wrong')
#     events = json.loads(response.content)
#     events_data = pd.DataFrame(events)
#     return events_data

#outline for scraper here:
#Firstly, find the number of pages in the past events data using bs4
#iterate over each page and scrape every event link
#Each event link contains several more individual decklist links, compile those into a list
#Scrape the decklist from each link, including name, maindeck subdivided by card type, and sideboard
#Conver the list of decklists into a dataframe and return it to the main file.

def scrape_mtgtop8_data():
    url_fragment = "https://www.mtgtop8.com/format?f=ST&meta=46&cp="
    page_count = find_page_count(url_fragment)
    


#Iterates over page buttons on events column
#Returns number of pages
def find_page_count(url_fragment):
    largest_page = 1
    while True:
        response = requests.get(url_fragment + str(largest_page))
        soup = BeautifulSoup(response.text, "html.parser")

        #Annoying way to find largest number button on the page selector
        high_page = soup.find('div', string = "Next").previous
        if high_page == largest_page:
            break
        else:
            largest_page = high_page
    return largest_page