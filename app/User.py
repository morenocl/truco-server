import app.data
import os
from flask import jsonify


def get_users():
    return jsonify({ "users": data.USERS })


def create_user(json):
    username = json.get('username')
    password = json.get('password')
    exist = [user for user in data.USERS if user["username"] == username]
    if not exist:
        data.USERS.append({ "username": username, "password": password , "win": False, "turn": False })
        msj = jsonify({ "status": "ok" })
    else:
        msj = jsonify({ "status": "error", "message": "El usuario ya esta en uso." })
    return msj


def delete_users(json):
    username = json.get('username')
    password = json.get('password')
    exist = [user for user in data.USERS if user["username"] == username and user["password"] == password]
    if not exist:
        msj = jsonify({ "status": "error", "message": "Usuario o contraseña invalido." })
    else:
        data.USERS.remove(exist[0])
        msj = jsonify({ "status": "ok" })
    return msj


def login_user(json):
    return jsonify({ "status": "ok" })
