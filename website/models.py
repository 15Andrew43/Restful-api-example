from . import db 


class User(db.Model):  # UserMixiт
	id = db.Column(db.Integer, primary_key=True) # , autoincrement=True
	nickname = db.Column(db.String(150))
	email = db.Column(db.String(150)) # , unique=True
	rating = db.Column(db.Integer)

	def __init__(self, id, nickname, email, rating):
		self.id = id
		self.nickname = nickname
		self.email = email
		self.rating = rating

	def __repr__(self):
		return f'<|> User {self.nickname} <|>'
