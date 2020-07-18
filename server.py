from flask import Flask, request
import User
import Game


app = Flask(__name__)


@app.route('/user', methods=['GET'])
def get_users():
    return User.get_users()


@app.route('/user', methods=['POST'])
def create_user():
    return User.create_user(request.json)


@app.route('/user', methods=['DELETE'])
def delete_users():
    return User.delete_users(request.json)


@app.route('/game', methods=['POST'])
def create_game():
    return Game.create_game(request.json)


@app.route('/game/<string: username>', methods=['GET'])
def get_game_status(username):
    return Game.get_game_status(username)


@app.route('/game', methods=['PUT'])
def update_points():
    return Game.update_points(request.json)


if __name__ == "__main__":
    app.run(debug=True)