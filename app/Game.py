import data


def create_game(json):
    name = json.get("name")
    nosotros = json.get("nosotros")
    ellos = json.get("ellos")
    data.GAME.clear()
    data.GAME['name'] = name
    data.GAME['players'] = players
    data.GAME['turn'] = 0
    data.GAME['points'] = (0, 0)
    data.GAME['win'] = None
    data.GAME['players_info'] = {}
    for player in players:
        data.GAME['players_info'][player] = []
    return jsonify({"status": "ok"})


def get_game_status(player):
    # player : string
    game = data.GAME
    return jsonify({
        "name": game['name'],
        "players": game['players'],
        "players_info": game['players_info'][player],
        "turn": game['turn'],
        "points": game['points'],
        "win": game['win']
    })


def update_points(json):
    points = json.get('points')
    a, b = data.Game['points']
    data.Game['points'] = a + points[0], b + points[1]
