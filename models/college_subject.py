from odoo import models, fields
class CollegeSubject(models.Model):
    _name="college.subject"
    _description="College Subject"
    _rec_name='subject_name'


    subject_name = fields.Char(string="Subject Name", required=True)
    subject_code = fields.Char(string="Subject Code", required=True)
    semester =fields.Selection([
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    ], string="Semester", required=True)
    subject_type=fields.Selection([
        ('practical','Practical'),
        ('theory', 'Theory'),
        ('lab', 'Lab')
    ],string="Subject Type", required=True)
    credit =fields.Integer(string="Credits",required=True)
    department = fields.Many2one('college.department', string="Department", required=True)
    course = fields.Many2one('student.course', string="Course")
    assigned_faculty = fields.Many2many('college.staff', string="Assigned Faculty", required=True)
