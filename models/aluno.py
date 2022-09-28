""" from ..extensions import db


class Aluno(db.Model):
    __tablename__ = "alunos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    ra = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return "<Uc(nome={}, email={}, ra={})>".format(self.nome, self.email, self.ra)
 """
