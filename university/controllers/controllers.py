# -*- coding: utf-8 -*-
from odoo import http

# class University(http.Controller):
#     @http.route('/university/university/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/university/university/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('university.listing', {
#             'root': '/university/university',
#             'objects': http.request.env['university.university'].search([]),
#         })

#     @http.route('/university/university/objects/<model("university.university"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('university.object', {
#             'object': obj
#         })