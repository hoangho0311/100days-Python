with open("./Input/Names/invited.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Namse/letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        letter_contents.replace("[name]", name)
