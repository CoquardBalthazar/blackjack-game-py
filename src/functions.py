import random
from .card import Card
from .deck import Deck
from .player import Player
from .bank import Bank

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

def hit(deck, player_hand):
    player_hand.add_card(deck.deal_one())
    player_hand.adjust_for_ace()

def take_bet(bank):
     while True:
        try:
            bank.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if bank.bet > bank.bank:
                print("Sorry, your bet can't exceed",bank.bank)
            else:
                break

def hit_or_stand(deck,player_hand, var_turn_on):
    global turn_on  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,player_hand)  # hit() function defined above
            var_turn_on = True
            return var_turn_on

        elif x[0].lower() == 's':
            print('\n' + "Player stands. Dealer is playing.")
            turn_on = False
            var_turn_on = False
            return var_turn_on

        else:
            print('\n' + "Sorry, please try again.")
            continue
        break

def player_busts(player,dealer,bank):
    print(f"Player {player.name} busts!")
    bank.lose_bet()

def player_wins(player,dealer,bank):
    print(f"Player {player.name} wins!")
    bank.win_bet()

def dealer_busts(player,dealer,bank):
    print(f"Dealer {dealer.name} busts!")
    bank.win_bet()
    
def dealer_wins(player,dealer,bank):
    print(f"Dealer {dealer.name} wins!")
    bank.lose_bet()
    
def push(player,dealer):
    print(f"Dealer and Player tie! It's a push.")

def other_hand_input():
    while True:
        try:
            other_hand = input("Would you like to play another hand? Enter 'y' or 'n' ").lower()
            if other_hand not in ['y', 'n']:
                raise ValueError(f"Invalid input: {other_hand}. Please enter 'y' or 'n'.")
            return other_hand
        except ValueError as e:
            print(e)



''' CORRECTION Udemy Course :
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

QUICK NOTES ABOUT PRINT STATEMENTS:
* The asterisk <code>*</code> symbol is used to print every item in a collection, and the <code>sep='\n '</code> argument prints each item on a separate line.
* In the fourth line where we have
      print('',dealer.cards[1])
    the empty string and comma are there just to add a space.
- Here we used commas to separate the objects being printed in each line. If you want to concatenate strings using the <code>+</code> symbol, then you have to call each Card object's \_\_str\_\_ method explicitly, as with
      print(' ' + dealer.cards[1].__str__())    
'''