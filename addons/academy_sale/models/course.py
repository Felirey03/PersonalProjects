from odoo import api, fields, models

class Course(models.Model):
    _inherit = 'academy.course'

    product_id = fields.Many2one(comodel_name="product.template", string="Related Product")
    