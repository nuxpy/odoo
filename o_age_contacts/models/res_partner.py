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
    _description = 'Methods and fields related with res_partner'
    
    birthday = fields.Date('Born day')
    age = fields.Integer('Age', compute='_calc_age')
    
    
    @api.depends('birthday')
    def _calc_age(self):
        for rec in self:
            age = 0
            if rec.birthday:
                date_today = date.today()
                if date_today.__ge__(rec.birthday):
                    age = date_today.__sub__(rec.birthday).days / 365
            rec.age = age
