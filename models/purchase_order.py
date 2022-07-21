from odoo import models, fields, api


class CustomPurchaseOrderForm(models.Model):
    _inherit = 'purchase.order'

    operation = fields.Many2one('freight.operation', 'Lote Imp')

    is_import = fields.Boolean(related='partner_id.is_import')
