#####################################################################################
# Description: The Base Deck                                                        #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.2 30.08.2020                                                           #
#####################################################################################

from Card import Card
import random


class Deck(object):
    # ------------------------------------------------------------------- Builder ----------------------------------------------------------------

    def __init__(self):
        """ list - cards = The List of all cards stored in this deck"""
        self.cards = []
        # Create Cards and shuffle the Deck
        self.build()
        self.shuffle()

    # ------------------------------------------------------------------- Setup ----------------------------------------------------------------

    def build(self):
        """initialise Cards"""
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))

    # ------------------------------------------------------------------- Misc -------------------------------------------------------------------

    def shuffle(self):
        """shuffles the cards"""
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        """returns a card and pops it from the Deck"""
        return self.cards.pop()

    def show(self):
        """prints all cards in Deck"""
        for card in self.cards:
            print(card.show())
