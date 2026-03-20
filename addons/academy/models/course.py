from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course info'

    name = fields.Char(string='Title', required=True)
    active = fields.Boolean(string='Active', default=True)

    description = fields.Text()
    level = fields.Selection(string="Level",
                             selection=[
                                 ('beginner', 'Beginner'),
                                 ('intermediate', 'Intermediate'),
                                 ('advanced', 'Advanced'),
                             ], copy=False)
    session_ids = fields.One2many(comodel_name='academy.session', string='Sessions', inverse_name='course_id')
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency'
                                  , default=lambda self: self.env.company.currency_id.id)

                                  
    base_price = fields.Monetary(string='Price', currency_field='currency_id')
    additional_fee = fields.Monetary(string='Additional Fee', currency_field='currency_id')
    total_price = fields.Monetary(string='Total Price', currency_field='currency_id', compute='_compute_total_price')


    @api.depends('base_price', 'additional_fee')
    def _compute_total_price(self):
        for records in self:
            if(records.base_price < 0):
                raise ValidationError("Base price cannot be negative.")
            records.total_price = records.base_price + records.additional_fee


