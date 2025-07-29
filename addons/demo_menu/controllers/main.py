from odoo import http
from odoo.http import request

class StudentDetail(http.Controller):
    @http.route('/student', auth='public', website=True)
    def index(self):
        return request.render('demo_menu.student_data')