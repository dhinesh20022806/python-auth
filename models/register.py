from db.database import get_db


def create_table():
    db = get_db()

    cursor = db.cursor()

    cursor.execute(""" 
        IF NOT EXIST CREATE TABLE users
        (
            id SERIAL,
            email VARCHAR(100) UNIQUE,
            password TEXT

        );

        """)
    print('successfully created ')

    if __name__ == '__main__':
        create_table()


def insert_table(email, password):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""INSERT INTO users (email, password) VALUES (%s, %s)""", (email, password))
    db.commit()
    cursor.close()
    db.close()
    print('successfully inserted to the table')
