#
# Star Wars Crawl
#
# by: Nathan Wells
#

import argparse
import json
import io
import time
import csv

#parser = argparse.ArgumentParser()
#parser.add_argument("what_movie", type=str, help="Name the movie for the opening crawl you want to watch.")

#args = parser.parse_args()
#movie = args.what_movie.center(80)
#movie = args.what_movie
# user args.what_movie for the user to choose what movie


with open('people.json') as json_file:  
    films = json.load(json_file)
    myFile = open('star_wars_people.csv', 'w')
    myFields = ['id', 'name', 'height', 'mass', 'eye color']
    writer = csv.DictWriter(myFile, fieldnames=myFields)
    writer.writeheader()
    with myFile: 
        for film in films:
            myFile = open('star_wars_people.csv', 'w')
            with myFile:  
                writer.writerow({'id' : film['pk'], 'name': film['fields']['name'], 'height': film['fields']['height'], 'mass': film['fields']['mass'], 'eye color': film['fields']['eye_color']})

        



 
