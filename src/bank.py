import random
from .card import Card
from .deck import Deck
from .player import Player 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Bank():
  def __init__(self, owner, type_owner, bank = 20):
    self.owner = owner.upper()
    self.type_owner = type_owner
    self.bank = bank
    self.bet = 0

  def __str__(self):
    return f'{self.owner}, you have {self.bank} chips available.'

  def bank_description(self):
    return f"Bank of {self.type_owner} {self.owner}, with {self.bank} Chips."
    

  def win_bet(self):
      self.bank += self.bet
    
  def lose_bet(self):
      self.bank -= self.bet
