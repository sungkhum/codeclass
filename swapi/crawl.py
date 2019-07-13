#
# Star Wars Crawl
#
# by: Nathan Wells
#

import argparse
import json
import io
import time

parser = argparse.ArgumentParser()
parser.add_argument("what_movie", type=str, help="Name the movie for the opening crawl you want to watch.")

args = parser.parse_args()
#movie = args.what_movie.center(80)
movie = args.what_movie
# user args.what_movie for the user to choose what movie


with open('films.json') as json_file:  
    films = json.load(json_file)
    for film in films:
        if film['fields']['title'] == movie:
            print(film['fields']['title'].center(80))
            star_wars = "________  _________  ________  ________          ___       __   ________  ________  ________      \r\n|\\   ____\\|\\___   ___\\\\   __  \\|\\   __  \\        |\\  \\     |\\  \\|\\   __  \\|\\   __  \\|\\   ____\\     \r\n\\ \\  \\___|\\|___ \\  \\_\\ \\  \\|\\  \\ \\  \\|\\  \\       \\ \\  \\    \\ \\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\___|_    \r\n \\ \\_____  \\   \\ \\  \\ \\ \\   __  \\ \\   _  _\\       \\ \\  \\  __\\ \\  \\ \\   __  \\ \\   _  _\\ \\_____  \\   \r\n \\|____|\\  \\   \\ \\  \\ \\ \\  \\ \\  \\ \\  \\\\  \\|       \\ \\  \\|\\__\\_\\  \\ \\  \\ \\  \\ \\  \\\\  \\\\|____|\\  \\  \r\n    ____\\_\\  \\   \\ \\__\\ \\ \\__\\ \\__\\ \\__\\\\ _\\        \\ \\____________\\ \\__\\ \\__\\ \\__\\\\ _\\ ____\\_\\  \\ \r\n   |\\_________\\   \\|__|  \\|__|\\|__|\\|__|\\|__|        \\|____________|\\|__|\\|__|\\|__|\\|__|\\_________\\\r\n   \\|_________|                                                                        \\|_________|\r\n"
            star_wars_crawl = io.StringIO(star_wars)
            for line in star_wars_crawl:
                 print(line.center(80))
                 time.sleep(0.2)
            crawl_line = io.StringIO(film['fields']['opening_crawl'])
            for line in crawl_line:
                 print(line.center(80))
                 time.sleep(0.2)


