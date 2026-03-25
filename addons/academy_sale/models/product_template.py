from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[('course', 'Course')], ondelete={'course': 'set service'})
    course_ids = fields.Many2one(comodel_name="academy.course", inverse_name="product_id")

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['course'] = 'service'
        return type_mapping