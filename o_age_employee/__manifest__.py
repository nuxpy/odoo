# -*- coding: utf-8 -*-
{
    'name': 'O Age Employee',
    'version': '0.1',
    'category': 'Hidden',
    'application': False,
    'author': 'nuxpy',
    'contributors': [
        'Félix Urbina <furbina@nuxpy.com>'
    ],
    'website': 'https://nuxpy.com',
    'summary': 'Calculate the age of an employee.',
    'description': """This module has the following things:
* A new field to show the age of a contact according to the field of the born day.
""",
    'depends': ['hr'],
    'data': [
        'views/hr_employee_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False
}
