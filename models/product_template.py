from odoo import models, fields, api

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    part_number = fields.Char(string="Part Number")
    group_id = fields.Many2one('netlinks.product.group')
