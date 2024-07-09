from db.database import get_db

def select_table(email):
	db = get_db()
	cursor = db.cursor()

	cursor.execute(""" SELECT email, password FROM users WHERE email= %s ;""",(email,))

	row = cursor.fetchone()

	print(row, 'login model')

	

	cursor.close()
	db.close()

	return row
