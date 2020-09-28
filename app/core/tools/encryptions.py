from app.utils import generatePassword

import hashlib

def set_password(password):
	genereated_pass = generatePassword(password)
	encrypted = hashlib.sha256(password.encode('utf-8'))
	return encrypted.hexdigest()

def verify_password(password, c):
	encrypted_password = set_password(password)
	if encrypted_password == c:
		return True
	return False