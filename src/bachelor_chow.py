#!/usr/bin/python3

import time
import json
from json2html import *
import random

def get_recipe():
    recipe_json=open("db-recipes.json")

    # Load the recipe json from the file into a dictionary
    all_recipes=json.load(recipe_json)

    # Get all of the keys
    recipe_keys=list(all_recipes.keys())

    # randomly pick one
    recipe_entry=random.choice(recipe_keys)

    # Get the dictionary entry, this will be in json format
    recipe=all_recipes[recipe_entry]

    # convert the dictionary to a json string
    recipe_json_string=json.dumps(recipe)

    # Take the json formatted recipe and convert to html
    html=json2html.convert(json=recipe_json_string)

    # open a file named index.html
    index_file=open(file="/root/html/index.html", mode="w")
    # write to the file
    index_file.write(html)

    recipe_json.close()
    index_file.close()

def main():
    while True:
        get_recipe()
        time.sleep(60)

if __name__ == "__main__":
    main()
