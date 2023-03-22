from database.db_connection import execute_query
from get_bio import get_bio
from get_names import get_names

def open_main_menu():
    main_menu = input("\nMAIN MENU\n\nWhat would you like to do?\n\n1. View all heroes\n2. Update information about a specific hero\n3. Add a new hero\n4. Delete a hero\n\nPlease choose an option above\n")
    
    if main_menu == "1":
        print("\n\nALL HEROES\n----------\n")
        get_names()
        print("\n")
        get_bio()
    elif main_menu == "2":
        print("\n\nALL HEROES\n----------\n")
        get_names()
        update = input("\nSelect a hero to update\n")
        query3 = f"SELECT name from heroes WHERE id = {update}"
        update_query = execute_query(query3).fetchone()
        print(f"Updating... {update_query[0]}")
        what_to_update = input("\nWhich would you like to update? (Select One)\n\n1. Name\n\n2. Bio\n\n")
        if what_to_update == "1":
            name_change = input(f"What would you like to change {update_query[0]}s' name to?\n")
        
            change_query = f"UPDATE heroes SET name = '{name_change}' WHERE id = {update}"
            name_query = execute_query(change_query)
            print(f"You have changed their name to {name_change}")
    elif main_menu == "3":
        new_name = input("Enter the name of the new hero:\n")
        new_bio = input(f"Enter a bio for {new_name}\n")
        query = f"INSERT INTO heroes (name, about_me, biography) VALUES ('{new_name}', 'null', '{new_bio}')"
        new_name_query = execute_query(query)
        print(f"{new_name} has been added to the team!\n")
    elif main_menu == "4":
        print("\n\nALL HEROES\n----------\n")
        get_names()
        print("\n")
        delete = input("Enter the hero by name (Case Sensitive) you wish to delete:\n")
        query = f"DELETE FROM heroes WHERE name LIKE '{delete}%'"
        delete_query = execute_query(query)
        print(f"{delete} has been removed from the team!")