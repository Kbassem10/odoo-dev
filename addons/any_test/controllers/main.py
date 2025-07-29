from odoo import http
from odoo.http import request

class TestHello(http.Controller):

    @http.route('/hello', type='http', auth='none', csrf=False)
    def hello(self, **kw):
        return "<html><body><h1>Hello World from Any Test Module!</h1><p>Route is working correctly.</p></body></html>"
    
    @http.route('/hello/template', type='http', auth='none', csrf=False)
    def hello_template(self, **kw):
        return request.render('any_test.Hello')