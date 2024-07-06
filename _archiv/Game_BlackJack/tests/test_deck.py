import unittest

import sys
sys.path.append("..")

from src.deck import Deck

class TestDeck(unittest.TestCase):

     # Test deck creation first card
    def test_creation_deck_first_card (self):
        deck = Deck()
        result = str(deck.all_cards[0])
        self.assertEqual(result, 'Two of Hearts')

    # Test deck creation last card
    def test_creation_deck_last_card (self):
        deck = Deck()
        result = str(deck.all_cards[-1])
        self.assertEqual(result, 'Ace of Clubs')
    
    # Test __str__ when deck is full
    def test_string_length (self):
        deck = Deck()
        result = len(deck.all_cards)
        self.assertEqual(result, 52) 

    # Test deal_one : check the last card when poping it Ace Clubs
    def test_deal_one (self):
        deck = Deck()
        result = str(deck.deal_one())
        self.assertEqual(result, "Ace of Clubs") 

    # Test deal_one length after pop one
    def test_creation_deck_first (self):
        deck = Deck()
        deck.deal_one()
        result = len(deck.all_cards)
        self.assertEqual(result, 51) 