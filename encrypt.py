from bcrypt import gensalt, hashpw, checkpw

def hash_password(text):
	bytes = text.encode('utf-8')
	salt = gensalt()
	hash = hashpw(bytes, salt)
	hash = hash.decode('utf-8')
	return hash 

def verify_password(password, stored_password):
    """Verify a stored password against one provided by user"""
    
    user_password = password.encode('utf-8')

    stored_password_bytes = stored_password.encode('utf-8')
    
    result = checkpw(user_password, stored_password_bytes)
    print(result)
    return result

  	