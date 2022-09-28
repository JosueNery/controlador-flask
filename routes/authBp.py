from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from ..extensions import db
from ..models.user import User

authBp = Blueprint('authBp', __name__)


@authBp.route('/login')
def login():
    return render_template('login.html')


@authBp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Dados de login inválidos')
        return redirect(url_for('authBp.login'))

    login_user(user, remember=remember)
    return redirect(url_for('ucBp.uc_list'))


@authBp.route('/signup')
def signup():
    return render_template('signup.html')


@authBp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    nome = request.form.get('nome')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Endereço de e-mail indisponível')
        return redirect(url_for('authBp.signup'))

    new_user = User(email=email, nome=nome,
                    password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('authBp.login'))


@authBp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
