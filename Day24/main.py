    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#Create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()

#For each name in invited_names.txt replace the [name] placeholder with the actual name.
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

new_name_list = []
for name in name_list:
    new_name = name.strip("\n")
    new_name_list.append(new_name)


#Save the letters in the folder "Output".

for name in new_name_list:
    new_letter = letter_text.replace("[name]", name)
    with open(f"./Output/{name}.txt", mode="w") as invitation:
        invitation.write(new_letter)


