from database.db_connection import execute_query
from get_bio import get_bio
from get_names import get_names
import time
import os
from time import sleep
import sys

def open_main_menu():
    print(f"""\n
-------------------Main Menu----------------------|
--------------------------------------------------|
-----What would you like to do?-------------------|
--------------------------------------------------|
-----1. View all heroes---------------------------|
-----2. Update information about a specific hero--|
-----3. Add a new hero----------------------------|
-----4. Delete a hero-----------------------------|
--------------------------------------------------|""")
    choose_option = ("Please choose an option above---------------------|\n")
    for char in choose_option:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    main_menu = input("\n")
    
    if main_menu == "1":
        os.system('clear')
        menu_one()
    elif main_menu == "2":
        os.system('clear')
        menu_two()
    elif main_menu == "3":
        os.system('clear')
        menu_three()
    elif main_menu == "4":
        os.system('clear')
        menu_four()

def menu_one():
    print("\n\n-------------------All Heroes---------------------|\n--------------------------------------------------|\n")
    get_names()
    print("--------------------------------------------------|")
    print("--------------------------------------------------|")
    get_bio()
    main_or_quit()

def menu_two():
    print("\n\n-------------------All Heroes---------------------|\n--------------------------------------------------|\n")
    get_names()
    print("--------------------------------------------------|")
    print("--------------------------------------------------|")
    string = "\nSelect a hero to update:\n"
    for char in string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    update = input("\n")
    query3 = "SELECT name from heroes WHERE id = %s"
    update_query = execute_query(query3, (update,)).fetchone()
    os.system('clear')
    print(f"\nUpdating... {update_query[0]}")
    what_to_update = input("\nWhich would you like to update? (Select One)\n\n1. Name\n\n2. Bio\n\n")
    if what_to_update == "1":
        os.system('clear')
        name_change = input(f"What would you like to change {update_query[0]}s' name to?\n")
        change_query = "UPDATE heroes SET name = %s WHERE id = %s"
        name_query = execute_query(change_query, (name_change, update,))
        os.system('clear')
        string = "You have changed their hero name to: \n\n"
        for char in string:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(1)
        print("\n")
        print(f"{name_change}")
        print("\n\n")
    main_or_quit()

def menu_three():
    print("\n\n---------------New Hero Creation------------------|\n--------------------------------------------------|\n\n")
    string = "Enter the name of the new hero: \n"
    for char in string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    new_name = input("")
    print("\n--------------------------------------------------|\n\n")
    bio_string = "Enter a bio for "
    for char in bio_string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    new_bio = input(f"{new_name}: \n")
    print("\n--------------------------------------------------|\n\n")
    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, 'null', %s)"
    new_name_query = execute_query(query, (new_name, new_bio,))
    name_string = f"{new_name} has been added to the team!\n\n"
    for char in name_string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    main_or_quit()

def menu_four():
    print("\n\n-------------------All Heroes---------------------|\n--------------------------------------------------|\n")
    get_names()
    print("--------------------------------------------------|")
    print("--------------------------------------------------|")
    delete_string = "Enter the ID of the hero you wish to delete:\n"
    for char in string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    delete = input("\n")
    query = "DELETE FROM heroes WHERE id = %s"
    delete_query = execute_query(query, (delete,))
    string = f"Hero ID#{delete} has been removed from the team!"
    for char in string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    # print(f"Hero ID#{delete} has been removed from the team!")
    main_or_quit()

def main_or_quit():
    string = "\n\nPlease press Enter or to return to the main menu or Q to exit the terminal:\n"
    for char in string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    back_to_menu = input("\n").capitalize()
    if back_to_menu == "":
        os.system('clear')
        open_main_menu()
    elif back_to_menu == "Q":
        os.system('clear')
        quit()