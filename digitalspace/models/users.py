from odoo import models, fields, api

class InhertUsers(models.Model):
    _inherit = 'res.users'

    is_instructor = fields.Boolean('Instructor ?')
    teacher_level_id = fields.Many2one('digitalspace.teacher_level', 'Teacher Level')