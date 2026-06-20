with open("names.txt", "r") as file:
    names = file.readlines()

with open("letters.txt", "r") as file:
    letter = file.read()

for n in names:
    name = n.strip() # strips the whitespace from the file

    new_letter = letter.replace("[name]", name)

    with open(f"output/{name}.txt", "w") as file:
        file.write(new_letter)

print("Letters created successfully!")