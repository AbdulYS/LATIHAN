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
    user_id = fields.Many2one('res.users', string='Instructor', domain="['|',('is_instructor','=',True),('teacher_level_id','!=',False)]")
    course_id = fields.Many2one(comodel_name='digitalspace.course', string='Course', required=True)

    # Many2many
    partner_ids = fields.Many2many('res.partner', string='Attendees')


    # Compute
    taken_seats = fields.Float(compute='_compute_taken_seats', string='Taken Seats')
    
    @api.depends('partner_ids','number_of_seats')
    def _compute_taken_seats(self):
        for rec in self:
            if rec.number_of_seats and rec.partner_ids:
                rec.taken_seats = len(rec.partner_ids) / rec.number_of_seats * 100
            else:
                rec.taken_seats = 0