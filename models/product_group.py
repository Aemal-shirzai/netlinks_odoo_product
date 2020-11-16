from odoo import models, fields, api, _

class ProductGroup(models.Model):
    '''This Class Create new model for product groups'''
    
    _name = "netlinks.product.group"
    _description = "Groups For Product template model"

    _sql_constraints = [('name_uniq', 'unique (name)',
                         'The category name must be unique !')]

    name = fields.Char(string='Group Name', required=True)
    group_id = fields.One2many('product.template', 'group_id')

    