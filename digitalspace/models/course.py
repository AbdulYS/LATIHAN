# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'digitalspace.course'
    _description = 'digitalspace.course'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    