import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':[1,11]}


playing = True


''' 
# GAME Set Up
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


    # TURN > WHILE LOOP
    turn = 0 / 1

    turn = 0 :
        - Announce dealer card > return / print cards
        - announce player cards. > return / print cards
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

    turn = 1: WHILE round_winner = False
        hit() until win score p0 or loses
        - win p0 : 
            > turn , 
            > announce dealer winner, 
            > p0 pay the bet = remove the bet from the bank
            > ask to play next round ?
                >no : game_on = False, end_game
                >yes : round loop start again

        - burst :
            > gameon False, 
            > announce player winner round, 
            > p0 get the bet, 
            > ask to continue play ?
                >no : game_on = False, end_game
                >yes : round loop start again


end_game
- player has not money in bank:
    > you dont have enough money to continue play
    > stop or bring more money in your bank ?
- player stoped game before:
    > you have xxx in your bank. 
    > if + than initial_bank : Felicitation you won xxx, which is (difference between init and now) than your initial bank value
    > if - than initial_bank : You finish with xxx. Today was not your lucky day, it is xxx less than your initial bak input.
'''