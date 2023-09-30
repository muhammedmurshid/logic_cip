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
        ('draft', 'Draft'), ('scheduled', 'Scheduled'), ('excel_started', 'Excel Started'),
        ('excel_completed', 'Excel Completed'), ('cip', 'CIP'), ('cip_started', 'CIP Started'), ('project', 'Project'),
        ('certificate', 'Certificate'), ('completed', 'Completed'),
    ], default='draft')
    day_one_cip_attendance = fields.Selection([
        ('full_day', 'Full Day'), ('half_day', 'Half Day'), ('absent', 'Absent')
    ], string='Day One')
    day_two_cip_attendance = fields.Selection([
        ('full_day', 'Full Day'), ('half_day', 'Half Day'), ('absent', 'Absent')
    ], string='Day Two')
    day_three_cip_attendance = fields.Selection([
        ('full_day', 'Full Day'), ('half_day', 'Half Day'), ('absent', 'Absent')
    ], string='Day Three')

    stud_attendance = fields.Float(string="Attendance",compute="_compute_stud_attendance")
    
    def _compute_stud_attendance(self):
        for record in self:
            total_present = 0
            if record.day_one_cip_attendance=="full_day":
                total_present+=1
            elif record.day_one_cip_attendance=="half_day":
                total_present+=0.5

            if record.day_two_cip_attendance=="full_day":
                total_present+=1
            elif record.day_two_cip_attendance=="half_day":
                total_present+=0.5

            if record.day_three_cip_attendance=="full_day":
                total_present+=1
            elif record.day_three_cip_attendance=="half_day":
                total_present+=0.5
            record.stud_attendance = total_present

    day_one_check = fields.Boolean('Day One')
    day_two_check = fields.Boolean('Day Two')
    day_three_check = fields.Boolean('Day Three')
    student_id = fields.Integer()
