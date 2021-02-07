import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato_df)
#DONE Create Dict in this format:
# {"A" : "Alpha", "B": "Bravo"}
nato_dict = {row.letter:row.code for index, row in nato_df.iterrows()}

#DONE Create a list of phonetic codes from user-inputted word
# Enter a word: Thomas
# ['Tango', 'Hotel, 'Oscar, 'Mike', 'Alpha', 'Sierra']
user_word = input("Enter a word: ").upper()
user_nato_word = [nato_dict[letter] for letter in user_word]
print(user_nato_word)



