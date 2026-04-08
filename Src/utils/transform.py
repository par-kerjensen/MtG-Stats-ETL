import pandas as pd


#Todo Here + spitballing
#dataframe is essentially complete, but we can do a lot with enrichment here
#I want to replace the cardnames in each dictionary entry in the decklist field with scryfall card objects
#From those we can create aggregate fields, specifically card type counts, deck price, and avg cmc

def enrich_data(card_df):
    card_df['Main Deck Price'] = card_df['Main Deck'].apply(maindeck_price)

def maindeck_price(card_ser):
    print("this is one execution")
    print(card_ser)

#def add_aggregate_fields(card_df):
    #print("Hello!")
    total_cmc = 0
    type_counts = {"Land": 0, "Creature" : 0, "Artifact" : 0, "Enchantment" : 0, "Planeswalker" : 0, "Battle" : 0, "Instant" : 0, "Sorcery" : 0}
    total_price = 0

