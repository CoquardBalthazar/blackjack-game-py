from src.card import Card


class Player():
    '''
    a class that creates the players (human(s) & computer dealer) and their cards.
    '''

    def __init__(self, name, type, bank = 20): 
        # type "player" or "dealer"
        # money: money to bring to bet in the game

        # Check for input type
        if type.lower() in ["player", "dealer"] or type.lower() in ["p", "d"] :
            if type.lower() == "p" or type.lower() == "player":
                self.type = "player"

            elif type.lower() == "d" or type.lower() == "dealer":
                self.type = "dealer"

            else:
                raise ValueError("Invalid 'type' parameter. It must be 'player' or 'dealer'.")
        
        self.name = name.upper()
        self.all_cards = []
        self.value_count = 0
        self.bank = bank
        self.bet = 0

    def __str__(self):
        return f'{self.name} is a {self.type}'
    
    def bank_status(self):
        return f'{self.name}, you have {self.bank} chips available.'

    def hit(self, new_card):
        return self.all_cards.append(new_card)
    
    def return_cards(self, amount=1):
        # method that return one or all the cards hold by the player (player, dealer)
        if not self.all_cards:
            return "No cards in hand."
        if amount != 1:
            return ', '.join(map(str, self.all_cards))
        else :
            return str(self.all_cards[0]) 
    
    def announce_cards(self, amount=1):
        # method that prints the cards of the player, based on its type (player, dealer) and the amount of cards to print
        if self.type in ["player","p"] :
            return f'At the moment {self.name} holds these cards : {self.return_cards(len(self.all_cards))}'
        
        else :
            if amount == 1:
                return f'The visible card of {self.name} is the {self.return_cards(1)}.'
            
            else:
                return f'At the moment {self.name} holds these cards : {self.return_cards(len(self.all_cards))}' 

    def bet_input(self) :
        # method that keep asking for a bet input until format is int

        while True :
            try :
                bet_player = int(input(f"{self.name}, how much do you want to bet in this round ? : "))

                if type(bet_player) != int:
                    raise ValueError('Invalid type. Your input must be an integer')
                else:
                    return bet_player

            except ValueError as ve :
                print(f'Error : {ve}')
            

    def check_possible_bet(self, bet_player) -> bool:
        #a method that check if the player has the fund for its bet. Yes : True No : False
        
        if self.bank - bet_player < 0 :
            return False
        else :
            return True

    def place_bet(self, bet_player) -> int:
        self.bet = int(bet_player)
        return f'You placed a bet of {self.bet}'

    # In TESTfile : From here Class TestValue
    def choose_ace_value (self, ace_card) -> int:
            while True:
                try :
                    ace_value = int(input("What value do you want your ace to have ? (1 or 11)"))

                    if type(ace_value) != int :
                        raise InvalidTypeError('Invalid type. Your input must be an integer')
                    elif ace_value not in [1,11] :
                        raise InvalidValueError ("Invalid 'value'. It must be '1' or '11'.")
                    
                    break

                except InvalidTypeError as ite :
                    print(f'Error : {ite}')
                except InvalidValueError as ive :
                    print (f'Error : {ive}')
                except Exception as e:
                    print(f'An unexpected error occurred: {e}')
            return ace_value

    def add_value(self, card) -> None:
        #method that use the attribute value from the card the value of a card to the value_count of the player
        if card.rank != "Ace" :
            self.value_count += card.value
        else :
            ace_value = self.choose_ace_value(card)
            if ace_value == 1:
                self.value_count += card.value[0]
            else :
                self.value_count += card.value[1]


    def total_value(self) ->int:
        print(f'The total value of your cards is {self.value_count}.')
        return self.value_count


    def clear_value(self) -> bool:
        self.value_count == 0
        print('Your hand value has been reset to 0.')
        return True
    
    
    
    ''' NOTES : Functions for the Choice best ace combinaison --------------------------------------------------------------------------------------------------------------------------------------------------
    functions :
        > ace_amount() = return the number of aces in the player hand
        > aces_value_combinaisons() = create and return a dictionnary with all the combinaison possible for the aces (takes number of aces as arguments)                    
        > aces_possibilities() = create and return a dictionnary with all the possibilities based on the aces value combinaison (takes dico of value combinaison as argument)
        > best_possibilitiy() = return the key:value pair with the number of the key value pair with the best possibility (takes dico of possibility as argument)
        > best_value_combinaison() = return the list of aces value from the best possibility (takes n° of the best possibility as argument)
        > return_value_best_possibilitycombinaison = return the value of the best possibilities (total value of the cards
        > sum_up function to execute all the functions before
    '''
    
    def ace_amount(self):
        ace_amount = 0
        for card in self.player.all_card:
            if card.rank == "Ace":
                ace_amount += 1
            else:
                pass
        return ace_amount
    
    def aces_value_combinaisons(self,ace_amount=0):
        #Create and return a dictionnary with all the combinaison possible for the aces 
        #Argument : number of aces as argument
        #Dictionnary looks like : {AVC1:[0,1,0];AVC2:[0,1,1];...} in which AVC1 : [index_value_1st_ace, index_value_2nd_ace, ...]

        ace_value_combinaisons = {}

        #Creation of the keys dictionary of ace value combinaisons
        for i in range(2**ace_amount):
            ace_value_combinaisons[f"AVC{i}"]= []

        #Adding value for each key
        for i in range(ace_amount):
        # 1 iteration by Ace in the player hand
            for i in range(2**ace_amount):
                # Decide ace index value 0 or 1 based on even/uneven --> Reminder : For Aces, card.value[index0]=1 or card.value[index1]=11)
                if i/2 !=0:
                    ace_value_combinaisons[f"AVC{i}"].append(0)
                if i/2 == 0 :
                    ace_value_combinaisons[f"AVC{i}"].append(1)
        return ace_value_combinaisons
    
    def aces_possibilities(self,ace_value_combinaisons=dict,ace_amount=0):
        #Create and return a dictionnary with all the possibilities based on the aces value combinaison
        #Format : dico possibilities = {P1:sum_values;P2:sum_values;...}
        #Argument = dico with all value combinaisons based on number of aces

        #Creation of Dict with the possibilities for the hand player value 
        hand_value_possibilities = {}

        #Creation of the keys of dictionary
        for i in range(2**ace_amount):
            hand_value_possibilities[f"P{i}"]= []

            #Add card value to possibility (if ace, use the ace_value_combinaison dico)
            for card in self.all_cards:
                possibility_ace_count=0
                if card.rank != "Ace":
                    hand_value_possibilities[f"P{i}"] +=card.value
                else:
                    hand_value_possibilities[f"P{i}"] += card.value[ace_value_combinaisons[f"ACV{i}"][possibility_ace_count]]
                    possibility_ace_count+=1

        return hand_value_possibilities
    

    def best_possibility(self, player_value_count, ace_amount=0, hand_value_possibilities=dict):
        #return the key:value pair with the number of the key value pair with the best possibility (takes dico of possibility as argument)

        #Iterate through dico possibilities, and see best value
        best_possibility = 0
        smallest_possibility = 21
        burst_possibility = ""
        dealer_wins = False

        while dealer_wins == False:

            for i in range(2**ace_amount):
                check_21 = hand_value_possibilities[f"P{i}"] <=21
                check_better_player = hand_value_possibilities[f"P{i}"] > player_value_count

                # Check <= 21 & Better player
                if check_21 and check_better_player:
                    best_possibility = hand_value_possibilities[f"P{i}"]
                    num_best_key = i
                    dealer_wins = True

                # Check <= 21 & Lower player
                elif check_21 and not check_better_player :
                    if hand_value_possibilities[f"P{i}"] < smallest_possibility:
                        smallest_possibility = hand_value_possibilities[f"P{i}"]
                    else:
                        continue
                
                # Check Burst & Better player
                elif not check_21 :
                    burst_possibility = "Burst"
                else:
                    continue
            
            break

        if dealer_wins == True:
            dealer_wins_tupple = (True, best_possibility)
            return dealer_wins_tupple
        
        #Does not beat player, but does not burst 
        elif smallest_possibility != 21:
            dealer_replay = (False, smallest_possibility)
            return dealer_replay
        
        #Only option above 21, dealer will "Burst"
        else:
            return burst_possibility


    def best_combinaison(self,ace_value_combinaisons = dict, num_best_key=int):
        #return the list of aces value from the best possibility 
        #Argument : n° of the best key possibility as argument
        return ace_value_combinaisons[f"ACV{num_best_key}"]
    
    def decide_dealer_action(self):
        #Function that executes all the other "Best possibility" functions
        #returns the best_option_tupple (best_possibility, num_best_key)
        hand_value_possibilities = self.aces_possibilities(self.aces_value_combinaisons(self.ace_amount()),self.ace_amount())
        return self.best_possibility(self.value_count,self.ace_amount(),hand_value_possibilities)




