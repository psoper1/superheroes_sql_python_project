from database.db_connection import execute_query
from get_bio import get_bio
from get_names import get_names
from open_main_menu import open_main_menu
from ascii_art_two import ascii_art_two
from explosion_ascii_art import explosion_ascii_art
import time
from time import sleep
import pwinput
import os
import sys

ascii_art_two()
sleep(1)
welcome_text = "\nWELCOME TO THE SUPERHERO DATABASE *BETA*\n\n\n"
for char in welcome_text:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
welcome_text2 = "TO MAKE SURE YOU HAVE THE PROPER CLEARENCE, PLEASE ENTER THE ADMINISTRATOR PASSWORD FOR THIS DATABASE:\n\n"
for char in welcome_text2:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
time.sleep(1)
main_pass = pwinput.pwinput(prompt="PASSWORD: ").capitalize()
if main_pass == "Test":
    sleep(1)
    dots = "...      ...      ...      ..."
    for char in dots:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    success = "\nSUCCESS!"
    for char in success:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    os.system('clear')
    open_main_menu()
else:
    string = "\n\nYOU ARE NOT PERMITTED TO VIEW THIS DATABASE AND AGENTS ARE ALREADY ON THEIR WAY TO YOUR LOCATION\n\n"
    for char in string:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    string2 = "GOOD LUCK, YOU'RE GOING TO NEED IT!\n\n"
    for char in string2:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    string3 = "Device will sef destruct in:\n\n"
    for char in string3:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    print("3\n")
    sleep(1)
    print("2\n")
    sleep(1)
    print("1\n")
    sleep(1)
    os.system('clear')
    explosion_ascii_art()
    sleep(3)
    os.system('clear')
    quit()