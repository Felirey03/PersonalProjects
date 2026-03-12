from odoo import fields, models

class PersonalProject(models.Model):
    _name = 'personal.project'
    _description = 'Personal Project'

    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)

    description = fields.Text()





