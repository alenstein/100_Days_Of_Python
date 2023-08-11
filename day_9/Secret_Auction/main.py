#!/usr/bin/python3
# Final project of day 9 for 100 Days of python challenge.

import art

end_of_algo = True
bids = {}

def reload(answer=False):
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("ERROR: invalid input")


# find highest bidder
def highest_b(bids={}):
    highest = ""
    val = 0
    for key in bids:
        if int(bids[key]) > val:
            highest = str(key) 
            val = int(bids[key])
        else:
            pass
    print(f"The highest bidder is {highest} with an amount ${val}.")
    
# sys init
while end_of_algo:
    # render bidding logo
    print(art.logo)
    name = input("Enter name: ")
    bid = input("Bid price: $")
    
    bids[name] = bid

    ans = input("Are there other bidders(y or n): ").lower()
    end_of_algo = reload(ans)

    if ans == 'n':
        highest_b(bids)
