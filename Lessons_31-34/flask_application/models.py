from __init__ import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    purchases = db.relationship('Purchase', backref='user', lazy=True)

    def __repr__(self):
        return f'user {self.first_name}'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    price = db.Column(db.Integer)
    purchases = db.relationship('Purchase', backref='book', lazy=True)

    def __repr__(self):
        return f'user {self.title}'


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __repr__(self):
        return f'user {self.id}'



