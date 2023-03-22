from database.db_connection import execute_query
from get_bio import get_bio
from get_names import get_names
import time

def open_main_menu():
    main_menu = input(f"\nMAIN MENU\n\nWhat would you like to do?\n\n1. View all heroes\n2. Update information about a specific hero\n3. Add a new hero\n4. Delete a hero\n\nPlease choose an option above\n")
    
    if main_menu == "1":
        menu_one()
    elif main_menu == "2":
        menu_two()
    elif main_menu == "3":
        menu_three()
    elif main_menu == "4":
        menu_four()

def menu_one():
    print("\n\nALL HEROES\n----------\n")
    get_names()
    print("\n")
    get_bio()
    main_or_quit()

def menu_two():
    print("\n\nALL HEROES\n----------\n")
    get_names()
    update = input("\nSelect a hero to update\n")
    query3 = "SELECT name from heroes WHERE id = %s"
    update_query = execute_query(query3, (update,)).fetchone()
    print(f"Updating... {update_query[0]}")
    what_to_update = input("\nWhich would you like to update? (Select One)\n\n1. Name\n\n2. Bio\n\n")
    if what_to_update == "1":
        name_change = input(f"What would you like to change {update_query[0]}s' name to?\n")
        
        change_query = "UPDATE heroes SET name = '%s' WHERE id = %s"
        name_query = execute_query(change_query, (name_change, update,))
        print(f"You have changed their name to {name_change}")
    main_or_quit()

def menu_three():
    new_name = input("Enter the name of the new hero:\n")
    new_bio = input(f"Enter a bio for {new_name}\n")
    query = "INSERT INTO heroes (name, about_me, biography) VALUES ('%s', 'null', '%s')"
    new_name_query = execute_query(query, (new_name, new_bio,))
    print(f"{new_name} has been added to the team!\n")
    main_or_quit()

def menu_four():
    print("\n\nALL HEROES\n----------\n")
    get_names()
    print("\n")
    delete = input("Enter the ID of the hero you wish to delete:\n")
    query = "DELETE FROM heroes WHERE id = %s"
    delete_query = execute_query(query, (delete,))
    print(f"{delete} has been removed from the team!")
    main_or_quit()

def main_or_quit():
    back_to_menu = input("Please press Enter or to return to the main menu or Q to exit the terminal:\n").capitalize()
    if back_to_menu == "":
        open_main_menu()
    elif back_to_menu == "Q":
        quit()