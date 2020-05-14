"""
Write a Program DeckOfCards.java, to initialize deck of cards having suit ("Clubs",
"Diamonds", "Hearts", "Spades") & Rank ("2", "3", "4", "5", "6", "7", "8", "9", "10",
"Jack", "Queen", "King", "Ace"). Shuffle the cards using Random method and then
distribute 9 Cards to 4 Players and Print the Cards the received by the 4 Players
using 2D Array…
"""

import random


class Deck:
    def __init__(self):
        self.suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []

    def pack_of_cards(self):
        for suit in self.suit:
            for rank in self.rank:
                self.cards.append(rank + " of " + suit)
        return self.cards

    def shuffle_of_cards(self):
        shuffle_cards = random.sample(self.pack_of_cards(), 36)
        print(f"The cards distributed to 4 players are: {shuffle_cards}")
        shuffle_to_player1 = shuffle_cards[:9]
        shuffle_to_player2 = shuffle_cards[9:18]
        shuffle_to_player3 = shuffle_cards[18:27]
        shuffle_to_player4 = shuffle_cards[27:]

        print(f"Player 1 cards: {shuffle_to_player1}")
        print(f"Player 2 cards: {shuffle_to_player2}")
        print(f"Player 3 cards: {shuffle_to_player3}")
        print(f"Player 4 cards: {shuffle_to_player4}")


obj_of_deck = Deck()
obj_of_deck.shuffle_of_cards()
