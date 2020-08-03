from flask import Flask, request
from app import User
from app import Game
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return 'Server work'


@app.route('/user', methods=['GET'])
def get_users():
    return User.get_users()


@app.route('/user', methods=['POST'])
def create_user():
    return User.create_user(request.json)


@app.route('/user/login', methods=['POST'])
def login_user():
    print('login')
    return User.login_user(request.json)


@app.route('/user', methods=['DELETE'])
def delete_users():
    return User.delete_users(request.json)


@app.route('/game', methods=['GET'])
def list_games():
    return Game.list_games()


@app.route('/game', methods=['POST'])
def create_game():
    return Game.create_game(request.json)


@app.route('/game/<int:id>', methods=['PATCH'])
def start_game(id):
    return Game.start_game(id)


@app.route('/game/<string:username>', methods=['GET'])
def get_game_started(username):
    return Game.get_game_started(username)


@app.route('/game/<int:id>/<string:username>', methods=['GET'])
def get_game_status(id, username):
    return Game.get_game_status(id, username)


@app.route('/game/<int:id>', methods=['PUT'])
def update_points(id):
    return Game.update_points(id, request.json)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=environ.get("PORT", 5000))
