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


class ResCountry(models.Model):
    _name = 'res.country.province'
    _description = 'Provinces of a country'
    
    name = fields.Char('Name')
    description = fields.Text('Description')
    code = fields.Char('Code')
    country_id = fields.Many2one('res.country', string="Country")
    state_id = fields.Many2one('res.country.state', string="State")
    community_ids = fields.One2many('res.country.community', 'province_id', string="Communities")
    partner_ids = fields.One2many('res.partner', 'province_id', string="Partners")
    
    _order = 'country_id, name'
