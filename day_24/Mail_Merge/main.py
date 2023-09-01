#!/usr/bin/python3
# TODO: Create a letter using starting_letter.txt
PLACE_HOLDER = "[name]"

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as stl:
    letter = stl.read()
    # Replace the [name] placeholder with the actual name.
    for name in names:
        the_name = name.strip()
        new_letter = letter.replace(PLACE_HOLDER, the_name)

        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/{the_name}_letter.txt", "w") as outbox:
            outbox.write(new_letter)
