import utils.mtgtop8
import utils.scryfall

def main():

    extract()

    transform()

    load()

def extract():
    scryfall_data = utils.scryfall.get_scryfall_data()

    #Given URL is for large standard events of the last 2 months, easily exchanged with data for Modern
    #Maybe in the future
    event_data = utils.mtgtop8.scrape_mtgtop8_data("https://www.mtgtop8.com/format?f=ST&meta=46&cp=")
#def transform():
#do transformations here, potentially with more data sources (though I'm not sure what would be best, this seems pretty comprehensive)

#def load():
#Not sure about how to implement this part yet, but for proper analysis I want to split these tables
#into 'blocks' where the metagame between each set is represented so I can compare them against each other later
#This also helps to reduce query times and confusion
#Do this by deploying every 2 months and adding entries to their appropriate tables based on event dates
#Can fetch these dates programmatically with scryfall

#At the endpoint of this, post warehouse creation, i want to use BI tools to represent these metagame changes

#This is gonna be cool as hell!  can't wait to get this working and show Tristan and Dal.

if __name__ =="__main__":
    main()