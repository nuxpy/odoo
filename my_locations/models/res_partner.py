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


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Locations for res_partner'
    
    province_id = fields.Many2one('res.country.province', string="Province")
    community_id = fields.Many2one('res.country.community', string="Community")
    location_id = fields.Many2one('res.country.location', string="Location")
    latitude = fields.Float('Latitude')
    longitude = fields.Float('Longitude')
    
    @api.onchange("location_id")
    def onchange_location_id(self):
        if self.location_id:
            self.city = self.location_id.name if self.location_id.name else ''
            self.state_id = self.location_id.state_id.id if self.location_id.state_id else ''
            self.province_id = self.location_id.province_id.id if self.location_id.province_id else ''
            self.zip = self.location_id.zip if self.location_id.zip else ''
            self.country_id = self.location_id.country_id.id if self.location_id.country_id else ''
            self.latitude = self.latitude if self.latitude else ''
            self.longitude = self.longitude if self.longitude else ''
