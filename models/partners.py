from odoo import models, fields


class CustomPartner(models.Model):
    _inherit = 'res.partner'

    is_import = fields.Boolean('Importación')
