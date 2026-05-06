from odoo import models, fields


class ScrewdriverType(models.Model):
    _name = 'screwdriver.type'
    _description = 'Screwdriver Type'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')