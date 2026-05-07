from odoo import models, fields


class Screwdriver(models.Model):
    _name = "screwdriver"
    _description = "Screwdriver"

    # id is automatically created
    name = fields.Char(string="ID", required=True)
    type_id = fields.Many2one(
        comodel_name="screwdriver.type",
        string="Screwdriver Type",
        ondelete="cascade",
        index=True,
        required=True,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("available", "Available"), 
            ("rented", "Rented"), 
            ("decommissioned", "Decommissioned")],
        default="available",
        required=True,
    )