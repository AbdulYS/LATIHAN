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

    # Many2one
    user_id = fields.Many2one('res.users', string='Instructor', domain="['!',('is_instructor','=',True),('teacher_level_id','!=',False)]")
    course_id = fields.Many2one(comodel_name='digitalspace.course', string='Course', required=True)

    # Many2many
    partner_ids = fields.Many2many('res.partner', string='Attendees')