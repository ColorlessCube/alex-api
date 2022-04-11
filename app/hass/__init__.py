from flask import Blueprint
from config import config

hass_bp = Blueprint('hass', __name__)

from .status import *
