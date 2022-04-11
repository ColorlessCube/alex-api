from flask import Flask, session
from flaskz import log
from config import config
from .main import main_bp
from .hass import hass_bp


def create_app(config_name):
    app = Flask(__name__)
    app_config = config[config_name]
    app.config.from_object(app_config)
    app_config.init_app(app)

    log.init_log(app)
    log.flaskz_logger.info('-- create app with %s config --' % config_name)

    # CORS(app) # If need to support cross-domain

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(hass_bp, url_prefix='/hass')

    return app