class InvalidTypeError(Exception):
#Inheritance: It inherits from the built-in Exception class.
    pass

class InvalidValueError(Exception):
    #Inheritance: It inherits from the built-in Exception class.
    pass



''' NOTES to SELF
- return instead of print() - to change in future
    some method uses return but should use print() instead. this was made for the sake of the tests. 
    However it is possible to test printing statement, which make this practice not the best.
'''

''' NOTES ABOUT BEST POSSIBILITY FUNCTIONS
# Count number of Aces in hand player


# Simulate the value combinaisons (1 or 11) of the aces in the player hand (from 0 aces to 4)
    > possibilities are stored into a dictionnary of lists = ace_value_combinaisons
    > possibilities are named from AVC1 == Aces Value Combinaisons 1 to AVC16
    > dictionnary looks like : {AVC1:[0,1,0];AVC2:[0,1,1];...} in which AVC1 : [index_value_1st_ace, index_value_2nd_ace, ...]

    for i in 2**ace_amount:
        > create the key and empty list value
        > stored them in the dico
        > MAYBE no NEED : create the variables --> store directly as x:[],y:[], ... 
    
        for i in ace_amount
            # Fill the values of each key of the dictionary, based on the number of Aces --> 2 Aces means a list of 2 values P1: [0,1], 3 Aces 3 values, ...

            for i in dico:
            # each possibility has 2 variants (Ace value is 1, at card.value[index0] or 11 at card.value[index11])
            
                if i Uneven :
                    dico.append 0 in AV{i} key
                if i Even :
                    dico.append 0 in AV{i} key

# Simulate the possibilities based on aces value
    > Create possibilities variables --> as a dico possibilities = {P1:x;P2:x;..)}
        for i in range(0;2**ace_amount-1):
            possibilities[i]=f"P{i}"

    > Iterate through cards by adding their value to each possibility
    for i in range(2**ace_amount):
        for card in self.player.all_cards:
            if card.rank != "Ace":
                possibilities[f"P{i}"] +=card.value
            else:
                possibilities[f"P{i}"] += ace_values[f"AV{i}"[ace_n°, which ace is it, 1st, 2nd, ...]]

        > Iterate through dico possibilities, and see best value
        best_possibility = 0
        best_key = P{possibility}
        for possibility in dico_possibilities:
            if possibility <=21:
                if possibility > player_value_count:
                    if possibility > best_possibility:
                        best_possibility = possibility

                    else:
                        pass
                else:
                    pass
            else:
                pass
    
return possibilities[key:best_possibility] // aces_values[key:best_aces_values]

'''
