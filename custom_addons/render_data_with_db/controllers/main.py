from odoo import http
from odoo.http import request

class UserFormController(http.Controller):

    @http.route('/hello/form', auth='user', website=True)
    def user_form(self, **kwargs):

        user_info = request.env['custom.userinfo'].search([('user_id', '=', request.env.user.id)], limit=1)
        return request.render('render_data_with_db.user_form_template', {
            'user_info': user_info
        })

    @http.route('/hello/form/submit', auth='user', type='http', website=True, csrf=True)
    def user_form_submit(self, **post):
        name = post.get('name')
        email = post.get('email')
        age = post.get('age')
        birthdate = post.get('birthdate')
        fav_color = post.get('fav_color')
        fav_number = post.get('fav_number')

        try:
            existing_info = request.env['custom.userinfo'].search([('user_id', '=', request.env.user.id)], limit=1)
            
            data = {
                'name': name,
                'email': email,
                'age': int(age) if age else 0,
                'birthdate': birthdate,
                'fav_color': fav_color,
                'fav_number': int(fav_number) if fav_number else 0,
            }
            
            if existing_info:
                existing_info.write(data)
            else:
                request.env['custom.userinfo'].create(data)
                
            return request.render('render_data_with_db.user_form_template', {
                'success_message': 'User information saved successfully!',
                'user_info': request.env['custom.userinfo'].search([('user_id', '=', request.env.user.id)], limit=1)
            })
        except Exception as e:
            return request.render('render_data_with_db.user_form_template', {
                'error_message': 'Error saving user information. Please try again.'
            })
        
    @http.route('/hello/form/delete', auth='user', type='http', website=True, csrf=True)
    def user_form_delete(self, **kwargs):
        try:
            record = request.env['custom.userinfo'].search([('user_id' , '=' , request.env.user.id)], limit=1)
            if record:
                record.unlink()
                return request.render('render_data_with_db.user_form_template', {
                'success_message': 'Your data has been deleted.'
                })
            else:
                return request.render('render_data_with_db.user_form_template', {
                    'error_message': 'No data found to delete.'
                })
        except Exception as e:
            return request.render('render_data_with_db.user_form_template', {
                'error_message': 'Error deleting data. Please try again.'
            })