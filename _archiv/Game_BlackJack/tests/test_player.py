import unittest
import pytest
from unittest.mock import patch

import sys
sys.path.append("..")

from src.player import Player
from src.deck import Deck


# CLASS Test_player_creation ----------------------------

    
class TestPlayerCreation(unittest.TestCase):
    def setUp(self):
        self.player = Player("JACKSON", "Player", 200)
        self.dealer = Player("BICRAVE", "Dealer", 200)
        self.player_no_bank_input = Player("NOINPUT", "Player")

    # test creation of player : print name and type YES
    def test_printing_player(self):
        result = str(self.player)
        self.assertEqual(result, "JACKSON is a player")
    
    # test creation of dealer : print name and type YES
    def test_printing_dealer(self):
        result = str(self.dealer)
        self.assertEqual(result, "BICRAVE is a dealer")

    # test bank YES
    def test_bank(self):
        result = self.player_no_bank_input.bank
        self.assertEqual(result, 20)


    # test bank status #test no input in player --> 20 YES
    def test_bank_status_no_input(self):
        result = self.player_no_bank_input.bank_status()
        self.assertEqual(result, "NOINPUT, you have 20 chips available.")
        
    # test bank status # test with input 200 --> 200 YES
    def test_bank_status_with_input(self):
        result = self.player.bank_status()
        self.assertEqual(result, "JACKSON, you have 200 chips available.")
        

    # test hit --> append 2 cards YES
    def test_hit(self):
        deck = Deck()
        for card in range(2):
            self.player.hit(deck.deal_one())
            # 1s dealed Card (last created card)= Ace of Clubs
            # 2nd dealed Card (before last created card)= King of Clubs

        result = len(self.player.all_cards)
        self.assertEqual(result, 2)

    #test print one card # test no cards YES
    def test_return_card_no_card(self):
        result = str(self.player.return_cards())
        self.assertEqual(result,"No cards in hand." )

    #test print one card # test no input amount --> 1 card YES
    def test_return_card_no_input(self):
        deck = Deck()
        for card in range(2):
            self.player.hit(deck.deal_one())
        result = str(self.player.return_cards())
        self.assertEqual(result,"Ace of Clubs" )
    
    #test return   # test with input --> 2 cards YES
    def test_return_card_with_input(self):
        deck = Deck()
        for card in range(2):
            self.player.hit(deck.deal_one())

        result = str(self.player.return_cards(2))
        self.assertEqual(result,'Ace of Clubs, King of Clubs' )

    #test print all cards --> for player Jackson, with 2 cards
    def test_announce_cards_player(self):
        deck2 = Deck()
        for card in range(2):
            self.player.hit(deck2.deal_one())
            
        result = self.player.announce_cards()
        self.assertEqual(result,'At the moment JACKSON holds these cards : Ace of Clubs, King of Clubs')
       
    #test print all cards --> for dealer BICRAVE, amount = 1 card
    # Give 2 cards to the dealer
    def test_announce_cards_dealer_one_card(self): 
        deck2 = Deck()
        for card in range(2):
            self.dealer.hit(deck2.deal_one())
        
        result = self.dealer.announce_cards(1)
        self.assertEqual(result,'The visible card of BICRAVE is the Ace of Clubs.')

    #test print all cards --> for type dealer, amount = 2 cards
    def test_announce_cards_dealer_two_card(self):
        deck2 = Deck()
        for card in range(2):
            self.dealer.hit(deck2.deal_one())       
        result = self.dealer.announce_cards(2)
        self.assertEqual(result,'At the moment BICRAVE holds these cards : Ace of Clubs, King of Clubs')

# CLASS Test_bank -------------------------------------------

