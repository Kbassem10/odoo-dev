# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Render Data',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Rendering data from the backend',
    'description': """
Render Data Module
==================
A module for rendering data from the backend to the frontend interface.
Provides functionality to display and manipulate data through web views.
    """,
    'depends': ['base', 'web', 'website'],
    'data': [
        'views/static_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
