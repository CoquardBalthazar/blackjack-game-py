import random
from .card import Card 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Deck():
    '''
    a class that allows to create a 52 cards game deck and shuffle it

    Methods :
    - __str__(self) : return card name (rank & suit)
    - __len__(self)
    - __getitem__(self, index)
    - shuffle(self, amount=3) : return value card
    - deal_one(self)
    - length(self)
    '''

    def __init__(self):
        self.deck = []
    
        for suit in suits :
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)
        # Creation of each card by iteration through suits and ranks & Add to the deck

    def __str__(self) -> str:
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n '+ card.__str__() ## Add the name of the card (rank, suit)
        return 'The deck is composed of :' + deck_composition
        
    def __len__(self) -> int:
        return len(self.deck)
    
    def __getitem__(self, index):
        # Implement logic to retrieve item at the given index
        # For example, return the card at the specified index
        return self.deck[index]
    
    def shuffle(self, amount=3):
        for i in range(amount):
            random.shuffle(self.deck)
    
    def deal_one(self):
        # deal the last card of the deck
        return self.deck.pop()
    
    def return_one(self, card_to_append):
        return self.deck.append(card_to_append)

