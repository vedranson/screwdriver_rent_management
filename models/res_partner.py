from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    screwdriver_rental_ids = fields.One2many(
        comodel_name="screwdriver.rental",
        inverse_name="partner_id",
        string="Rented Screwdrivers",
    )
    screwdriver_rental_active_ids = fields.One2many(
        comodel_name="screwdriver.rental",
        inverse_name="partner_id",
        string="Currently Holding",
        domain=[("return_date", "=", False)],
    )
    screwdriver_rental_history_ids = fields.One2many(
        comodel_name="screwdriver.rental",
        inverse_name="partner_id",
        string="Rental History",
        domain=[("return_date", "!=", False)],
    )