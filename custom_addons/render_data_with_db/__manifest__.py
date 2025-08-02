# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Render Data with DB',
    'version': '1.0.0',
    'summary': 'User Info Form with Database Storage',
    'description': """
        A module that provides a web form to collect user information
        and store it in the database.
    """,
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'category': 'Website',
    'depends': ['base', 'website'],
    'data': [
        'views/user_form_template.xml',
        'views/users_list_template.xml',
        'views/user_info_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
