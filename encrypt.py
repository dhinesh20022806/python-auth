from bcrypt import gensalt, hashpw, checkpw

def hash_password(text):
	bytes = text.encode('utf-8')
	salt = gensalt()
	hash = hashpw(bytes, salt)
	return hash 

def verify_password(text, stored_password):
	user_bytes = text.encode('utf-8')

	result = checkpw(user_bytes , stored_password)

	return result