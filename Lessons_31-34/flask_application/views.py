import os
import re
from __init__ import app, db
from flask import redirect, url_for, request, abort, render_template, session
import logging
from templates import *
from models import *

app.secret_key = os.getenv('SECRET_KEY')


@app.route('/hello')
def hello_world():
    logging.info(msg='Request at /hello')
    return 'Hello World!'


@app.route('/users', methods=['GET', 'POST'])
def users():
    if session.get('username') is None:
        return redirect(url_for('login'))

    if request.method == 'GET':
        size = int(request.args.get('size')) if request.args.get('size') else 1000000
        all_users = db.session.execute(db.select(User).limit(size)).scalars()
        return render_template('users.html', all_users=all_users, username=session.get('username'))

    elif request.method == 'POST':
        content_type = request.headers['Content-Type']
        if content_type == 'application/json':
            data = request.get_json()
        elif content_type == 'application/x-www-form-urlencoded':
            data = request.form
        else:
            return 'Forbidden content type', 400
        user = User(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            age=int(data.get('age')) if data.get('age') else ''
        )
        db.session.add(user)
        db.session.commit()
        return 'ok', 201

    else:
        return 'Forbidden request method', 405


@app.get('/users/<int:user_id>')
def user_for_id(user_id):
    if session.get('username') is None:
        return redirect(url_for('login'))

    user = User.query.get(user_id)
    if user:
        return render_template('users.id.html', user=user, username=session.get('username'))
    else:
        return 'User not Found', 404


@app.route('/books', methods=['GET', 'POST'])
def books():
    if session.get('username') is None:
        return redirect(url_for('login'))

    if request.method == 'GET':
        size = int(request.args.get('size')) if request.args.get('size') else 1000000
        all_books = db.session.execute(db.select(Book).limit(size)).scalars()
        return render_template('books.html', all_books=all_books, size=size, username=session.get('username'))

    elif request.method == 'POST':
        content_type = request.headers['Content-Type']
        if content_type == 'application/json':
            data = request.get_json()
        elif content_type == 'application/x-www-form-urlencoded':
            data = request.form
        else:
            return 'forbidden content type', 400
        book = Book(
            title=data.get('title'),
            author=data.get('author'),
            year=int(data.get('year')) if data.get('year') else '',
            price=int(data.get('price')) if data.get('price') else ''

        )
        db.session.add(book)
        db.session.commit()
        return 'ok', 201

    else:
        return 'Forbidden request method', 405


@app.get('/books/<int:book_id>')
def books_title(book_id):
    if session.get('username') is None:
        return redirect(url_for('login'))

    book = Book.query.get(book_id)
    if book:
        return render_template('books.id.html', book=book, username=session.get('username'))
    else:
        return 'User not Found', 404


@app.route('/purchases', methods=['GET', 'POST'])
def purchases():
    if session.get('username') is None:
        return redirect(url_for('login'))

    if request.method == 'GET':
        size = int(request.args.get('size')) if request.args.get('size') else 1000000
        all_purchases = db.session.execute(db.select(Purchase).limit(size)).scalars()
        return render_template('purchases.html', all_purchases=all_purchases, size=size,
                               username=session.get('username'))

    elif request.method == 'POST':
        content_type = request.headers['Content-Type']
        if content_type == 'application/json':
            data = request.get_json()
        elif content_type == 'application/x-www-form-urlencoded':
            data = request.form
        else:
            return 'Forbidden content type', 400

        user_id = data.get('user_id')
        if not User.query.get(user_id):
            return f"User with ID {user_id} is not found"

        book_id = data.get('book_id')
        if not Book.query.get(book_id):
            return f"Book with ID {book_id} is not found"

        purchase = Purchase(
            user_id=user_id,
            book_id=book_id,
        )
        db.session.add(purchase)
        db.session.commit()
        return 'ok', 201
        # else:
        #     return 'not ok', 400
    else:
        return 'Forbidden request method', 405


@app.get('/params')
def params():
    if session.get('username') is None:
        return redirect(url_for('login'))
    return render_template('params.html', attr=request.args.items(), username=session.get('username'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username) >= 5 and \
                len(password) >= 8 and \
                re.search(r'\d', password) and \
                re.search(r'[A-Z]', password):
            session['username'] = username
            return redirect(url_for('users')), 201
        else:
            abort(400)


@app.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
