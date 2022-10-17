from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "users.db"

def create_app():
    
	app = Flask(__name__)
	app.config['SECRET_KEY'] = "ucwewvelhvghs nldfgksgeorh"
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)

	from .views import views

	app.register_blueprint(views, url_prefix='/')

	from .models import User


	create_database(app)

	return app
	
	

def create_database(app):
	if not path.exists('instance/' + DB_NAME):
		from .models import User
		with app.app_context():
			db.create_all()
			db.session.commit()
			user = User(id=0, nickname=None, email=None, rating=None)
			db.session.add(user)
			db.session.commit()
		print('\n\n\nDatabase created!\n\n\n')
