import pandas as pd
import requests
import json
from bs4 import BeautifulSoup

#outline for scraper here:
#Firstly, find the number of pages in the past events data using bs4
#iterate over each page and scrape every event link
#Each event link contains several more individual decklist links, compile those into a list
#Scrape the decklist from each link, including name, maindeck subdivided by card type, and sideboard
#Conver the list of decklists into a dataframe and return it to the main file.

def scrape_mtgtop8_data():
    url_fragment = "https://www.mtgtop8.com/format?f=ST&meta=46&cp="
    page_count = find_page_count(url_fragment)
    decks = []
    for i in range(1, page_count + 1):
        event_links = get_events(url_fragment + str(i))
        for event in event_links:
            decklist_links = get_decklist_links("https://www.mtgtop8.com/" + event)
            for deck in decklist_links:
                decks.append(get_decklist_from_link("https://mtgtop8.com/event" + deck))
    return decks

#Iterates over page buttons on events column
#Returns number of pages
def find_page_count(url_fragment):
    largest_page = 1
    while True:
        try:
            response = requests.get(url_fragment + str(largest_page))
            response.raise_for_status()
        except:
            raise Exception(f'There was an error in finding the page count')
        soup = BeautifulSoup(response.text, "html.parser")

        high_page = soup.find('div', string = "Next").previous
        if high_page == largest_page:
            break
        else:
            largest_page = high_page
    return int(largest_page)

#Get list of event links from one page
#Returns list of url fragments of event pages
def get_events(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        raise Exception(f'There was an error in getting the event links')
    soup = BeautifulSoup(response.text, "html.parser")
    links = [a.get('href') for a in soup.table.find_all('table')[1].find_all('a', href = True)]
    return(links)


#Get list of deck links from one event page
#Returns a list of url fragments of decklist pages
def get_decklist_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        raise Exception(f'There was an error in getting the decklist links')
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.body.find('div', attrs={"style" : "width:25%;"}).find_all('a', href = True, class_ = None)
    links = links[::2]
    del links[0]
    links = [a.get('href') for a in links]

#Get decklist from a given decklist url
#Returns a dictionary of decklist data broken down into its component parts
def get_decklist_from_link(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        raise Exception(f'There was an error getting the decklist data')
    soup = BeautifulSoup(response.text, "html.parser")

