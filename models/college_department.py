
# -*- coding: utf-8 -*-

from odoo import fields,models

class CollegeDepartment(models.Model):
    _name= 'college.department'
    _description= 'college department'

    name = fields.Char(string="Name",required=True)
