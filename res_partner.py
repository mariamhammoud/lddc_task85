from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vendor_reference = fields.Char(string='Unique Vendor Reference', help="The Unique Sequence no", required=True,
                                   copy=False, readonly=True, default='/')

    @api.model
    def create(self, values):
        if values.get('supplier_rank') and values.get('supplier_rank') > 0 and values.get('vendor_reference', '/') == '/': #if it's a vendor not having seq
            vendor_sequence = self.env.company.vendor_reference
            if vendor_sequence: # if a seq is selected from settings
                next_seq_id = vendor_sequence.next_by_id()
                #if next_seq_id: #max nb of seq is attempted
                    #values['vendor_reference'] = next_seq_id
                values['vendor_reference'] = next_seq_id
                #else:
                    #raise Warning(_("Max Number of Sequences is Attempted"))
        result = super(ResPartner, self).create(values)
        return result
