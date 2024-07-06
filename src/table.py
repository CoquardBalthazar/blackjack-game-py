from .card import Card
from .deck import Deck
from .player import Player
from .bank import Bank
from .functions import *

class Table():
    def __init__(self):
        # Logic placeholder variables declaration
        self.player_hand = None
        self.dealer_hand = None
        self.player_bank = None
        self.deck = None

        self.game_on = None
        self.turn_on = None
    
    def rules(self):
        # Rules explanation :
        print("""
              -------------------------------------------------------------------------------------


            WELCOME TO BLACKJACK SIMPLIFIED !
            
            Here are the rules. 
              The object is to have a hand with a total value higher than the dealer's without going over 21. 
              Kings, Queens, Jacks and Tens are worth a value of 10. 
              An Ace has the value of 1 or 11. The remaining cards are counted at face value.

            
            -------------------------------------------------------------------------------------

            """)
    def players_setup(self):
        
        # Initialize players and their hands + deal 2 cards to each
        player_name = input("Player 1 please enter your name : ")
        self.player_hand = Player(player_name, 'player')

        self.dealer_hand = Player('dealer', "dealer")
        print(f"The game opposes {self.player_hand.name} to {self.dealer_hand.name}")

        # Set up players' bank :
        self.player_bank = Bank(self.player_hand.name, self.player_hand.type, bank = 20) # default value is 20

        while True:
            ready = input("Are you ready to start ? (yes/no) : ")
            if ready in ["y", "yes"]:
                break
            else:
                continue

    def game_setup (self):
        # Creation deck
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand.add_card(self.deck.deal_one())
        self.player_hand.add_card(self.deck.deal_one())

        self.dealer_hand.add_card(self.deck.deal_one())
        self.dealer_hand.add_card(self.deck.deal_one())
    
    def game_reset(self):
        self.player_hand.cards = []
        self.player_hand.value = 0
        self.player_hand.aces = 0
    
        self.dealer_hand.cards = []
        self.dealer_hand.value = 0
        self.dealer_hand.aces = 0

    def player_bet(self):
        # Prompt the Player for their bet
        print(self.player_bank)
        take_bet(self.player_bank)
    
    def turn_player(self):
        print('\n'*3 + "---------------------PLAYER'S TURN---------------------" + '\n'*3)
        # Show cards (but keep one dealer card hidden)
        self.player_hand.announce_cards()
        self.dealer_hand.announce_cards()

        self.turn_on = True
        while self.turn_on:  # recall this variable from our hit_or_stand function
        
            # Prompt for Player to Hit or Stand
            self.turn_on = hit_or_stand(self.deck,self.player_hand, self.turn_on)
            
            # Show cards (but keep one dealer card hidden)
            self.player_hand.announce_cards()
            self.dealer_hand.announce_cards()
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if self.player_hand.value > 21:
                print('\n')
                player_busts(self.player_hand,self.dealer_hand,self.player_bank)
                print("\nPlayer's bank stands at",self.player_bank.bank)
                self.turn_on = False  

    def turn_dealer(self):
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if self.player_hand.value <= 21:
            print('\n'*3 + "---------------------DEALER'S TURN---------------------" + '\n'*3)

            while self.dealer_hand.value < 17:
                hit(self.deck,self.dealer_hand)    
        
            # Show all cards
            self.player_hand.announce_cards()
            self.dealer_hand.announce_cards(len(self.dealer_hand.cards))
            
            # Run different winning scenarios
            if self.dealer_hand.value > 21:
                dealer_busts(self.player_hand,self.dealer_hand,self.player_bank)

            elif self.dealer_hand.value > self.player_hand.value:
                dealer_wins(self.player_hand,self.dealer_hand,self.player_bank)

            elif self.dealer_hand.value < self.player_hand.value:
                player_wins(self.player_hand,self.dealer_hand,self.player_bank)

            else:
                push(self.player_hand,self.dealer_hand)  
        
            # Inform Player of their chips total 
            print("\nPlayer's bank stands at",self.player_bank.bank)
