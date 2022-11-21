import pytest
import requests
import json


def test_get_methods():
	# get users and check
	users = requests.get('http://127.0.0.1:8099/api/users')
	n_users = len(users.json())
	assert n_users > 0

def test_post_method():
	# create user and check
	users = requests.get('http://127.0.0.1:8099/api/users')
	n_users = len(users.json())
	r = requests.post('http://127.0.0.1:8099/users', json={
			'nickname': 'my_name',
			'email': 'NOT_my_email@gmail.com',
			'rating': '100500'
		})
	users = requests.get('http://127.0.0.1:8099/api/users')
	assert len(users.json()) > n_users
	n_users = len(users.json())
	assert users.json()[-1]['nickname'] == 'my_name'
	assert users.json()[-1]['email'] == 'NOT_my_email@gmail.com'
	assert users.json()[-1]['rating'] == '100500'

def test_put_method():
	# modify user and check
	users = requests.get('http://127.0.0.1:8099/api/users')
	n_users = len(users.json())
	last_id = users.json()[-1]['id']
	r = requests.put(f'http://127.0.0.1:8099/users/{last_id}', json={
			'id': last_id,
			'nickname': 'my_name',
			'email': 'my_email@gmail.com',
			'rating': '100500'
		})
	users = requests.get('http://127.0.0.1:8099/api/users')
	assert len(users.json()) == n_users
	assert users.json()[-1]['nickname'] == 'my_name'
	assert users.json()[-1]['email'] == 'my_email@gmail.com'
	assert users.json()[-1]['rating'] == '100500'

def test_delete_method():
	# delete user and check
	users = requests.get('http://127.0.0.1:8099/api/users')
	n_users = len(users.json())
	last_id = users.json()[-1]['id']
	r = requests.delete(f'http://127.0.0.1:8099/users/{last_id}')
	users = requests.get('http://127.0.0.1:8099/api/users')
	assert len(users.json()) < n_users
	
