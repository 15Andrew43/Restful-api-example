from flask import Blueprint, render_template, request, flash  # , redirect, url_for
from .models import User
from . import db
from functools import wraps
import json
import requests

import socket
socketName = socket.gethostbyname(socket.gethostname())


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open("log.txt", "a+") as log_file:
            log_file.write(
                "================================LOGGER============================\n")
            log_file.write(str(request.__dict__))
            log_file.write('\n')
        return func(*args, **kwargs)
    return wrapper


next_id = 1

views = Blueprint('views', __name__)


@views.route('/users', methods=['POST'])
@logger
def add_user():
    global next_id
    if request.method == 'POST':

        nickname = request.get_json()['nickname']
        email = request.get_json()['email']
        rating = request.get_json()['rating']
        print("\n\n\n")
        print(nickname)
        print(email)
        print(rating)
        print("==================POST================")
        print("\n\n\n")

    next_id += 1

    if not nickname:
        nickname = 'default name'
    if not email:
        email = 'default@gmail.com'
    if not rating:
        rating = 100500
    user = User(id=next_id, nickname=nickname, email=email, rating=rating)
    db.session.add(user)
    db.session.commit()

    # redirect(url_for('views.users')) # render_template("users.html", users=users) #
    return ""


@views.route('/users/<id>', methods=['PUT'])
@logger
def edit_user(id):
    print("\n\n\n")
    print("===================PUT========================")
    print(request.json)
    print("\n\n\n")

    # id=request.get_json()['id']
    nickname = request.get_json()['nickname']
    email = request.get_json()['email']
    rating = request.get_json()['rating']

    if not nickname:
        nickname = 'default name'
    if not email:
        email = 'default@gmail.com'
    if not rating:
        rating = 100500

    User.query.filter_by(id=id).update({
        'id': id,
        'nickname': nickname,
        'email': email,
        'rating': rating
    })
    db.session.commit()

    return ""


@views.route('/users/<id>', methods=['DELETE'])
@logger
def delete_user(id):
    print("\n\n\n")
    # print(request.json)
    print("===================DELETE========================")
    print("\n\n\n")

    User.query.filter_by(id=id).delete()
    db.session.commit()

    return ""


@views.route('/')
@logger
def home():
    return render_template("base.html", socketName=socketName,  realIp=requests.get("https://ifconfig.me").text)


@views.route('/users', methods=['GET'])
@logger
def users():
    print("\n\n\n")
    print("================GET===============")
    print("\n\n\n")

    users = db.session.query(User).all()
    print("________________________________________________________________________________")
    print(users)
    print("________________________________________________________________________________")

    return render_template("users.html", users=users, socketName=socketName, realIp=requests.get("https://ifconfig.me").text)


@views.route('/error')
@logger
def error():
    return "error", 500


@views.route('/api/users', methods=['GET'])
@logger
def api_users():
    if request.method == 'GET':
        print("\n\n\n")
        print("================GET USERS===============")
        print("\n\n\n")

        users = db.session.query(User).all()
        print("________________________________________________________________________________")
        print(users)
        print("________________________________________________________________________________")

        return json.dumps(list(map(lambda user: user.to_json(), users)))
