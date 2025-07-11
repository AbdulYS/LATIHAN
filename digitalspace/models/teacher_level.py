# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TeacherLevel(models.Model):
    _name = 'digitalspace.teacher_level'
    _description = 'Teacher Level'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')