# -*- coding: utf-8 -*-

from odoo import models, fields


class CollegeStaff(models.Model):
    _name = "college.staff"
    _description = "College Staff"

    name = fields.Char(string="Name", required=True)
    employee_id = fields.Char(string="Employee_ID", required=True)
    date_of_birth = fields.Date(string="Birthday", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    mobile_no = fields.Char(string="Mobile_no.")
     
