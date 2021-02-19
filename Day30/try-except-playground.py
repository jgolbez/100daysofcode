

## Handling IndexError
#fruits = ["Apple", "Pear", "Orange"]
#
#TODO: Catch the exception and make sure the code runs without crashing.
#def make_pie(index):
#    try:
##        fruit = fruits[index]
#    except IndexError:
#        print("Fruit pie")
##    else:
#       print(fruit + " pie")
#make_pie(566)


## KeyError Handling
#facebook_posts = [
#    {'Likes': 21, 'Comments': 2},
#    {'Likes': 13, 'Comments': 2, 'Shares': 1},
#    {'Likes': 33, 'Comments': 8, 'Shares': 3},
##    {'Comments': 4, 'Shares': 2},
#    {'Comments': 1, 'Shares': 1},
#    {'Likes': 19, 'Comments': 3}
#]
#
#total_likes = 0
#
#for post in facebook_posts:
#    try:
#        total_likes = total_likes + post['Likes']
#    except KeyError:
#        pass
#
#print(total_likes)





'''
#KeyError Handling with NATO Alphabet

import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato_df)
#DONE Create Dict in this format:
# {"A" : "Alpha", "B": "Bravo"}
nato_dict = {row.letter:row.code for index, row in nato_df.iterrows()}

#DONE Create a list of phonetic codes from user-inputted word
# Enter a word: Thomas
# ['Tango', 'Hotel, 'Oscar, 'Mike', 'Alpha', 'Sierra']
running = True

while running:
    user_word = input("Enter a word: ").upper()
    try:
        user_nato_word = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Please only use letters")
    else:
        running = False
        print(user_nato_word)
'''


