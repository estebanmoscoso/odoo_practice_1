from odoo import models, fields, api


class CustomStockPickingForm(models.Model):
    _inherit = 'stock.picking'
    operation = fields.Many2one(related='purchase_id.operation')
