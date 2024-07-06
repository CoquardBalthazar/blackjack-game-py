import random
from .card import Card
from .deck import Deck 
from .player import Player

deck = Deck()

player = Player("TeSt", "p")
player.add_card(deck.deal_one())
player.add_card(deck.deal_one())



dealer = Player("TeSt", "d")
dealer.add_card(deck.deal_one())
dealer.add_card(deck.deal_one())

print(player.__str__())
print(player.announce_cards())
print(dealer.__str__())
print(dealer.announce_cards())
