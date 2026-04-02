import extract_data

def main():
    #scryfall_data = extract_data.get_scryfall_data()
    #scryfall_data.info()
    event_data = extract_data.scrape_mtgtop8_data()

if __name__ =="__main__":
    main()