import random

import sys
sys.path.append("..")

from src.card import Card 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
       
class Deck():
    '''
    a class that allows to create a 52 cards game deck and shuffle it
    '''

    def __init__(self):
        self.all_cards = []
    
        for suit in suits :
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
        # Creation of each card by iteration through suits and ranks & Add to the deck

    def __str__(self) -> int:
        return len(self.all_cards)
    
    def __getitem__(self, index):
        # Implement logic to retrieve item at the given index
        # For example, return the card at the specified index
        return self.all_cards[index]
    
    def shuffle(self, amount=3):
        for i in range(amount):
            random.shuffle(self.all_cards)
    
    def deal_one(self):
        # deal the last card of the deck
        return self.all_cards.pop()
    
    def print_cards(self):
        print(self.all_cards[-1])
        print(self.all_cards[0])

