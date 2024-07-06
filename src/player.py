import random
from .card import Card
from .deck import Deck 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Player():
    '''
    A class that symbolizes the hand of the player (human(s) & computer dealer).´
    Methods :
    - __str__(self)
    - add_card(self, card) : Add card to player hand.
    - announce_cards(self, amount=1) : Announce player's cards based on player type (player, dealer)
    - adjust_for_ace(self) : Adjust property value to not depass 21 if there is an ace in the player hand
    - return_cards(self, amount=1) : Returns a string of all the cards
    - clear_value(self) : Clear the value of the player's hand and Return True once done
    - total_value(self) : Indicate the value of the player's hand
    '''

    def __init__(self, name, type):
        # Type : "player" or "dealer"
        # bank : minimum chips value hold by the player

        # Check for input type
        if type.lower() in ["player", "dealer"] or type.lower() in ["p", "d"] :
            if type.lower() == "p" or type.lower() == "player":
                self.type = "player"

            elif type.lower() == "d" or type.lower() == "dealer":
                self.type = "dealer"

            else:
                raise ValueError("Invalid 'type' parameter. It must be 'player' or 'dealer'.")
            
        self.name = name.upper()
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return f'{self.name} is a {self.type}'
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

    def return_cards(self, amount=1):
        # method that return one or all the cards hold by the player (player, dealer)
        if not self.cards:
            return "No cards in hand."
        if amount != 1:
          return '\n ' + '\n '.join(map(str, self.cards))
        else :
            return str(self.cards[0]) 
        
    def announce_cards(self, amount=1):
        # method that prints the cards of the player, based on its type (player, dealer) and the amount of cards to print
        if self.type in ["player","p"] :
            print('\n' + f'At the moment {self.name} holds these cards : {self.return_cards(len(self.cards))}')
        
        else :
            if amount == 1:
                print('\n' + f'The visible card of {self.name} is the {self.return_cards(1)}.')
            
            else:
                print('\n' + f'At the moment {self.name} holds these cards : {self.return_cards(len(self.cards))}')
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
          self.value -= 10
          self.aces -= 1
    
  