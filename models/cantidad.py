# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    qty_total = fields.Float(string='Total',readonly=True,compute='_compute_age',)

    @api.multi
    @api.depends('product_ids.reserved_quantity')
    def _compute_age(self):
        for record in self:
            qty_total = reserved_quantity
