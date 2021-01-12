from os import system
#HINT: You can call clear() to clear the output in the console.

def clear():
    _ = system('clear')




bids = {}
def get_bid():
  bidder_name = input("What is your name?\n")
  bidder_bidval = int(input("What is your bid?\n"))
  bids[bidder_name] = bidder_bidval
  print(f"{bidder_name}, your bid is {bids[bidder_name]}") 
  more_bidders = input("Are there any more bidders, YES or NO\n").upper()
  if more_bidders == "NO":
    clear()
  elif more_bidders == "YES":
    clear()
    get_bid()
  else:
    print("That is not a valid choice")


def compare_bid(bidlist):
  highest_bid = 0
  highest_bidder = ""
  for key, val in bids.items():
    if bids[key] > highest_bid:
      highest_bid = bids[key]
      highest_bidder = key
    else:
      continue
  print(f"The highest bidder is {highest_bidder} with a bid of {highest_bid}")

get_bid()
compare_bid(bids)