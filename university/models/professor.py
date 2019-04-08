# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfessor(models.Model):
    _name = 'university.professor'

    f_name = fields.Char('Fist name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'), ('female','Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    start_date = fields.Datetime('Start date')
    email = fields.Char()
    phone = fields.Char()