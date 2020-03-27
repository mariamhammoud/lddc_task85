from odoo import models, fields


class CompanySequence(models.Model):
    _inherit = 'res.company'

    vendor_reference = fields.Many2one('ir.sequence', string="Vendor Reference",
                                       help="Company's Vendor Reference")
