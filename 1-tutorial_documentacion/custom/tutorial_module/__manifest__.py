# -*- coding: utf-8 -*-

{
    'name': 'Tutorial Module',
    'version': '1.0',
    'category': 'Hidden',
    'description': """Modulo de prueba creado a partir de la documentacions de odoo 15""",
    'website': 'https://www.odoo.com/app/test',
    'depends': ['base_setup'],
    'data': [
        'data/ir.model.access.csv',
        'views/tutorial_test_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
