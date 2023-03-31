import re
from __init__ import app
from flask import redirect, url_for, request, abort
import logging
from random import randint, choices


@app.route('/hello')
def hello_world():
    logging.info(msg='Request at /hello')
    return 'Hello World!'


@app.get('/users')
def users():
    names = ['Анна', 'Олександра', 'Катерина', 'Ірина', 'Вікторія', 'Марія', 'Олена', 'Наталія', 'Юлія', 'Тетяна',
             'Олександр', 'Андрій', 'Володимир', 'Сергій', 'Михайло', 'Іван', 'Олег', 'Юрій', 'Дмитро', 'Віктор']
    count = request.args.get('count')
    if count:
        count = int(count)
    else:
        count = randint(1, len(names))
    users_list = ''
    for name in choices(names, k=count):
        users_list += f'{name}, '
    return users_list, 200


@app.get('/books')
def books():
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
    html_list = '<ol>'
    for key, value in books_dict.items():
        if count > 0:
            html_list += f'<li>{key} - {value}</li>'
            count -= 1
    html_list += '</ol>'
    return html_list, 200


@app.get('/users/<int:id>')
def books_for_id(book_id):
    if book_id % 2 == 0:
        return f'Your id is: {book_id}', 200
    else:
        return 'Not Found', 404


@app.get('/books/<string:title>')
def books_title(title):
    return title.capitalize(), 200


@app.get('/params')
def params():
    html_list = '<ol>'
    for key, value in request.args.items():
        html_list += f'<li>{key} - {value}</li>'
    html_list += '</ol>'
    return html_list, 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        html_form = """
        <style>
          form {
            width: 400px; 
            margin: 380 auto; 
          }
        </style>
        <form method="POST" action="/login">
          <label for="username">Ім'я користувача:</label>
          <input type="text" id="username" name="username"><br>
        
          <label for="password">Пароль:</label>
          <input type="password" id="password" name="password"><br>
        
          <input type="submit" value="Увійти">
        </form>
        """
        return html_form, 200
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username) >= 5 and \
                len(password) >= 8 and\
                re.search(r'\d', password) and\
                re.search(r'[A-Z]', password):
            return redirect(url_for('users')), 201
        else:
            abort(400)
