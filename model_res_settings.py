from odoo import fields, api, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    vendor_sequence = fields.Many2one('ir.sequence', string="Vendor Reference",readonly=False, copy=False, related="company_id.vendor_reference",
                                      help="Company's Vendor Reference")
