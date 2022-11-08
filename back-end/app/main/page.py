# map the path to the static html files
from flask import redirect

from . import main_bp

page_mapping = {
}


@main_bp.route('/favicon.ico')
def favicon():
    return main_bp.send_static_file('./favicon.ico')


@main_bp.route('/', defaults={'page': 'index'})
@main_bp.route('/<page>', methods=['GET'])
def show_page(page):
    _page = page_mapping.get(page)
    if _page:
        if page == 'index' or page == 'login':
            return main_bp.send_static_file(_page)
        return redirect(_page)

    if page.endswith(".html"):
        return main_bp.send_static_file(page)

    return main_bp.send_static_file(page_mapping.get('error_404'))
