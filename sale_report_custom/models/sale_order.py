# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    width = fields.Float(string='Ancho', digits=(12, 3), default=0.0)
    height = fields.Float(string='Alto', digits=(12, 3), default=0.0)
