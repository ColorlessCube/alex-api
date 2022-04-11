from requests import request
from flaskz.log import flaskz_logger


def create_request(url, method, headers):
    response = request(url=url, method=method, headers=headers)
    flaskz_logger.info('Remote request completed:\n    url={url}\n    headers={headers}\n    result={result}'.format(**{
        'result': response,
        'url': url,
        'headers': headers
    }))
    return response.text
