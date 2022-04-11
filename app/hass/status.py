from . import hass_bp, config
from ..utils import create_request
from flaskz.log import flaskz_logger

config = config["default"]
default_headers = config.HASS_DEFAULT_HEADERS
token = config.HASS_TOKEN
base_url = config.HASS_BASE_URL


def request_api(url, method='GET', headers=None):
    if headers is None:
        headers = default_headers
    url = base_url + url
    return create_request(url=url, method=method, headers=headers)


def get_route_log(route):
    flaskz_logger.info('Route: ' + route)


@hass_bp.route('/get_all_status', methods=['GET'])
def get_status():
    get_route_log('/get_all_status')
    return request_api('/api/states')
