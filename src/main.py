from database.db_connection import execute_query
from get_bio import get_bio
from get_names import get_names
from open_main_menu import open_main_menu
from ascii_art import shrek
import time
import pwinput

shrek()
time.sleep(1)
print("WELCOME TO THE SUPERHERO DATABASE *BETA*\n\n\n\nTO MAKE SURE YOU HAVE THE PROPER CLEARENCE, PLEASE ENTER THE ADMINISTRATOR PASSWORD FOR THIS DATABASE:\n\n")
main_pass = pwinput.pwinput(prompt="PASSWORD: ").capitalize()
if main_pass == "Test":
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("SUCCESS!")
    time.sleep(1)
    open_main_menu()
else:
    print("\n\nYOU ARE NOT PERMITTED TO VIEW THIS DATABASE AND AGENTS ARE ALREADY ON THEIR WAY TO YOUR LOCATION\n\n")
    time.sleep(2)
    print("GOOD LUCK, YOU'RE GOING TO NEED IT!\n\n")
    time.sleep(2)
    print("Device will sef destruct in:\n")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    quit()