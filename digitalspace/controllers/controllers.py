# -*- coding: utf-8 -*-
# from odoo import http


# class Digitalspace(http.Controller):
#     @http.route('/digitalspace/digitalspace', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/digitalspace/digitalspace/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('digitalspace.listing', {
#             'root': '/digitalspace/digitalspace',
#             'objects': http.request.env['digitalspace.digitalspace'].search([]),
#         })

#     @http.route('/digitalspace/digitalspace/objects/<model("digitalspace.digitalspace"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('digitalspace.object', {
#             'object': obj
#         })
