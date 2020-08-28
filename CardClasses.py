#####################################################################################
# Description: This is ment to be a Base for all diffrent kinds of Card game        #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.2 25.08.2020                                                           #
#####################################################################################

import random


class Card(object):
    # ------------------------------------------------------------------- Builder ----------------------------------------------------------------

    # string - suit = Spades, Clubs, Diamond or Hearts
    # string - value = from 2 to 14
    # string - name = The full name of the cards - easier to read for Humans but useless for operations
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        self.set_name()

    # ------------------------------------------------------------------- Setup ------------------------------------------------------------------

    def set_name(self):
        """Builds name by value and suit: 2 to 10, Jack, Queen, King, Ace"""
        if self.value <= 10:
            self.name = (str(self.value) + " of " + self.suit)
        elif self.value == 11:
            self.name = ("Jack of " + self.suit)
        elif self.value == 12:
            self.name = ("Queen of " + self.suit)
        elif self.value == 13:
            self.name = ("King of " + self.suit)
        elif self.value == 14:
            self.name = ("Ace of " + self.suit)

    # ------------------------------------------------------------------- Misc -------------------------------------------------------------------

    def show(self):
        """returns the cards name"""
        return self.name


class Deck(object):
    # ------------------------------------------------------------------- Builder ----------------------------------------------------------------

    def __init__(self):
        # list - cards = The List of all cards stored in this deck
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


class Player(object):
    # ------------------------------------------------------------------- Builder ----------------------------------------------------------------

    def __init__(self):
        # string - name = name of the Player
        # list - hand = All Cards the Player has
        # int - hand_value = Total of all card values in hand
        self.name = input("Please enter your name: ")
        self.hand = []
        self.hand_value = 0

    # ------------------------------------------------------------------- Misc -------------------------------------------------------------------

    def draw(self, Deck):
        """adds a card from the deck to the players hand"""
        self.hand.append(Deck.drawCard())
        return self

    def discard(self, placeInHand):
        """takes the position of a card and removes it from the hand"""
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
# Split into multiple Files
# Add a exception if all cards were drawn from the deck
# Add discard function
# Create a Stack for the cards, that are discarded
