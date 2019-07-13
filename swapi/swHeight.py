#
# Tallest and Shortest Characters in Each Star Wars Film
#

import json
import csv

myCSVFile = open('star_wars_heights.csv', 'w')
myFields = ['movie', 'name of tallest', 'height', 'name of shortest', 'height']
writer = csv.DictWriter(myCSVFile, fieldnames=myFields)
writer.writeheader()

with open('films.json') as json_file:
    films = json.load(json_file)
    max_height = int(0)
    min_height = int(9999)
    max_character = ''
    min_character = ''
    for film in films:
        characters = film['fields']['characters']
        movie = film['fields']['title']
        for id in characters:
        	#print(id)
        	with open('star_wars_people.csv') as myFile:
        		reader = csv.DictReader(myFile)
        		for row in reader:
        			csv_id = row['id']
        			if str(id) == str(csv_id):
        				if row['height'] != 'unknown':
        				    if int(row['height']) > int(max_height):
        				    	max_height = int(row['height'])
        				    	max_character = row['name']
        				    if int(row['height']) < int(min_height):
        				    	min_height = int(row['height'])
        				    	min_character = row['name']
        #print(movie)
        #print(f'Tallest Character: {max_character}')
        #print(f'Max Height: {max_height}')
        #print(f'Shortest Character: {min_character}')
        #print(f'Min Height: {min_height}')
        myCSVFile = open('star_wars_heights.csv', 'w')
        with myCSVFile:  
            writer.writerow({'movie' : movie, 'name of tallest': max_character, 'height': max_height, 'name of shortest': min_character, 'height': min_height})

        


