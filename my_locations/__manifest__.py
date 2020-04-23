# -*- coding: utf-8 -*-
{
    'name': 'My Locations',
    'version': '0.2',
    'category': 'Localization',
    'application': False,
    'author': 'nuxpy',
    'contributors': [
        'Félix Urbina <nuxpy4@gmail.com>'
    ],
    'website': 'https://nuxpy.com',
    'summary': '',
    'description': """
""",
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/location_param_data.xml',
        'data/res_country_active_data.xml',
        'data/cron_import_locations_data.xml',
        'views/res_country_active_view.xml',
        'views/res_country_province_view.xml',
        'views/res_country_community_view.xml',
        'views/res_country_location_view.xml',
        'views/res_partner_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False
}
