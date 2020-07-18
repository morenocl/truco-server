from flask import Flask, request
import User


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





if __name__ == "__main__":
    app.run(debug=True)
