# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hello Module',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Simple Hello Page with Navigation Menu',
    'description': """
Hello Module
============
A simple module that displays a hello page with navigation to other custom addons.
    """,
    'depends': ['base', 'web', 'website'],
    'data': [
        'views/hello_page.xml',
        'data/menu_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
