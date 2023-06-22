#!/usr/bin/python3
import os
import json

# Load the command data
with open('commands.json', 'r') as file:
    commands = json.load(file)

while True:
    os.system("clear")  # Clear terminal

    # Print the main menu
    for i, category in enumerate(commands.keys(), start=1):
        print(f"{i}. {category}")

    category_num = input("\nSelect a category by number, 'q' to quit: ")

    if category_num.lower() == 'q':
        break

    category = list(commands.keys())[int(category_num) - 1]

    os.system("clear")  # Clear terminal

    # Print the commands menu
    for command, description in commands[category].items():
        print(f"{command} - {description}\n")  # Added newline here for spacing

    command = input("\nType the command you want to learn about, 'back' to return to the category list, or 'q' to quit: ")

    if command.lower() == 'back':
        continue
    elif command.lower() == 'q':
        break

    os.system("clear")  # Clear terminal

    # Retrieve the command detail from 'commands.txt'
    with open('commands.txt', 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith(command + ' '):  # Check if the line starts with the command followed by a space
                # Print the details of the command until an empty line is reached
                for detail_line in lines[i:]:
                    if detail_line.strip() == '':
                        break
                    print(detail_line, end='')
                break

    input("\nPress 'Enter' to return to the category list...")
