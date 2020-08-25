#####################################################################################
# Description: The Goal is to get as close to 21 as Possible, without going higher  #
# This game is build upon my CardClasses Library for Card games                     #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.0 24.07.2020                                                           #
# Planned Features: GUI with custom pixelart Cards,                                 #     
#####################################################################################

from CardClasses import *

class Blackjack():
    # ---------------------------------------------------------------------- Setup -----------------------------------------------------------------

    def __init__(self):
        # list - players = Stores the Names of the Players
        self.set_players()
        self.deck = Deck()

        self.play()

    # ---------------------------------------------------------------------- Setter ----------------------------------------------------------------
    
    # Creates the players
    def set_players(self):
        self.players = []
        for player in range(0, int(input("How many Players are Playing? "))):
            self.players.append(Player())

    # ---------------------------------------------------------------------- Main Game -------------------------------------------------------------

    def play(self):
        game_running = True
        while game_running:
            for Player in self.players:
                wants_to_draw = input(f"{Player.name}, do you want to draw another Card? ")
                if wants_to_draw.lower() in ["y", "yes", "j", "ja"]:
                    Player.draw(self.deck)
                    Player.showHand()


        # Spieler zieht eine Karte
        # Nächster Spieler ist dran, Loop wiederholen

        # Wenn alle 3 Spieler nicht mehr ziehen wollen, wird ausgewertet
        # Kartenwerte addieren und prüfen, ob sie >= 21 sind
        # Verbleibende Spieler miteinander vergleichen und größte zahl auswählen
        # Spieler mit dieser Höchsten Zahl gewinnt





game = Blackjack()

# Later add Lives, so that the game can be played as a best out of x