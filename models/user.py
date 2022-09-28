from flask_login import UserMixin
from ..extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


def __repr__(self):
    return "<Uc(nome={}, email={}>".format(self.nome, self.email)
