from database.db_connection import execute_query

def get_bio():
    more_info = input("Choose a hero to view more information on that hero: ")
    if more_info == "1":
        query = "SELECT name FROM heroes WHERE id = 1"
        query2 = "SELECT biography FROM heroes"
        name = execute_query(query).fetchone()
        bio = execute_query(query2).fetchone()
        print(f"\nHero: {name[0]}\n")
        print(f"Bio: {bio[0]}\n")
    elif more_info == "2":
        query = "SELECT name FROM heroes WHERE id = 2"
        query2 = "SELECT biography FROM heroes WHERE id = 2"
        name = execute_query(query).fetchone()
        bio = execute_query(query2).fetchone()
        print(f"\nHero: {name[0]}\n")
        print(f"Bio: {bio[0]}\n")
    elif more_info == "3":
        query = "SELECT name FROM heroes WHERE id = 3"
        query2 = "SELECT biography FROM heroes WHERE id = 3"
        name = execute_query(query).fetchone()
        bio = execute_query(query2).fetchone()
        print(f"\nHero: {name[0]}\n")
        print(f"Bio: {bio[0]}\n")
    elif more_info == "4":
        query = "SELECT name FROM heroes WHERE id = 4"
        query2 = "SELECT biography FROM heroes WHERE id = 4"
        name = execute_query(query).fetchone()
        bio = execute_query(query2).fetchone()
        print(f"\nHero: {name[0]}\n")
        print(f"Bio: {bio[0]}\n")
    elif more_info == "5":
        query = "SELECT name FROM heroes WHERE id = 5"
        query2 = "SELECT biography FROM heroes WHERE id = 5"
        name = execute_query(query).fetchone()
        bio = execute_query(query2).fetchone()
        print(f"\nHero: {name[0]}\n")
        print(f"Bio: {bio[0]}\n")
    elif more_info == "6":
        query = "SELECT name FROM heroes WHERE id = 6"
        query2 = "SELECT biography FROM heroes WHERE id = 6"
        name = execute_query(query).fetchone()
        bio = execute_query(query2).fetchone()
        print(f"\nHero: {name[0]}\n")
        print(f"Bio: {bio[0]}\n")

def get_names():
    query = "SELECT name FROM heroes"
    names = execute_query(query).fetchall()
    for count, x in enumerate(names):
        print(f"{count + 1}: {x[0]}")

inital_answer = input("WELCOME TO THE SUPERHERO DATABASE *BETA*\n\n\n\nTO MAKE SURE YOU HAVE THE PROPER CLEARENCE, PLEASE ENTER THE ADMINISTRATOR PASSWORD FOR THIS DATABASE:\n").capitalize()
if inital_answer == "Test":
    print("SUCCESS!")
else:
    print("YOU ARE NOT PERMITTED TO VIEW THIS DATABASE AND AGENTS ARE ALREADY ON THEIR WAY TO YOUR LOCATION\n\nGOOD LUCK, YOU'RE GOING TO NEED IT!")
    quit()

main_menu = input("\nMAIN MENU\n\nWhat would you like to do?\n\n1. View all heroes\n2. Update information about a specific hero\n3. Add a new hero\n4. Delete a hero\n\nPlease choose an option above\n")
    
# answer = input("Would you like to see a list of superheroes? ").capitalize()
if main_menu == "1":
    print("\n\nALL HEROES\n----------\n")
    get_names()
    print("\n")
    get_bio()
elif main_menu == "2":
    print("\n\nALL HEROES\n----------\n")
    get_names()
    update = input("\nSelect a hero to update\n")
    # Add more code here to finish statement
elif main_menu == "3":
    # Add code here to finish statement
    pass
elif main_menu == "4":
    print("\n\nALL HEROES\n----------\n")
    get_names()
    print("\n")
    delete = input("Choose a hero you wish to delete:\n")
    # Add more code here to finish statement


