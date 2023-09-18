from odoo import models, fields, api, _


class CipAttendance(models.Model):
    _name = 'logic.cip.attendance'
    _description = 'Cip Attendance'

    name = fields.Char('Name')
    cip_id = fields.Many2one('logic.cip.form', string='Cip')
    grade = fields.Selection([
        ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
    ], string='Grade')
    project_submit = fields.Boolean('Project Submitted')
    certificate_submit = fields.Boolean('Certificate Submitted')
    state = fields.Selection([
        ('draft', 'Draft'), ('scheduled', 'Scheduled'), ('started', 'Started'), ('project', 'Project'),
        ('certificate', 'Certificate'), ('completed', 'Completed'),
    ], default='draft')
