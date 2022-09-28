from flask import Blueprint, render_template
from ..extensions import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    db.create_all()
    return render_template('index.html')
