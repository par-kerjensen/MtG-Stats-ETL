import pandas


#Todo Here + spitballing
#dataframe is essentially complete, but we can do a lot with enrichment here
#I want to replace the cardnames in each dictionary entry in the decklist field with scryfall card objects
#From those we can create aggregate fields, specifically card type counts, deck price, color identity, and avg cmc

def enrich_data(card_df, scryfall_df):
    card_df[['Main Deck', 'Sideboard']] = card_df[['Main Deck', 'Sideboard']].apply(replace_decklist, args = (scryfall_df,))

def replace_decklist(decklist_df, scryfall_df):
    print("starting new apply!")
    print(decklist_df)

#def add_aggregate_fields(card_df):

