from app import data
import os
from flask import jsonify


def get_users():
    users = [user['username'] for user in data.USERS]
    print(users)
    return jsonify({ "users": users })


def create_user(json):
    username = json.get('username')
    password = json.get('password')
    exist = [user for user in data.USERS if user["username"] == username]
    print('Exist: ', exist)
    if not exist:
        data.USERS.append({ "username": username, "password": password, "token": username + username[::-1]})
        print(data.USERS)
        msj = jsonify({ "status": "ok" })
    else:
        print('Send mensaje de error')
        msj = jsonify({ "status": "error", "message": "El usuario ya esta en uso." })
    print(msj)
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
    username = json.get('username')
    password = json.get('password')
    exist = [user for user in data.USERS if user["username"] == username and user["password"] == password]
    print('A continuacion el contenido de exist')
    print(exist[0])
    if exist:
        token = exist[0]['token']
        msj = jsonify({ "status": "ok", "token": token })
    else:
        msj = jsonify({ "status": "error", "message": "Usuario o contraseña invalido." })
    return msj
