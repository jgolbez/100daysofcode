from game_data import data as gd
from art import logo, vs
import os
import random

#Track winner data for subsequent rounds, is there a winner? This affects whether we draw new data for comparison or keep what we have from previous
isWinner = False
winner_data = {
    'name' : 'Foo',
    'follower_count' : 0,
    'description': 'Fighter',
    'country': 'Grohlistan',
    'winner_index' : 0 
}
score = 0
#We need to know how many entries exist to choose from randomly, this examines the list and gives us the end of the range
choice_list_length = len(gd)

#Clear screen after every choice to present new choice
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Return winner to compare against choice
def compare_followers(a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return "A"
    else:
        return "B"

#If there's already a previous winner, draw the comparison data from previous winner data. Otherwise pull two new comparisons
def high_low():
    clear()
    global isWinner
    global winner_data
    global score  
    #If there is a previous winner, load that data into A to keep the streak going. Otherwise generate new data for A
    if isWinner:
        a_name = winner_data['name']
        a_follower_count = winner_data['follower_count']
        a_description = winner_data['description']
        a_country = winner_data['country']
        a_index = winner_data['winner_index']
    else:
        a_index = random.randint(0, choice_list_length)
        a_name = gd[a_index]['name']
        a_follower_count = gd[a_index]['follower_count']
        a_description = gd[a_index]['description']
        a_country = gd[a_index]['country']
    ##print(f"DEBUGGING:\n A_NAME: {a_name} A_FOLLOWER_COUNT: {a_follower_count} A_DESCRIPTION: {a_description} A_COUNTRY: {a_country}")
    #Regardless of whether we retain A or draw new data, the choice for B is always new
    b_index = random.randint(0, choice_list_length)
    # Ensure the choices are not the same choice
    while b_index == a_index:
        b_index = random.randint(0, choice_list_length)
    b_name = gd[b_index]['name']
    b_follower_count = gd[b_index]['follower_count']
    b_description = gd[b_index]['description']
    b_country = gd[b_index]['country']
    ##print(f"DEBUGGING:\n B_NAME: {b_name} B_FOLLOWER_COUNT: {b_follower_count} B_DESCRIPTION: {b_description} B_COUNTRY: {b_country}")
    print(logo)
    if isWinner:
        print(f"You're right! Current score is {score}")
    print(f"Compare {a_name}, {a_description}, from {a_country}")
    print(vs)
    print(f"Against {b_name}, {b_description}, from {b_country}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    winner = compare_followers(a_follower_count, b_follower_count)
    ##print(f"DEBUG: Choice was: {choice}")
    ##print(f"DEBUG: Winner is {winner}")
    if winner == choice and winner == "A":
        isWinner = True
        winner_data['name'] = a_name
        winner_data['description'] = a_description
        winner_data['follower_count'] = a_follower_count
        winner_data['country'] = a_country
        winner_data['winner_index'] = a_index
        score += 1
    ##    print(f"DEBUG: WINNER NAME IS {winner_data['name']} DESC IS {winner_data['description']} FOLLOW IS {winner_data['follower_count']} COUNTRY IS {winner_data['country']}")
        high_low()
    elif winner == choice and winner == "B":
        isWinner = True
        winner_data['name'] = b_name
        winner_data['description'] = b_description
        winner_data['follower_count'] = b_follower_count
        winner_data['country'] = b_country
        winner_data['winner_index'] = b_index
        score += 1
    ##    print(f"DEBUG: WINNER NAME IS {winner_data['name']} DESC IS {winner_data['description']} FOLLOW IS {winner_data['follower_count']} COUNTRY IS {winner_data['country']}")
        high_low()
    else:
        isWinner = False
        score = 0
        play_again = input("Sorry! That's not the right choice. Do you want to play again? Y/N\n").upper()
        if play_again =="Y":
            high_low()
high_low()
