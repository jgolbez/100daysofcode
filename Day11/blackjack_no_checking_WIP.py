from os import system
import random
import sys
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_stand = False
dealer_stand = False

def card_score(current_hand):
  total_score = 0
  for card in current_hand:
    total_score += card
  return total_score

def clear():
  system('clear')

def compare(pl_score, dl_score):
  if pl_score > dl_score:
    return "Player"
  elif pl_score == dl_score:
    return "No one"
  else:
    return "Dealer"

def deal_card(current_hand, cardnum):
  for card in range(1, 1 + cardnum):
    current_hand.append(random.choice(cards))
  return current_hand

def is_blackjack(current_hand):
  bl_total = 0
  for card in current_hand:
    bl_total += card
  if bl_total == 21:
    return True
  else:
    return False


def is_busted(current_score):
  if current_score > 21:
    return True  


def has_ace(current_hand):
  if 11 not in current_hand:
    return False
  else:
    return True

def play_again():
  repeat = input("Would you like to play again? Y / N\n").upper()
  if repeat == "Y":
    clear()
    blackjack_start()
  else:
    sys.exit()


def blackjack_start():
  print("Welcome to Blackjack!")
  cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_hand = []
  dealer_hand = []    
  player_stand = False
  dealer_stand = False
  deal_card(player_hand, 2)
  deal_card(dealer_hand, 2)
  print(f"DEBUG: {player_hand}")
  print(f"DEBUG: {dealer_hand}")
  print(f"Your cards:")
  for card in player_hand:
    print(card)
  print(f"Current Player Score: {card_score(player_hand)}")
  print("Dealer Cards:")
  print(str(dealer_hand[0]) + " X")
  if is_blackjack(dealer_hand):
    for card in dealer_hand:
      print(card)
    print(f"Blackjack! Dealer Wins!")
    play_again()
  elif is_blackjack(player_hand):
    for card in player_hand:
      print(card)
    print("Blackjack! Player wins!")
    play_again()
  while not player_stand:
    player_continue = input("Do you want another card? Y or N\n").upper()
    if player_continue == "Y":
      deal_card(player_hand, 1)
      print(player_hand)
      pl_score = card_score(player_hand)
      
      if has_ace(player_hand) and is_busted(pl_score):
        ace_index = player_hand.index(11)
        player_hand[ace_index] = 1
        print("ACE has changed value to 1 from 11")
        pl_score = card_score(player_hand)
      elif not has_ace(player_hand) and is_busted(pl_score):
        print("Busted! Dealer wins!")
        play_again()

      print(f"Current Player Score: {pl_score}")
      for card in player_hand:
        print(card)
    elif player_continue == "N":
      print("Okay, done")
      player_stand = True
      pl_score = card_score(player_hand)
      while not dealer_stand:
        print("Dealer Cards")
        for card in dealer_hand:
          print(card)
        dl_score = card_score(dealer_hand)
        print(f"Current Dealer Score: {dl_score}")
      
        if has_ace(dealer_hand) and is_busted(dl_score):
          ace_index = dealer_hand.index(11)
          dealer_hand[ace_index] = 1
          print("ACE has changed value to 1 from 11")
          dl_score = card_score(dealer_hand)
        elif not has_ace(dealer_hand) and is_busted(dl_score):
          print("Dealer Busted! Player wins!")
          play_again()
        elif dl_score >= 17:
          dealer_stand = True
        else:
          deal_card(dealer_hand, 1)
  who_wins = compare(pl_score, dl_score)
  print(f"{who_wins} wins!")
  play_again()

blackjack_start()