from odoo import models, fields, api

class InhertPartner(models.Model):
    _inherit = 'res.partner'

    session_ids = fields.Many2many('digitalspace.session', string='Sessions')