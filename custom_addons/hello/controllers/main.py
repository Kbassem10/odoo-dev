from odoo import http
from odoo.http import request

class HelloController(http.Controller):

    @http.route('/hello', type='http', auth='public', website=True)
    def hello_page(self):
        return request.render('hello.hello_page')

    @http.route('/student', type='http', auth='public', website=True)
    def student_books(self):
        books = [
            {'title': 'Python Programming', 'author': 'John Doe'},
            {'title': 'Web Development', 'author': 'Jane Smith'},
            {'title': 'Data Science', 'author': 'Bob Johnson'},
        ]
        return request.render('demo_menu.student_data', {'books': books})

    @http.route('/books', type='http', auth='public', website=True)
    def static_books(self):
        books = [
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
            {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
            {'title': '1984', 'author': 'George Orwell'},
        ]
        return request.render('render_data.static_template', {'books': books})