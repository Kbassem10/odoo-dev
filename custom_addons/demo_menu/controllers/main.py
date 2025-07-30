from odoo import http
from odoo.http import request

class StudentDetail(http.Controller):
    @http.route('/student', auth='public', website=True)
    def index(self):
        data = [
            {'title': 'Learn Python', 'author': 'Guido'},
            {'title': 'Learn Odoo', 'author': 'Fabien'},
            {'title': 'Master Django', 'author': 'Adrian'}
        ]
        return request.render('demo_menu.student_data', {'books': data})