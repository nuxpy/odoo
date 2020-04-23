# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api, _
from odoo.exceptions import Warning
from odoo.tools import float_is_zero
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import odoo.addons.decimal_precision as dp
from datetime import datetime, timedelta
import pytz
from pytz import timezone
import logging
_logger = logging.getLogger(__name__)


class ResCountry(models.Model):
    _inherit = 'res.country'
    _description = 'Countries'
    
    province_ids = fields.One2many('res.country.province', 'country_id', string="Provinces")
    community_ids = fields.One2many('res.country.community', 'country_id', string="Community")
