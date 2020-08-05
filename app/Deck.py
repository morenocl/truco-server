from app import data
import random


def create_deck():
    deck = []
    for n in data.NUMBERS:
        for c in data.CARDS:
            deck.append((n, c))

    random.shuffle(deck)
    return deck


def deal(id):
    players = data.GAME[id]['players']
    data.GAME[id]['players_info'] = [{"player": p, "cards":[], "playedCards": [], "actions": []} for p in players]
    deck = create_deck()
    for player in data.GAME[id]['players_info']:
        for i in range(3):
            player['cards'].append(deck.pop())
