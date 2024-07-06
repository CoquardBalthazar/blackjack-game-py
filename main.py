from src.card import Card
from src.deck import Deck
from src.player import Player
from src.bank import Bank
from src.table import Table
from src.functions import *

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
turn_on = True

def main():
  table = Table()
  turn_on = table.turn_on

  while True:
      # Print opening game with rules
      table.rules()

      # Setup the game
      table.players_setup()
      table.game_setup()

      table.game_on = True

      while table.game_on :
        table.player_bet()
        # Player's turn
        table.turn_player()

        # Dealer's turn (until 18) with result round
        table.turn_dealer()

        # Ask to play again
        if table.player_bank.bank >0:
          
          new_game = other_hand_input()
        
          if new_game[0].lower()=='y':
              table.game_on=True

              # Reset the Deck and the Dealer's and Player's hands
              table.game_reset()
              table.game_setup()
  
              continue
          else:
              print("Thanks for playing!")
              table.game_on=False
        else:
          print(f"Player {table.player_hand.name} busts!")
          print("Thanks for playing!")
          table.game_on=False
      break
    
if __name__ == "__main__":
  main()
  print("End of main file")