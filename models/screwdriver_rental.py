from odoo import api, models, fields
from odoo.tools import Markup


class ScrewdriverRental(models.Model):
    _name = "screwdriver.rental"
    _description = "Screwdriver Rental"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Rental Reference", compute="_compute_name", store=True
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Renter",
        ondelete="cascade",
        index=True,
        required=True,
        tracking=True,
    )
    screwdriver_id = fields.Many2one(
        comodel_name="screwdriver",
        string="Screwdriver",
        ondelete="cascade",
        index=True,
        required=True,
        tracking=True,
    )
    rental_date = fields.Date(
        string="Rental Date", required=True, tracking=True
    )
    return_date = fields.Date(string="Return Date", tracking=True)

    @api.depends("partner_id", "screwdriver_id", "rental_date")
    def _compute_name(self):
        for rec in self:
            if rec.partner_id and rec.screwdriver_id and rec.rental_date:
                rec.name = "%s - %s - %s" % (
                    rec.partner_id.name,
                    rec.screwdriver_id.name,
                    rec.rental_date,
                )
            else:
                rec.name = ""

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        rec.partner_id.message_post(
            body=Markup("Screwdriver rental created: %s")
            % rec._get_html_link(),
            message_type="notification",
            subtype_xmlid="mail.mt_note",
        )
        return rec

    def write(self, vals):
        res = super().write(vals)
        for rec in self:
            rec.partner_id.message_post(
                body=Markup("Screwdriver rental updated: %s")
                % rec._get_html_link(),
                message_type="notification",
                subtype_xmlid="mail.mt_note",
            )
        return res
