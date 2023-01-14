# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    lines = letter_file.readlines()
    with open("./Input/Names/invited_names.txt", mode="r") as names_file:
        names = names_file.readlines()
        for i in names:
            stripped_name = i.strip()
            with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as output_file:
                for j in lines:
                    x = j.replace("[name]", stripped_name)
                    output_file.write(x)


