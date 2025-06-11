# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Session(models.Model):
    _name = 'digitalspace.session'
    _description = 'digitalspace.session'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    duration = fields.Float(string='Duration')
    number_of_seats = fields.Float(string='Number of seats')
    description = fields.Text(string='Description')