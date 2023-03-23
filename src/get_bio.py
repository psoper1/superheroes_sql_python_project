from database.db_connection import execute_query
import time
import os
from time import sleep
import sys

def get_bio():
    string = "\nSelect a hero to view more information:\n"
    for char in string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    update = input("\n")
    query = "SELECT name, biography from heroes WHERE id = %s"
    selected_hero = execute_query(query, (update, )).fetchone()
    os.system('clear')
    print(f"\n\nHERO: {selected_hero[0]}\n\nBIO: {selected_hero[1]}\n\nABILITIES: {get_abilities(update)}\n")

def get_abilities(update):
    abilities = """SELECT ability_types.name AS ability_name
                    FROM heroes
                    LEFT JOIN abilities
                    ON heroes.id = abilities.hero_id
                    LEFT JOIN ability_types
                    ON abilities.ability_type_id = ability_types.id
                    WHERE heroes.id = %s"""  
    abilities_query = execute_query(abilities, (update, )).fetchall()
    ability_string = []
    for ability in abilities_query:
        ability_string.append(ability[0])
    return ", ".join(ability_string)
    