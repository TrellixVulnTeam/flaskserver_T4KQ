from flask import Blueprint
from . import db

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return 'Index'

@main.route('/Profile')
def profile():
    return 'Profile'

    