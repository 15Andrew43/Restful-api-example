from flask import Blueprint, render_template, request, flash #, redirect, url_for
from .models import User
from . import db





next_id = 0

views = Blueprint('views', __name__)

@views.route('/users', methods=['POST'])
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

	user = User(id=next_id, nickname=nickname, email=email, rating=rating)
	db.session.add(user)
	db.session.commit()


	return "" # redirect(url_for('views.users')) # render_template("users.html", users=users) # 
	


@views.route('/users/<id>', methods=['PUT'])
def edit_user(id):
	print("\n\n\n")
	print("===================PUT========================")
	print(request.json)
	print("\n\n\n")

	# id=request.get_json()['id']
	nickname = request.get_json()['nickname']
	email = request.get_json()['email']
	rating = request.get_json()['rating']

	User.query.filter_by(id=id).update({
		'id': id,
		'nickname': nickname,
		'email': email,
		'rating': rating
	})
	db.session.commit()

	return ""


@views.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
	print("\n\n\n")
	# print(request.json)
	print("===================DELETE========================")
	print("\n\n\n")


	User.query.filter_by(id=id).delete()
	db.session.commit()

	return "" 


@views.route('/')
def home():
	return render_template("base.html")

@views.route('/users', methods=['GET'])
def users():
	print("\n\n\n")
	print("================GET===============")
	print("\n\n\n")


	users = db.session.query(User).all()
	print("________________________________________________________________________________")
	print(users)
	print("________________________________________________________________________________")

	return render_template("users.html", users=users)



@views.route('/error')
def error():
	return "error", 500


