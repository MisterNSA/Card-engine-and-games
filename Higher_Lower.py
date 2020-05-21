from CardClasses import Card, Deck


class HigherLowerGame(object):
    def __init__(self):
        self.win = False
        self.loose = False
        deck = Deck()
        player = input("Please enter your name: ")
        self.play(deck, player)

    # returns the players guess, if the next card is higher or lower
    def getGuess(self):
        valid_input = False
        while valid_input == False:
            print("Is the next card higher or lower? higher = h lower = l")
            guess = input("your guess: ")
            guess = guess.lower()
            if guess in ["h", "higher", "l", "lower"]:
                valid_input = True
            else:
                print(
                    "That wasnt a valid input. Please enter h for higher or l for lower!")
        return guess

    def play(self, Deck, player):
        currentCard = Deck.drawCard()
        print("The card is: {}".format(Card.show(currentCard)))
        # solange noch Karten im Deck sind, hat der Spieler nicht gewonnen
        # !!!Später Schwierigkeitsgrade mit unterschiedlicher Kartenanzehl
        while self.win != True and self.loose != True:
            guess = self.getGuess()
            # save the last card and get a new card
            lastCard = currentCard
            currentCard = Deck.drawCard()
            if guess.lower() == "h":
                if lastCard.value >= currentCard.value:
                    self.loose = True

            elif guess.lower() == "l":
                if lastCard.value <= currentCard.value:
                    self.loose = True

            if len(Deck.cards) == 0:
                self.win = True

            print("The card is: " + Card.show(currentCard))

        if self.win == True:
            print("Congratulations {}! You won!".format(player.name))
        else:
            print("You loose")


Game = HigherLowerGame()
