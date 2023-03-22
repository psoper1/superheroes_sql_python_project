from database.db_connection import execute_query
from get_bio import get_bio
from get_names import get_names
from open_main_menu import open_main_menu
from ascii_art import shrek

inital_answer = input(f"WELCOME TO THE SUPERHERO DATABASE *BETA*\n\n{shrek()}\n\nTO MAKE SURE YOU HAVE THE PROPER CLEARENCE, PLEASE ENTER THE ADMINISTRATOR PASSWORD FOR THIS DATABASE:\n").capitalize()
if inital_answer == "Test":
    print("SUCCESS!")
    open_main_menu()
else:
    print("YOU ARE NOT PERMITTED TO VIEW THIS DATABASE AND AGENTS ARE ALREADY ON THEIR WAY TO YOUR LOCATION\n\nGOOD LUCK, YOU'RE GOING TO NEED IT!")
    quit()