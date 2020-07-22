import app.data


def create_deck():
    for n in data.NUMBERS:
        for c in data.CARDS:
            deck.append((n, c))

    return random.shuffle(deck)


def deal():
    for player in data.GAME['players']:
        for i in range(3):
            data.GAME['players_info'][player].append(data.DECK.pop())
