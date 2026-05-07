from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    screwdriver_rental_ids = fields.One2many(
        comodel_name="screwdriver.rental",
        inverse_name="partner_id",
        string="Rented Screwdrivers",
    )