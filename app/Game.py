from app import data
from app.Deck import create_deck, deal
from flask import jsonify


def create_game(json):
    try:
        data.GAME.append({})
        id = len(data.GAME) - 1
        username = json.get("username")
        name = json.get("name")
        nosotros = json.get("nosotros")
        ellos = json.get("ellos")
        players = []
        for n, e in zip(nosotros, ellos):
            players.append(n)
            players.append(e)
        data.GAME[id]['id'] = id
        data.GAME[id]['owner'] = username
        data.GAME[id]['name'] = name
        data.GAME[id]['turn'] = 0
        data.GAME[id]['points'] = {"nos": 0, "ellos": 0}
        data.GAME[id]['win'] = None
        deal(id, players)
        msj = jsonify({"status": "ok", "id": id})
    except e:
        msj = jsonify({"status": "error", "message": e})
    return msj


def get_game_started(username):
    for game in data.GAME:
        exist = [player for player in game['players_info'] if player['player'] == username and not game['win']]
        print('Exist: ', exist)
        if exist:
            return jsonify({"status": "ok", "id": game['id']})
    return jsonify({"status": "error", "message": "No hay juego iniciado para este usuario."})


def get_game_status(id, username):
    game = data.GAME[id]
    return jsonify({
        "name": game['name'],
        "players_info": game['players_info'],
        "turn": game['turn'],
        "points": game['points'],
        "win": game['win']
    })


def update_points(id, json):
    points = json.get('points')
    nos = data.Game[id]['points']['nos']
    ellos = data.Game[id]['points']['ellos']
    data.Game['points']['nos'] = nos + points['nos']
    data.Game['points']['ellos'] = ellos + points['ellos']
