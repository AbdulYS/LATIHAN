# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'digitalspace.session'
    _description = 'digitalspace.session'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date', default = fields.Date.today())
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

    # Default
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progres', 'Progres'),
        ('done', 'Done')
    ], string='State', default='draft', track_visibility='onchange')
    active = fields.Boolean(string='Active', default = True)

    def action_confirm(self):
        self.state = 'progres'
    
    def action_done(self):
        self.state = 'done'

    # Onchange
    @api.onchange('number_of_seats')
    def _onchange_number_of(self):
        if self.number_of_seats < 0:
           return {
               'warning': {
                   'title': "Invalid Values",
                   'message': "Please input valid value on number of seats",
               }
           }
        
        if self.number_of_seats < len(self.partner_ids):
            return {
                'warning': { 
                    'title': "Something Bad Happend",
                    'message': "Partcipants more then seats",
                }
            }
    # Constraint Python
    @api.constrains('partner_ids','user_id')
    def _check_something(self):
        for record in self:
            partner_user_ids = self.env['res.users'].sudo().search([('partner_id','in',[x.id for x in record.partner_ids])])
            if record.user_id in partner_user_ids:
                raise ValidationError("Instructor cannot be attendess: %s" % record.user_id.partner_id.name)