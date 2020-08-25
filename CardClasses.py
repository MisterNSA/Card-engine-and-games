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

    # ------------------------------------------------------------------- Setter -----------------------------------------------------------------

    # Builds name by value adn suit: 2 to 10, Jack, Queen, King, Ace
    def set_name(self):
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

    # ------------------------------------------------------------------- Getter ----------------------------------------------------------------- 

    # returns the name of card
    def show(self):
        return self.name



class Deck(object):
    # ------------------------------------------------------------------- Builder ----------------------------------------------------------------

    def __init__(self):
        # list - cards = The List of all cards stored in this deck
        self.cards = []
        # Create Cards and shuffle the Deck
        self.build()
        self.shuffle()

    # ------------------------------------------------------------------- Setter -----------------------------------------------------------------

    # initialise Cards
    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))

    # shuffles the cards
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # ------------------------------------------------------------------- Getter -----------------------------------------------------------------

    # returns a card and pops it from the Deck
    def drawCard(self):
        return self.cards.pop()

    # prints all cards in Deck
    def show(self):
        for card in self.cards:
            print(card.show())



class Player(object):
    # ------------------------------------------------------------------- Builder ----------------------------------------------------------------

    def __init__(self):
        # string - name = name of the Player | Questionable, if needed
        # list - hand = All Cards the Player has
        self.name = input("Please enter your name: ")
        self.hand = []

    # ------------------------------------------------------------------- Setter -----------------------------------------------------------------

    # adds a card from the deck to the players hand
    def draw(self, Deck):
        self.hand.append(Deck.drawCard())
        return self

    # takes the position of a card and removes it from the hand
    def discard(self, placeInHand):
        return self.hand.pop(placeInHand - 1)

    # ------------------------------------------------------------------- Getter -----------------------------------------------------------------

    # prints the hand with the position of each card
    def showHand(self):
        count = 1
        for card in self.hand:
            print("Card {} = {}".format(count, card.show()))
            count += 1


