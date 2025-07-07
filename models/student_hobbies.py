# -*- coding: utf-8 -*-

from odoo import fields,models

class StudentHobbies(models.Model):
    _name= 'student.hobbies'
    _description= 'student hobbies'

    name = fields.Char(string="Name",required=True)
