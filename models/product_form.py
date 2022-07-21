from odoo import models, fields


class CustomProductTemplate(models.Model):
    _inherit = 'product.template'

    # def _get_is_import(self):
    #     return True

    is_import = fields.Boolean('Importación')