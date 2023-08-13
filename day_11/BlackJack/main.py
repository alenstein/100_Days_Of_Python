#!/usr/bin/python3
# Blackjack Project

import random
import art

# Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
    """
        Uses the list cards to return a random card
        11 is the Ace.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = int(random.choice(cards))
    return card
    
# Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
end_of_game = False


# load game function
def load_game(answer=''):
    if answer == 'y':
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    elif answer == 'n':
        end_of_game = True
        print("Game ended.")
    else: 
        print("ERROR: invalid input.")
       

# play the game again 
def reload_game(answer=''):
    user_cards = []
    computer_cards = []
    
    if answer == 'y':
        print("\033c", end="")
        return False
    elif answer == 'n':
        return True
    else:
        print("ERROR: invalid input.")
        return True

# function takes a List of cards as input and returns the score. 
def calculate_score(cards=[]):
    score = 0    
    for card in cards:
        score += int(card)
    if score == 21:
        return 0
    elif 11 in cards:
        if score > 21:
            cards.remove(11)
            cards.append(1)
    else:
        pass        
    return score


def draw(cards=[], score=0):
    if score < 21:
        cards.append(deal_card())
    else:
        print("\t\t\tYou can not draw another card, you lose!")

def winner(user=0, comp=0):
    if user <= 21 and comp <= 21:
        if user > comp:
            print("\t\t\tCongratulations you win!")
        elif comp > user:
            print("\t\t\tYou lose")
        else:
            print("\t\t\tIts a draw")
    elif user > 21:
        print("\t\tYou need to pick another card!")
        ans = input("\t\t\tPick another card?: Type 'y' or 'n' ")
        if ans == 'y':
            new_card = deal_card()
            user += int(new_card)
        else:
            print("\t\t\tGame over you quit!")
            
        if user > comp and ans == 'y':
            print("\t\t\tYou win!")
        else:
            print("\t\t\tComputer wins!")
    elif comp > 21:
        new_card = deal_card()
        comp += int(card)

        if comp > user:
            print("Computer wins!")
        else:
            print("You win!")



while not end_of_game:
    print(art.logo)
    ans = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    load_game(ans)
    user_result = calculate_score(user_cards)
    computer_result = calculate_score(computer_cards)

    print(f"\t\t\t\tScores\n\t\tComputer: {computer_result}\t\tUser: {user_result} ")
    if user_result == computer_result:
        print("\t\t\tIts a draw.")
        end_of_game = False
    elif not user_result == 0:
        if computer_result == 0:
            print("\t\t\tComputer wins.")
            end_of_game = True
        else:
            winner(user_result, computer_result)
    else:
        winner(user_result, computer_result)
    
    ans = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    end_of_game = reload_game(ans)

