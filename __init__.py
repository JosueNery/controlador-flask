from flask import Flask
from .extensions import db, migrate, login_manager
from .routes.ucBp import ucBp
from .routes.main import main
from .routes.authBp import authBp
from .models.user import User


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Alguma-chave-SECRETA'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app)
    login_manager.login_view = 'authBp.login'
    login_manager.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(ucBp)
    app.register_blueprint(authBp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
