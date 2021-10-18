# -*- coding: utf-8 -*-

{
    'name': 'Airline management',
    'version': '1.0',
    'category': 'Hidden',
    'description': """Modulo para el control de actividades basicas en una aerolinea""",
    'website': 'https://www.odoo.com/app/airline',
    'depends': ['base_setup'],
    'data': [
        'data/ir.model.access.csv',

        'views/country_view.xml',
        'views/role_view.xml',
        'views/activity_view.xml',
        'views/person_view.xml',
        'views/control_log_view.xml',
        'views/airline_menu.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}