class TestBank(unittest.TestCase):
    def setUp(self):
        self.player = Player("JACKSON", "Player", 200)

    ''' Test bet input with Error Message
    # Test bet input # test with input letter : return value error
    @patch('builtins.input', side_effect=["abc"])
    def test_bet_input_value_error(self, mock_input):
        result = self.player.bet_input()
        self.assertEqual(result, "Error : Invalid type. Your input must be an integer")
    
    
    @patch('builtins.input', side_effect=["abc"])
    def test_bet_input_value_error(self, mock_input):
        def mock_input_side_effect(*args, **kwargs):
            return "abc"

        mock_input.side_effect = mock_input_side_effect

        with pytest.raises(ValueError, match='Error : Invalid type. Your input must be an integer'):
            self.player.bet_input()
    
    @patch('builtins.input', side_effect=["abc"])
    def test(self, mock_input):
        with self.assertRaises(ValueError) as context:
            self.player.bet_input()

        self.assertTrue('Error : Invalid type. Your input must be an integer' in context.exception)
    '''
    # Test bet input # test integer : return the integer
    @patch('builtins.input', side_effect=[25])
    def test_bet_input_value_25(self, mock_input):
        result = self.player.bet_input()
        self.assertEqual(result, 25)

    # test check possible bet # test possible -->true
    def test_check_possible_bet(self):
        result = self.player.check_possible_bet(25)
        self.assertEqual(result, True)

    # test check possible bet # test impossible bet --> false
    def test_check_possible_25(self):
        result = self.player.check_possible_bet(225)
        self.assertEqual(result, False)

    # test place_bet --> bet that is possible, check the bet player functionality
    def test_place_bet(self):
        result = str(self.player.place_bet(25))
        self.assertEqual(result, 'You placed a bet of 25')


# CLASS Test_value ---------------------------------
class TestValue(unittest.TestCase):
    def setUp(self):
        self.player = Player("JACKSON", "Player", 200)
        self.deck = Deck()

    # Test choose_ace_value # Ace value is 1 --> return 1
    @patch('builtins.input', side_effect=[1])
    def test_choose_ace_value_1(self, mock_input):
        result = self.player.choose_ace_value(self.deck.all_cards[-1])
        self.assertEqual(result, 1)

    # Test choose_ace_value # Ace value is 11 --> return 11
    @patch('builtins.input', side_effect=[11])
    def test_choose_ace_value_11(self, mock_input):
        result = self.player.choose_ace_value(self.deck.all_cards[-1])
        self.assertEqual(result, 11)

    ''' Test choose ace value --> Error message
    # Test choose_ace_value # Ace value is not int --> print type error
    @patch('builtins.input', side_effect=["abc"])
    def test_choose_ace_value_txt(self, mock_input):
        result = self.player(self.deck[-1])
        self.assertEqual(result, "Error : Invalid type. Your input must be an integer" )

    # Test choose_ace_value # Ace value is not not in 1 11 --> print value error
    @patch('builtins.input', side_effect=[5])
    def test_choose_ace_value_out_range(self, mock_input):
        result = self.player(self.deck[-1])
        self.assertEqual(result, "Error : Invalid 'value'. It must be '1' or '11'." )
    '''
    # Test add_value # Test random card --> 2 of Hearts --> value is 2 :
    def test_add_value(self):

        self.player.add_value(self.deck.all_cards[0])
        result = self.player.value_count
        self.assertEqual(result, 2)

    # Test clear value : value of 5 --> printing + true
    def test_clear_value(self):
        self.player.clear_value()
        result = self.player.value_count
        self.assertEqual(result, 0)

    # Test add_value # Test Ace of Clubs ==1 --> value ==1
    @patch('builtins.input', side_effect=[1])
    def test_add_value_1(self, mock_input):
        #self.player.clear_value()
        self.player.add_value(self.deck.all_cards[-1])
        result = self.player.value_count
        self.assertEqual(result, 1)

    # Test add_value # Test Ace = 11 --> value ==11
    @patch('builtins.input', side_effect=[11])
    def test_add_value_11(self, mock_input):
        #self.player.clear_value()
        self.player.add_value(self.deck.all_cards[-1])
        result = self.player.value_count
        self.assertEqual(result, 11)
    
    # Test total-value value of 2 of Hearts --> player value.count is 2
    def test_total_value(self):
        self.player.add_value(self.deck.all_cards[0])
        result = self.player.total_value()
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()