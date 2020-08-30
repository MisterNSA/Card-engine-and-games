#####################################################################################
# Description: The Base of all Cards                                                #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.2 30.08.2020                                                           #
#####################################################################################


class Card(object):
    # ------------------------------------------------------------------- Builder ----------------------------------------------------------------

    # string - suit = Spades, Clubs, Diamond or Hearts
    # string - value = from 2 to 14
    # string - symbol = Holds special symbol from Jack to Ace, else None
    # string - name = The full name of the cards - easier to read for Humans but useless for operations
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        self.symbol = None
        self.set_name()

    # ------------------------------------------------------------------- Setup ------------------------------------------------------------------

    def set_name(self):
        """Builds name by value and suit: 2 to 10, Jack, Queen, King, Ace"""
        if self.value <= 10:
            self.name = (str(self.value) + " of " + self.suit)
        elif self.value == 11:
            self.name = ("Jack of " + self.suit)
            self.symbol = "Jack"
        elif self.value == 12:
            self.name = ("Queen of " + self.suit)
            self.symbol = "Queen"
        elif self.value == 13:
            self.name = ("King of " + self.suit)
            self.symbol = "King"
        elif self.value == 14:
            self.name = ("Ace of " + self.suit)
            self.symbol = "Ace"

    # ------------------------------------------------------------------- Misc -------------------------------------------------------------------

    def show(self):
        """returns the cards name"""
        return self.name

    def set_value(self, value):
        """Changes the Cards Value. Needed to game specific values"""
        self.value = value
