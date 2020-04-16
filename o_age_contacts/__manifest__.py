# -*- coding: utf-8 -*-
{
    'name': 'O Age Contacts',
    'version': '0.2',
    'category': 'Hidden',
    'application': False,
    'author': 'nuxpy',
    'contributors': [
        'Félix Urbina <furbina@nuxpy.com>'
    ],
    'website': 'https://nuxpy.com',
    'summary': 'Fix a born day to see the age of a contact.',
    'description': """This module has the following things:
* A new field to introduce the born day of a contact.
* A new field to show the age of a contact according to the field of the born day.
""",
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False
}
