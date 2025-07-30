from odoo import http
from odoo.http import request

class HelloController(http.Controller):

    @http.route('/hello', type='http', auth='public', website=True, sitemap=False)
    def hello_page(self, **kw):
        return request.render('hello.hello_page')