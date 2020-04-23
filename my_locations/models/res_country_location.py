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


class ResCountryLocation(models.Model):
    _name = 'res.country.location'
    _description = 'Locations'
    
    name = fields.Char('Name')
    description = fields.Text('Description')
    zip = fields.Char('Zip')
    country_id = fields.Many2one('res.country', string="Country")
    state_id = fields.Many2one('res.country.state', string="State")
    province_id = fields.Many2one('res.country.province', string="Province")
    community_id = fields.Many2one('res.country.community', string="Community")
    latitude = fields.Float('Latitude')
    longitude = fields.Float('Longitude')
    partner_ids = fields.One2many('res.partner', 'location_id', string="Partners")
    
    _order = 'country_id, name, zip'
    
    @api.multi
    def name_get(self):
        return [(rec.id, '%s [%s]' % (rec.name, rec.zip)) for rec in self]
    
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if name:
            args = ['|', ('name', operator, name), ('zip', 'like', name)]
        result = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return self.browse(result).name_get()
