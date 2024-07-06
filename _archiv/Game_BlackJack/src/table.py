from src.card import Card
from src.deck import Deck
from src.player import Player

class Table():
    def __init__(self):
        # Logic placeholder variables declaration
        self.player0 = None
        self.dealer = None
        self.deck = None

        self.game_on = None
        self.round_on = None
        self.turn_on = None
        self.initial_bank = None

    def game_set_up(self):
        '''GAME Set Up

            - Name P0
                >create P0 player
                >create P1 dealer

            - create deck
                >create deck
                >shuffle deck

            - Print game opposes P0 to P1
            - Print the rules

            - how much do you bring to the table?
                >change value bank player
                > save value as initial_bank

            - Are you ready to start ? 
                >print lets start
                >game_on = True
        '''
        # Creation players
        player0_name= input("Player 1 please enter your name : ")
        self.player0 = Player(player0_name, 'player')
        self.dealer = Player('dealer', "dealer")
        print(f"The game opposes {self.player0} to {self.dealer}")
        
        # Creation deck
        self.deck = Deck()
        self.deck.shuffle()

        # Initial Bank
        self.initial_bank = 20

        # Rules explanation :
        print("""
            WELCOME TO BLACKJACK SIMPLIFIED !
            
            Here are the rules. 
              The object is to have a hand with a total value higher than the dealer's without going over 21. 
              Kings, Queens, Jacks and Tens are worth a value of 10. 
              An Ace has the value of 1 or 11. The remaining cards are counted at face value.

            """)
        
        while True:
            ready = input("Are you ready to start ? (y/n) : ")
            if ready in ["y", "yes"]:
                break
            else:
                continue
    
    def bank_set_up(self):
        # Bank value - keep asking until correct value
        while True :
            try :
                bank_player = int(input(f"{self.name}, how much do you want to bring to the table ? : "))
                if type(bank_player) != int:
                    raise ValueError('Invalid type. Your input must be an integer')
                else:
                    self.player0.bank = bank_player
                    self.initial_bank = bank_player
                    break

            except ValueError as ve :
                print(f'Error : {ve}')

        self.game_on = True
    
    def round(self):
        '''
        # ROUND > WHILE LOOP game_on = True
        - bank print (how much does the player has in the bank)
            >check bank >0
                >no : end_game, gameOn False
                >yes : pass
            
        - how much do you bet this round ? 
            >bet_input
            >check possible bet
            >place bet to player bet
        - Distribute 2 cards to dealer and player
        '''
        print(self.player0.bank_status())

        # Check bank not empty
        if self.player0.bank > 0:
            pass
        else:
            self.round_on = False
        
        # Bet for the round
        bet_round = self.player0.bet_input()
        while self.player0.check_possible_bet(bet_round) == False:
            print("You don't have enough money in the bank for this bet, please enter another bet")
            bet_round = self.player0.bet_input()
        self.player0.place_bet(bet_round)
        self.player0.bank -= bet_round #remove bank from bank

        # Distribute 2 cards per players
        for card in range(2):
            self.player0.hit(self.deck.deal_one())
            self.dealer.hit(self.deck.deal_one())
        

    def turn(self):
        '''
        # TURN > WHILE LOOP
        turn = 0 / 1

        turn = 0 :
            - Announce dealer card > return / print cards
            - announce player cards. > return / print cards
            - add value
                - if Ace in player cards :
                    >choose ace value

            - announce hand value player

            - check hand value player 
                -- >21 loses : change turn to p1 dealer
                -- <21 continue

            - what do you wanna do ?
                >hit 
                    > add card to card player
                    > addvalue card
                    > start again loop
                >stop (turn p1 dealer)
        '''
        turn = 0
        while turn ==0:
            #Announce cards
            print(self.dealer.announce_cards(1))
            print(self.player0.announce_cards())
            
            #Clear Hand value player
            self.player0.clear_value()
            print('If you have an Ace, you will be prompted to choose its value.')

            #Update Value
            for card in self.player0.all_cards:
                self.player0.add_value(card)

            #Announce Hand value for turn
            self.player0.total_value()

            #Check hand value
            if self.player0.value_count > 21:
                turn=1
            else :
                pass

            #Action player
            player_action =None
            while player_action not in ["hit","stop"]:
                player_action = input("What do you want to do in this turn? (hit/stop): ").lower()
            if player_action == "hit":
                self.player0.hit(self.deck.deal_one())
            else:
                print(f'You stopped with a total value of {self.player0.value_count}.')
                print("It is now the dealer's turn")
                turn=1
                

        while turn ==1:
            ''' NOTES 
            while gameon = True / True
                - print second card dealer
                - dealer_action = decide dealer action()
                    > won --> dealer_action == tupple and dealer_action[0]==True
                        > gameon False,/ break
                        > announce dealer winner, 
                        > p0 pay the bet = remove the bet from the bank

                        > NOT IN HERE ask to play next round ?
                            >no : game_on = False, end_game
                            >yes : round loop start again

                            
                    > replay --> dealer_action == tupple and dealer_action[0]==False
                        > hit dealer with new card
                        > continue

                    > burst --> else / dealer_action = "Burst"
                        > gameon False, / break
                        > announce player winner round, 
                        > p0 get the bet, 

                        > NOT IN HERE ask to continue play ?
                            >no : game_on = False, end_game
                            >yes : round loop start again

            '''
            while True:
                #Announce cards
                print(self.dealer.announce_cards())

                #Clear Hand value player
                self.dealer.clear_value()
                dealer_action = self.dealer.decide_dealer_action()

                #Player lost / Dealer won 
                if dealer_action == tuple and dealer_action[0]==True :
                    print(f"{self.player0.name}, you lost! {self.dealer.name} won with a total value of {dealer_action[1]}")
                    self.player0.bet = 0
                    turn = None

                #No win, no burst --> replay 
                elif dealer_action == tuple and dealer_action[0]==False:
                    self.dealer.hit(self.deck.deal_one())
                    continue

                #Player won / Dealer burst --> else / dealer_action = "Burst"
                else:
                    print(f"{self.dealer.name} bursted. {self.player0.name} won with a total value of {self.player0.value_count}")
                    self.player0.bank += self.player0.bet
                    turn = None
            

    
    def replay(self):
        while True:
            play_or_not_play = input("What do you want to do? ('play'/'stop') : ")
            if play_or_not_play == 'play':
                return True
                
            elif play_or_not_play == 'stop':
                self.game_on = False
                return False
            else:
                continue

    def end_game(self):
        '''end_game
        - player has not money in bank:
            > you dont have enough money to continue play
            > stop or bring more money in your bank ?
        - player stoped game before:
            > you have xxx in your bank. 
            > if + than initial_bank : Felicitation you won xxx, which is (difference between init and now) than your initial bank value
            > if - than initial_bank : You finish with xxx. Today was not your lucky day, it is xxx less than your initial bak input.
        '''
        # Player has no money left in the bank
        if self.player0.bank <=0:
            print("You don't have enough money to continue play.")
            print(self.player0.bank_status())

        # Player has still some money
        else:
            print(self.player0.bank_status())
            if self.player0.bank > self.initial_bank:
                print(f'Félicitation ! You won {self.player0.bank}, which is {self.player0-self.initial_bank} more than your inital bank value!')
            elif self.player0.bank < self.initial_bank:
                print(f'You finished the game with {self.player0.bank}. That was not your lucky day, it is {abs(self.player0-self.initial_bank)} less than your initial bak input.')
            
            else:
                print(f'You did not lose neither win money. You finish the game with {self.player0.bank}, the same amount as your initial bank value ! ')

    def start_game(self):
        self.game_set_up()
        self.bank_set_up()

        while self.game_on == True :
            self.round_on = True
            while self.round_on == True:
                self.round()

                self.turn_on = True
                while self.turn_on:
                    self.turn()
                    self.turn_on = False

                # Ask to replay
                replay = self.replay()
                if replay == True:
                    continue
                else:
                    self.round_on = False
                    self.game_on = False
            
            self.end_game()
