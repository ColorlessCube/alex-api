# static page route

from flask import Blueprint

# static folder
main_bp = Blueprint('main', __name__, static_folder='../pages', static_url_path='/')

from . import errors
from . import page
