from odoo import http
from odoo.http import request
from datetime import datetime, timedelta

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

    @http.route('/hello/users', auth='public', website=True)
    def users_list(self, page=1, search='', color_filter='', age_filter='', **kwargs):
        domain = []
        
        # Search filter
        if search:
            domain.extend(['|', ('name', 'ilike', search), ('email', 'ilike', search)])
        
        # Color filter
        if color_filter:
            domain.append(('fav_color', 'ilike', color_filter))
        
        # Age filter
        if age_filter == 'young':
            domain.extend([('age', '>=', 18), ('age', '<=', 30)])
        elif age_filter == 'middle':
            domain.extend([('age', '>=', 31), ('age', '<=', 50)])
        elif age_filter == 'senior':
            domain.append(('age', '>=', 51))
        
        # Get users with pagination
        users_per_page = 12
        total_users = request.env['custom.userinfo'].search_count(domain)
        
        pager = request.website.pager(
            url="/hello/users",
            total=total_users,
            page=page,
            step=users_per_page,
            url_args={'search': search, 'color_filter': color_filter, 'age_filter': age_filter}
        )
        
        users = request.env['custom.userinfo'].search(
            domain, 
            limit=users_per_page, 
            offset=pager['offset'],
            order='register_date desc'
        )
        
        # Get available colors for filter dropdown
        all_users = request.env['custom.userinfo'].search([('fav_color', '!=', False)])
        available_colors = list(set(user.fav_color for user in all_users if user.fav_color))
        available_colors.sort()
        
        # Statistics
        total_users_count = request.env['custom.userinfo'].search_count([])
        users_with_complete_info = request.env['custom.userinfo'].search_count([
            ('age', '>', 0), ('birthdate', '!=', False), ('fav_color', '!=', False)
        ])
        
        # Recent users (last 7 days)
        week_ago = datetime.now() - timedelta(days=7)
        recent_users_count = request.env['custom.userinfo'].search_count([
            ('register_date', '>=', week_ago.strftime('%Y-%m-%d %H:%M:%S'))
        ])
        
        return request.render('render_data_with_db.users_list_template', {
            'users': users,
            'pager': pager,
            'search_term': search,
            'color_filter': color_filter,
            'age_filter': age_filter,
            'available_colors': available_colors,
            'total_users': total_users_count,
            'users_with_complete_info': users_with_complete_info,
            'recent_users': recent_users_count
        })