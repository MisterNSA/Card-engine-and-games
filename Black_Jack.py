#####################################################################################
# Description: The Goal is to get as close to 21 as Possible, without going higher  #
# This game is build upon my CardClasses Library for Card games                     #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.2 04.09.2020                                                           #
# Planned Features: GUI with custom pixelart Cards, Online Multiplayer              #
#####################################################################################

from Player import Player
from Deck import Deck
from Card import Card
from operator import attrgetter


class Bj_Player(Player):
    def __init__(self):
        """
        Stores information about the Person/s Playing Blackjack.

        string - name = Name of the Player
        list - hand = All Cards the Player has
        bool - draw_again = Save when player doesnt wants to draw again
        int - hand_value = The total value of all cards in players hand
        """
        self.name = input("Please enter your name: ")
        self.hand = []
        self.draw_again = True
        self.hand_value = 0


class Blackjack():
    """
    This Class represents the Game of Blackjack.

    list - players = Stores all Players playing the game
    instance - deck = An instance of the Deck-Class. Used to store the cards used to play the game.
    """
    # ---------------------------------------------------------------------- Setup -----------------------------------------------------------------

    def __init__(self):
        self.show_rules()
        input("\nPress any Key to continue... \n")
        # list - players = Stores the Names of the Players
        self.set_players()
        self.deck = Deck()

        # Loop throug all Cards in Hand, check if they have symbol and change the Value, so that it matches the Blackjack rules
        for Card in self.deck.cards:
            if Card.symbol == "Jack":
                Card.set_value(10)
            if Card.symbol == "Queen":
                Card.set_value(10)
            if Card.symbol == "King":
                Card.set_value(10)
            if Card.symbol == "Ace":
                Card.set_value(11)

        # start the Main Game
        self.play()

    def set_players(self):
        """Ask how many Players are playing and create them"""
        self.players = []

        valid = False
        while valid == False:
            try:
                player_number = int(input("How many Players are Playing? "))
                valid = True
            except:
                print("Das war keine valide Eingabe. Bitte gib eine Zahl ein.")
        # create the given Number of Players
        for _ in range(0, player_number):
            self.players.append(Bj_Player())

    # ---------------------------------------------------------------------- Rules -----------------------------------------------------------------

    def show_rules(self):
        """Prints out the Games Rules"""
        print("""
This Version of Blackjack is a free for all Game. Either there is a won or it is a draw!

***** Goal *****
The Goal of the Game is to draw Cards in Order to get as close to a total card value of 21 as possible, but not over it.

***** Rules *****
All Players can draw as many cards as they want.
When no one wants to draw again, the Game evaluates the Winner.

***** Wins *****
There are 2 Special wins who count higher than any other Wins.
The second highest win is the BlackJack with an Ace and a King.
The highest win is the Triple Seven. As the name says, you need to have three sevens in your hand.
        """)

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

        # List - could_win = For Players that could have won. So you can keep all Players for the next round, but only need to check for Players with valid Score
        could_win = []

        for Bj_Player in self.players:
            if Bj_Player.hand_value > 21:
                # Check if Ace should have the Value of one or eleven | Always seek Players advantage
                for Card in Bj_Player.hand:
                    if Card.symbol == "Ace" and Bj_Player.hand_value > 21:
                        Card.set_value(1)
                        Bj_Player.set_hand_value()

            # Check if Player can win
            if Bj_Player.hand_value <= 21:
                sevens = 0
                Ace = False
                King = False
                # 3 times 7
                Drilling = []
                # King and Ace
                BlackJack = []
                # Check if a special Win occured
                for Card in Bj_Player.hand:
                    if Card.symbol == "Ace":
                        Ace = True
                    elif Card.symbol == "King":
                        King = True
                    elif Card.value == 7:
                        sevens += 1
                if King and Ace:
                    BlackJack.append(Bj_Player)
                elif sevens == 3:
                    Drilling.append(Bj_Player)

                # add to List of Players that could have won
                could_win.append(Bj_Player)

        # Check who won, or if the game was a draw
        if len(could_win) > 0:
            # Check for special Wins
            if len(Drilling) > 0:
                print(f"{Drilling[0].name} has Won with Triple seven!")
            if len(BlackJack) > 0:
                if len(BlackJack) > 1:
                    print(f"Draw!")
                else:
                    print(f"{BlackJack[0].name} has Won with a BlackJack!")

            # Check for hand value nearest to 21
            could_win.sort(key=attrgetter("hand_value"), reverse=True)
            if len(could_win) > 1 and could_win[0].hand_value == could_win[1].hand_value:
                print(f"Draw!")
            else:
                print(f"{could_win[0].name} has Won!")
        else:
            print("Draw, neither of you got under the Score of 22!")


game = Blackjack()
