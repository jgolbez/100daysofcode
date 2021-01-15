import random
import os
import sys
keep_playing = True
game_over = False

def play_again():
    play = input("Thanks for playing! Play again? Y / N ?\n").upper()
    if play == "Y":
        os.system("cls" if os.name == "nt" else "clear")
        global game_over
        game_over = False
        guess_game()
    else:
        sys.exit()
    

def guess_game():
    global game_over
    num_answer = random.randrange(1, 100)
    print(f"DEBUG: Answer is {num_answer}")
    print("Welcome to the Number Guessing Game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    if difficulty == "easy":
        attempts_remaining = 10
    elif difficulty == "hard":
        attempts_remaining = 5
    else:
        print("Not a valid choice")
    while not game_over and attempts_remaining > 0:
        guess = int(input("Make a guess: "))
        attempts_remaining -= 1
        if guess == num_answer:
            game_over = True
            print("You guessed it!")
            play_again()
        elif guess > num_answer:
            print("Your guess is too high.")
            print(f"You have {attempts_remaining} attempts remaining.")
        elif guess < num_answer:
            print("Your guess is too low.")
            print(f"You have {attempts_remaining} attempts remaining.")
    print("You have used up all your guesses! You lose.")
    play_again()






guess_game()
