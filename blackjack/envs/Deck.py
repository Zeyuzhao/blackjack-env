import random

class Deck():
    # Each card is a tuple: (rank, suit)
    standard = [(i, j) for i in range(13) for j in range(4)]

    def __init__(self, num_decks = 1):
        self.deck = Deck.standard.copy() * num_decks
        self._drawn = 0

    def shuffle(self):
        random.shuffle(self.deck)

    def drawCard(self):
        return self.deck.pop()

    def drawValue(self):
        return self.deck.pop()[0]

    def drawNCards(self, n):
        cards = []
        for i in range(n):
            cards.append(self.deck.pop())
        return cards




