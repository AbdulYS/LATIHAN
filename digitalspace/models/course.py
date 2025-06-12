# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'digitalspace.course'
    _description = 'digitalspace.course'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    # Many2one
    user_id = fields.Many2one('res.users', string='Responsible user')

    # One2many
    session_ids = fields.One2many('digitalspace.session', 'course_id', string='Sessions')