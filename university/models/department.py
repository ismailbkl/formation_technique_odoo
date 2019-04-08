# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityDepatment(models.Model):
    _name = 'university.depatment'

    name = fields.Char()
    code = fields.Char()
