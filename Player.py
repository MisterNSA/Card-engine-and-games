#####################################################################################
# Description: This is ment to be a Base for all diffrent kinds of Card game        #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.2 30.08.2020                                                           #
#####################################################################################

from Deck import Deck
from Card import Card


class Player(object):
    # ------------------------------------------------------------------- Builder ----------------------------------------------------------------

    def __init__(self):
        """
        Class to model the Player of a Card game
        
        string - name = name of the Player
        list - hand = All Cards the Player has
        int - hand_value = Total of all card values in hand
        """
        self.name = input("Please enter your name: ")
        self.hand = []
        self.hand_value = 0

    # ------------------------------------------------------------------- Misc -------------------------------------------------------------------

    def draw(self, Deck):
        """adds a card from the deck to the players hand"""
        self.hand.append(Deck.drawCard())
        return self

    def discard(self, placeInHand):
        """
        takes the position of a card and removes it from the hand
        
        arguments:
        placeInHand - Index of the Card in Hand
        """
        return self.hand.pop(placeInHand - 1)

    def set_hand_value(self):
        """sets self.hand_value to the total value of cards in hand | Sometimes, get_hand_score is enough, this is for casese it isnt"""
        self.hand_value = 0
        for Card in self.hand:
            self.hand_value += Card.value

    def showHand(self):
        """prints the hand with the position of each card"""
        count = 1
        for card in self.hand:
            print("Card {} = {}".format(count, card.show()))
            count += 1

    def get_hand_value(self):
        """returns the hand_value to the total of all card values in Hand"""
        hand_value = 0
        for card in self.hand:
            hand_value += card.value
        return hand_value

# To Do
# Add a exception if all cards were drawn from the deck
# Create a Stack for the cards, that are discarded
