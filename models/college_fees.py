# -*- coding: utf-8 -*-

from odoo import models, fields


class CollegeFees(models.Model):
    _name = "college.fees"
    _description = "College Fees"

    amount = fields.Float(string="Amount", required=True)
    department = fields.Many2one('college.department',string="Department", required=True)


