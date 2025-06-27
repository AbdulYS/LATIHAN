# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'digitalspace.course'
    _description = 'digitalspace.course'

    _sql_constraints = [
        ('_check_name_unique', 'UNIQUE(name)', 'Name must be unique'),
        ('_check_name_different_description', 'CHECK(name != description)', 'Name and description must be different')
    ]

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    # Many2one
    user_id = fields.Many2one('res.users', string='Responsible user')

    # One2many
    session_ids = fields.One2many('digitalspace.session', 'course_id', string='Sessions')