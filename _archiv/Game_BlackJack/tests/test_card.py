import unittest

import sys
sys.path.append("..")

from src.card import Card

class TestCardClass (unittest.TestCase):

    # Test the printing statement for Ace of Heart
    def test_printing_name_and_value1 (self):
        card = Card("Hearts", "Ace")
        result = str(card)
        self.assertEqual(result, "Ace of Hearts")
    
    # Test the printing statement for Ten of Spades
    def test_printing_name_and_value2 (self):
        card = Card("Spades", "Ten")
        result = str(card)
        self.assertEqual(result, "Ten of Spades")

    # Test Show value for Ace of Heart (supposed to be [1,11])
    def test_show_value_ace (self):
        card = Card("Hearts", "Ace")
        result = card.show_value()
        self.assertEqual(result, [1,11])

    # Test Show value for Ten of Spades
    def test_show_value_ten (self):
        card = Card("Spades", "Ten")
        result = card.show_value()
        self.assertEqual(result, 10)


    