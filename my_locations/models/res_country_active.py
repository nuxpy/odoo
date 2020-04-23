# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api, _
from odoo.exceptions import Warning
from odoo.tools import float_is_zero
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import odoo.addons.decimal_precision as dp
from datetime import *
import pytz
from pytz import timezone
import logging
_logger = logging.getLogger(__name__)
import os
import wget
import tempfile
import io
import zipfile


class ResCountryActive(models.Model):
    _name = 'res.country.active'
    _description = 'Countries to import'
    
    name = fields.Char('Name')
    description = fields.Text('Description')
    code = fields.Char('Code', size=2)
    to_import = fields.Boolean('To import', default=False)
    imported = fields.Boolean('Imported', default=False)
    
    _order = 'to_import desc, imported desc, name'
    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'The code must be unique!')
    ]
    
    def check_import_locations(self):
        all_countries = self.search([(1, '=', 1)])
        for r in all_countries:
            if r.name == '-':
                name = self.env['res.country'].search([('code', '=', r.code)], limit=1).name or ''
                r.write({'name': name})
            if r.to_import == True and r.imported == False:
                country_code = r.code
                url_config = self.env['ir.config_parameter'].get_param('geoname.url')
                if url_config:
                    url = '%s/%s.zip' % (url_config, country_code)
                    _logger.info('Starting to download %s' % url)
                    tempdir = tempfile.mkdtemp(prefix='odoo')
                    tempdir_file_zip = os.path.join(tempdir, '%s.zip' % country_code)
                    get_file = wget.download(url, '%s' % tempdir_file_zip)
                    os.system('unzip %s -d %s/' % (tempdir_file_zip, tempdir))
                    file_list = os.path.join(tempdir, '%s.txt' % country_code)
                else:
                    _logger.warning(_('Missing config parameter, e.g.: http://download.geonames.org/export/zip'))
                    return False
                
                if file_list:
                    content_csv_file_r = open(file_list, 'r', encoding='utf-8')
                    state = []
                    province = []
                    community = []
                    locations = []
                    line = content_csv_file_r.readline()
                    while line:
                        l = line.split('\t')
                        data = {}
                        vals = {}
                        data = {
                            'code_country': l[0].strip(),
                            'zip': l[1].strip(),
                            'location_name': l[2].strip(),
                            'name_state': l[3].strip(),
                            'code_state': l[4].strip(),
                            'name_province': l[5].strip(),
                            'code_province': l[6].strip(),
                            'name_community': l[7].strip(),
                            'code_community': l[8].strip(),
                            'latitude': l[9].strip(),
                            'longitude': l[10].strip()
                        }
                        country_id = self.env['res.country'].search([('code', '=', data['code_country'])], limit=1).id or ''
                        state_id = self.env['res.country.state'].search([('code', '=', data['code_state']), 
                            ('country_id', '=', country_id)], limit=1).id or ''
                        province_id = self.env['res.country.province'].search([('code', '=', data['code_province']),
                            ('country_id', '=', country_id)], limit=1).id or ''
                        if not province_id:
                            province_id = self.env['res.country.province'].create({
                                'name': data['name_province'],
                                'code': data['code_province'],
                                'country_id': country_id,
                                'state_id': state_id
                            }).id
                        community_id = self.env['res.country.community'].search([('code', '=', data['code_community']),
                            ('country_id', '=', country_id)], limit=1).id or ''
                        if not community_id:
                            community_id = self.env['res.country.community'].create({
                                'name': data['name_community'],
                                'code': data['code_community'],
                                'country_id': country_id,
                                'state_id': state_id,
                                'province_id': province_id
                            }).id
                        vals = {
                            'name': data['location_name'],
                            'zip': data['zip'],
                            'country_id': country_id,
                            'state_id': state_id,
                            'province_id': province_id,
                            'community_id': community_id,
                            'latitude': data['latitude'],
                            'longitude': data['longitude']
                        }
                        self.env['res.country.location'].create(vals)
                        line = content_csv_file_r.readline()
                    content_csv_file_r.close()
                    os.system('rm -rf %s' % file_list.split('/')[1])
                    r.write({'imported': True})
        return True
