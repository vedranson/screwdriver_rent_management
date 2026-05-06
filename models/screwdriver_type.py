from odoo import models, fields


class ScrewdriverType(models.Model):
    _name = "screwdriver.type"
    _description = "Screwdriver Type"

    # id is automatically created
    name = fields.Char(string="Name", required=True)
    name_old_sys = fields.Char(string="Name Old System")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)
