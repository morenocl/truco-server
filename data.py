import random
import json


CARDS = [ "copa", "oro", "basto", "espada" ]
NUMBERS = [ 1, 2, 3, 4, 5, 6, 7, 10, 11, 12 ]
USERS = []

def create_deck():
    deck = []
    for n in NUMBERS:
        for c in CARDS:
            deck.append((n, c))

    return random.shuffle(deck)
