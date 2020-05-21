import random


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Shows the Value in a easy to read way
    def show(self):
        return("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
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
            if guess == 'h' or 'l':
                valid_input = True
            else:
                valid_input = False
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
