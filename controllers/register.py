from flask import render_template, request
from re import match

from encrypt import hash_password
from models.register import insert_table
from models.login import select_table


def get_register(email_error=None, password_error=None, confirm_password_error=None):
    return render_template('register.html', email_error=email_error, password_error=password_error,
                           confirm_password_error=confirm_password_error)


def post_register():
    email = request.form['email']
    plain_text = request.form['password']
    plain_text_confirm = request.form['confirm-password']

    regx_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    verify_email = match(regx_email, email)

    regx_plain_text = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    verify_plain_text = match(regx_plain_text, plain_text)

    data = select_table(email)

    if data:
        return get_register('email already exist')

    if not verify_email:
        return get_register('invalid email address')

    if len(plain_text) < 8:
        return get_register(None, 'Minium length 8 characters')

    if not verify_plain_text:
        return get_register(None, '1 uppercase, 1 lowercase, 1 digit, 1 special character')

    if plain_text != plain_text_confirm:
        return get_register(None, 'password should be same', 'password shold be same')

    password = hash_password(plain_text)
    insert_table(email, password)
    return '<h1>you register successfully!</h1>'
