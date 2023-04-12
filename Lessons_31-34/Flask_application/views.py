import re
from __init__ import app
from flask import redirect, url_for, request, abort, render_template, session
import logging
from random import randint, choices
from templates import *

app.secret_key = b'temporary-secret-key'


@app.route('/hello')
def hello_world():
    logging.info(msg='Request at /hello')
    return 'Hello World!'


@app.get('/users')
def users():
    if session.get('username') is None:
        return redirect(url_for('login'))
    names = ['Анна', 'Олександра', 'Катерина', 'Ірина', 'Вікторія', 'Марія', 'Олена', 'Наталія', 'Юлія', 'Тетяна',
             'Олександр', 'Андрій', 'Володимир', 'Сергій', 'Михайло', 'Іван', 'Олег', 'Юрій', 'Дмитро', 'Віктор']
    count = request.args.get('count')
    if count:
        count = int(count)
    else:
        count = randint(1, len(names))
    selected = choices(names, k=count)
    users_dict = {str(i): selected[i - 1] for i in range(1, count + 1)}
    return render_template('users.html', users_dict=users_dict, username=session.get('username'))


@app.get('/users/<int:user_id>')
def user_for_id(user_id):
    if session.get('username') is None:
        return redirect(url_for('login'))
    if user_id % 2 == 0:
        return render_template('users.id.html', user_id=user_id, username=session.get('username'))
    else:
        return 'Not Found', 404


@app.get('/books')
def books():
    if session.get('username') is None:
        return redirect(url_for('login'))
    books_dict = {
        'J.K. Роулінг': 'Гаррі Поттер і філософський камінь',
        'Наполеон Хілл': 'Таємниця успіху',
        'Пауло Коельйо': 'Алхімік',
        'Луис Пратс': 'Хатіко: Вірний друг',
        'Антуан де Сент-Екзюпері': 'Маленький принц'
    }
    count = request.args.get('count')
    if count:
        count = int(count)
    else:
        count = randint(1, len(books_dict))
    books_dict = dict(list(books_dict.items())[:count])
    return render_template('books.html', books_dict=books_dict, count=count, username=session.get('username'))


@app.get('/books/<string:title>')
def books_title(title):
    if session.get('username') is None:
        return redirect(url_for('login'))
    return render_template('books.id.html', title=title.capitalize(), username=session.get('username'))


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
