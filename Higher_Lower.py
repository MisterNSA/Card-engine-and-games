#####################################################################################
# Description: A game where you have to guess, if the next Card is higher is lower  #
# This game is build upon my CardClasses Library for Card games                     #
# Creator: Tobias Dominik Weber aka MisterNSA                                       #
# Version: 0.6 25.08.2020                                                           #
# Planned Features: GUI with custom pixelart Cards, Highscore List                  #     
#####################################################################################


from Card import Card
from Deck import Deck

class HigherLowerGame(object):
    # ---------------------------------------------------------------------- Setup -----------------------------------------------------------------

    def __init__(self):
        """
        Lets the player play the game

        Bool - win = Has the Player won yet?
        Bool - loose = Has the Player lost yet?
        """
        self.win = False
        self.loose = False
        # create Deck
        deck = Deck()
        player = input("Please enter your name: ")
        # Check which difficulty the Player wants
        Valid_input = False
        while Valid_input == False:
            difficulty = input("""What difficulty do you want to play with?
    Easy(e): Win with 48 cards left = guess 4 Cards
    Medium(m): Win with 46 cards left = guess 6 Cards
    Hard(h): Win with 40 cards left = guess 12 Cards
    impossible(i): Win with 30 cards left = guess 22 Cards
    ZeroValueError(z): Win with 0 cards left =  guess 52 cards ... why is this even here?\n""") 
            if difficulty in ["e", "E", "easy", "Easy"]:
                Cards_left_to_win = 48
                Valid_input = True
            if difficulty in ["m", "M", "medium", "Medium"]:
                Cards_left_to_win = 46
                Valid_input = True
            if difficulty in ["h", "H", "hard", "Hard"]:
                Cards_left_to_win = 40
                Valid_input = True
            if difficulty in ["i", "I", "impossible", "Impossible"]:
                Cards_left_to_win = 30
                Valid_input = True
            if difficulty in ["z", "Z"]:
                print("... really?")
                Cards_left_to_win = 0
                Valid_input = True
        # main game
        self.play(deck, player, Cards_left_to_win)

    # ---------------------------------------------------------------------- Main Game -------------------------------------------------------------

    def play(self, Deck, player, Cards_left_to_win):
        """
        Main Method to start the actual game

        arguments: 
        Deck - Instance of Deck-Class which stores all Cards
        player - Stores player name
        Cards_left_to_win - With how many cards left in the deck the player wins
        """
        currentCard = Deck.drawCard()
        print("The card is: " + Card.show(currentCard))

        while self.win != True and self.loose != True:
            guess = self.getGuess()
            # save the last card and get a new card
            lastCard = currentCard
            currentCard = Deck.drawCard()

            if guess.lower() in ["h", "higher"]:
                if lastCard.value >= currentCard.value:
                    self.loose = True
            elif guess.lower() in ["l", "lower"]:
                if lastCard.value <= currentCard.value:
                    self.loose = True

            if len(Deck.cards) == Cards_left_to_win:
                self.win = True

            print("The card is: " + Card.show(currentCard))

        if self.win == True:
            print("Congratulations {}! You won!".format(player))
        else:
            print("You loose")

    # ---------------------------------------------------------------------- Functionality ---------------------------------------------------------
    
    def getGuess(self):
        """returns the players guess, if the next card is higher or lower"""
        valid_input = False

        while valid_input == False:
            print("Is the next card higher or lower? higher = h lower = l")
            guess = input("your guess: ")
            guess = guess.lower()
            
            if guess in ["h", "H", "higher", "l", "L","lower"]:
                valid_input = True
            else:
                print(
                    "That wasnt a valid input. Please enter h for higher or l for lower!")
        return guess


Game = HigherLowerGame()
