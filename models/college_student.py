# -*- coding: utf-8 -*-

from odoo import fields, models, api

class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student"

    name = fields.Char(string="Name", required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    ],string="Gender",required=True)
    mobile = fields.Char(string="mobile No.")
    department = fields.Many2one('college.department', string="Department")
    hobbies = fields.Many2many('student.hobbies', string="Hobbies")
    state = fields.Selection([
        ('joining','Joining'),
        ('active','Active'),
        ('inactive','Inactive'),
    ],string="State", default="joining")
    fees = fields.Float(string="Fees")


    def action_confirm(self):
        if self.state == 'joining':
            self.state = 'active'
        else:self.state='inactive'

    # def _compute_fees(self):
    #     result = self.env['college.fees'].search([])
    #
    #     student_dep = self.department
    #     for rec in result:
    #         if rec.department == student_dep:
    #             self.fees = rec.amount
    #             break
    #         else:
    #             self.fees = 1000

    @api.onchange('department')
    def _onchange_student_depart(self):
        print('_onchange_student_depart=============')
        result = self.env['college.fees'].search([])
        student_dep = self.department
        for rec in result:
            if rec.department == student_dep:
                self.fees = rec.amount
                break
            else:
                self.fees = 1000