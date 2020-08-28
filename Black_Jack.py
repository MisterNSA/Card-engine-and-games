#####################################################################################
# Description: The Goal is to get as close to 21 as Possible, without going higher  #
# This game is build upon my CardClasses Library for Card games                     #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.0 24.07.2020                                                           #
# Planned Features: GUI with custom pixelart Cards,                                 #
#####################################################################################

from CardClasses import *
from operator import attrgetter


class Bj_Player(Player):
    def __init__(self):
        # string - name = name of the Player
        # list - hand = All Cards the Player has
        # bool - draw_again = Save when player doesnt wants to draw again
        self.name = input("Please enter your name: ")
        self.hand = []
        self.draw_again = True
        self.hand_value = 0


class Blackjack():
    """ This Class represents the Game of Blackjack"""
    # ---------------------------------------------------------------------- Setup -----------------------------------------------------------------

    def __init__(self):
        # list - players = Stores the Names of the Players
        self.set_players()
        self.deck = Deck()

        self.play()

    
    def set_players(self):
        """Ask how many Players are playing and creates them"""
        self.players = []

        valid = False
        while valid = False:
            try:
                player_number = int(input("How many Players are Playing? "))
                valid = True
            except:
                print("Das war keine valide Eingabe. Bitte gib eine Zahl ein.")
        # create the given Number of Players
        for _ in range(0, player_number):
            self.players.append(Bj_Player())

    # ---------------------------------------------------------------------- Main Game -------------------------------------------------------------

    def play(self):
        """
        The method to play the game
        Lets the Players draw cards as long as they want.
        If no one wants to draw again, the method evaluates who has lost because of a Handvalue over 21
        Then it evaluates which Player has the Highest Score and returns the Winner, or a draw if more than one Person has the best Score 
        """
        # bool - game_nunning = Flag to evaluate if the game is still running, or if the winner should be evaluated
        game_running = True
        # int - Players_done = Used to see, if all players are done drawing cards
        Players_done = 0
    # ---------------------------------------------------------------------- Game Loop -------------------------------------------------------------
    
        # Ask Players if they want to draw again, until no one wants to draw again
        while game_running:
            while Players_done < len(self.players):
                for Bj_Player in self.players:
                    if Bj_Player.draw_again:
                        wants_to_draw = input(
                            f"{Bj_Player.name}, do you want to draw another Card? ")
                        if wants_to_draw.lower() in ["y", "yes", "j", "ja"]:
                            Bj_Player.draw(self.deck)
                            Bj_Player.showHand()
                            Bj_Player.set_hand_value()
                        else:
                            Bj_Player.draw_again = False
                            Players_done += 1
            else:
                game_running = False

    # ---------------------------------------------------------------------- Evaluation ------------------------------------------------------------

        # List - could_win = For Players that could have won. So you can keep all Players for the next round,
        # but only need to check to check for Players with valid Score
        could_win = []
        for Bj_Player in self.players:
            if Bj_Player.hand_value <= 21:
                could_win.append(Bj_Player)

        # Check who won, or if the game was a draw
        # sort list by highest value of handcards
        if len(could_win) > 0:
            could_win.sort(key=attrgetter("hand_value"), reverse=True)
            ### I could print out between which players the draw occured, but for now im to lazy
            if len(could_win) > 1:
                if could_win[0].hand_value == could_win[1].hand_value:
                    print(f"Draw!")
            else:
                print(f"{could_win[0].name} has Won!")
        else:
            print("Draw, neither of you got under the Score of 22!")


game = Blackjack()

# To Do
# Fix Card Values
# Add a exception if all cards were drawn from the deck
