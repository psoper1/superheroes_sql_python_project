from database.db_connection import execute_query

def get_bio():
    update = input("\nSelect a hero:\n")
    # Add more code here to finish statement
    query = f"SELECT name from heroes WHERE id = {update}"
    query3 = f"SELECT biography from heroes WHERE id = {update}"
    name = execute_query(query).fetchone()
    update_query = execute_query(query3).fetchone()
    print(f"\nHERO: {name[0]}\nBIO: {update_query[0]}")

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
    query3 = f"SELECT name from heroes WHERE id = {update}"
    update_query = execute_query(query3).fetchone()
    print(update_query[0])
    # [int(update) - 1]
elif main_menu == "3":
    # Add code here to finish statement
    pass
elif main_menu == "4":
    print("\n\nALL HEROES\n----------\n")
    get_names()
    print("\n")
    delete = input("Choose a hero you wish to delete:\n")
    # Add more code here to finish statement


