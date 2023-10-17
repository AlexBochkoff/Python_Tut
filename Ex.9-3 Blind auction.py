from replit import clear

from BlindAuctionArt import logo
print(logo)
print("Welcome to the secret auction program.")


def highest_bid_amnt(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amnt = bidding_record[bidder]
    if bid_amnt > highest_bid:
      highest_bid = bid_amnt
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids_dict = {}
end_biding = False

while not end_biding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids_dict[name] = bid
  others = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  if others == 'no':
    end_bidding = True
    highest_bid_amnt(bids_dict)
  elif others == 'yes':
    clear()