# -*- coding: utf-8 -*-

from odoo import fields,models

class StudentCourse(models.Model):
    _name= 'student.course'
    _description= 'student course'

    name = fields.Char(string="Name",required=True)
