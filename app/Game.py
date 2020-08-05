from app import data
from app.Deck import create_deck, deal
from flask import jsonify


def list_games():
    games = data.GAME
    list = [{"id": game['id'], "name": game['name'], "owner": game['owner']} for game in games]
    return jsonify({"status": "ok", "games": list})


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
        data.GAME[id]['started'] = False
        data.GAME[id]['players'] = players
        data.GAME[id]['players_info'] = []
        msj = jsonify({"status": "ok", "id": id})
        print('Create game ok: ', id)
    except e:
        msj = jsonify({"status": "error", "message": e})
        print('Create game error: ', e)
    return msj


# auxiliar.
def create_actions(id):
    game = data.GAME[id]
    for player in game['players_info']:
        player['actions'].append({"type": 'end_turn'})
        player['actions'].append({"type": 'envido'})
        player['actions'].append({"type": 'truco'})


def start_game(id):
    try:
        data.GAME[id]['started'] = True
        deal(id)
        create_actions(id)
        msj = jsonify({"status": "ok"})
    except e:
        msj = jsonify({"status": "error", "message": e})
    return msj


def get_game_started(username):
    # retorna id del primer juego empezado y que no termino, tal que contiene al jugador.
    for game in data.GAME:
        exist = [player for player in game['players_info'] if player['player'] == username and game['started'] and not game['win']]
        print('Exist: ', exist)
        if exist:
            return jsonify({"status": "ok", "id": game['id']})
    return jsonify({"status": "error", "message": "No hay juego iniciado para este usuario."})


# auxiliar.
def is_equal(str1, str2):
    flag = len(str1) == len(str2)
    for (a,b) in zip(str1, str2):
        if a != b:
            flag = False
    return flag


def get_game_status(id, username):
    try:
        game = data.GAME[id]
        pInfo = [ player.copy() for player in data.GAME[id]['players_info'] ]
        for player in pInfo:
            if not is_equal(player['player'], username):
                player['cards'] = list(map(lambda c: ('x', 'x'), player['cards']))

        game = {
            "name": game['name'],
            "players_info": pInfo,
            "turn": game['turn'],
            "points": game['points'],
            "win": game['win']
        }
        msj = jsonify({"status": "ok", "game": game})
    except e:
        msj = jsonify({"status": "error", "message": e})
    return msj


def update_points(id, json):
    points = json.get('points')
    nos = data.Game[id]['points']['nos']
    ellos = data.Game[id]['points']['ellos']
    data.Game['points']['nos'] = nos + points['nos']
    data.Game['points']['ellos'] = ellos + points['ellos']
