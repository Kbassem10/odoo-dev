from odoo import http
from odoo.http import request

class StaticDataController(http.Controller):

    @http.route('/hello/static', type='http', auth='public', website=True, sitemap=False)
    def static_page(self, **kw):
        data = [
            {'title': 'Learn Python', 'author': 'Guido'},
            {'title': 'Learn Odoo', 'author': 'Fabien'},
            {'title': 'Master Django', 'author': 'Adrian'}
        ]
        return request.render('render_data.static_template', {'books': data})