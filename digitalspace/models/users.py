from odoo import models, fields, api

class InhertUsers(models.Model):
    _inherit = 'res.users'

    is_instructor = fields.Boolean('Instructor ?')