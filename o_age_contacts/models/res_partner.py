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
    age = fields.Integer('Age', compute='_calc_age', default=0)
    
    
    def _calc_age_raw(self, date_issue):
        age = 0
        date_today = date.today()
        if date_today.__gt__(date_issue):
            age = str(date_today.__sub__(date_issue) / 365).split()[0]
        return age
    
    def _calc_age(self):
        for r in self:
            if r.birthday:
                r.age = self._calc_age_raw(r.birthday)
