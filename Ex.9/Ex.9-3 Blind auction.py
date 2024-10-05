import os

from BlindAuctionArt import logo
print(logo)
print("Welcome to the secret auction program.")

bids_dict = {}
end_bidding = False

def highest_bid_amnt(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amnt = bidding_record[bidder]
        if bid_amnt > highest_bid:
            highest_bid = bid_amnt
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not end_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids_dict[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if others == 'no':
        end_bidding = True
        os.system("cls")
        highest_bid_amnt(bids_dict)
    elif others == 'yes':
        os.system("cls")
