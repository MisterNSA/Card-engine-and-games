#####################################################################################
# Description: This is ment to be a Base for all diffrent kinds of Card game        #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.1 24.07.2020                                                           #
#####################################################################################

import random


class Card(object):
    # string - suit = Spades, Clubs, Diamond or Hearts
    # string - value = 1 to 10, Jack, Queen, King, Ace
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Shows the Value in a easy to read way
    def show(self):
        return("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        # list - cards = The List of all cards stored in this deck
        self.cards = []
        # Create Cards and shuffle the Deck
        self.build()
        self.shuffle()

    # initialise Cards
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    # prints all cards in Deck
    def show(self):
        for c in self.cards:
            print(c.show())

    # shuffles the cards
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # returns a card and pops it from the Deck
    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        # string - name = name of the Player | Questionable, if needed
        # list - hand = All Cards the Player has
        self.name = name
        self.hand = []

    # adds a card from the deck to the players hand
    def draw(self, Deck):
        self.hand.append(Deck.drawCard())
        return self

    # prints the hand with the position of each card
    def showHand(self):
        count = 1
        for card in self.hand:
            print("Card {} = {}".format(count, card.show()))
            count += 1

    # takes the position of a card and removes it from the hand
    def discard(self, placeInHand):
        return self.hand.pop(placeInHand - 1)

