from odoo import models, fields, api, _


class ExcelFacultyRecord(models.Model):
    _name = 'excel.faculty.record'
    _description = 'Excel Faculty Record'

    date = fields.Date('Date')
    from_time = fields.Float('From Time')
    to_time = fields.Float('To Time')
    break_reason = fields.Char('Break Reason')
    break_time = fields.Float('Break Time')

    excel_faculty_id = fields.Many2one('logic.cip.form', string='Excel Faculty', ondelete='cascade')

    @api.depends('total_duration', 'from_time', 'to_time', 'break_time')
    def _compute_total_duration(self):
        for record in self:
            if record.from_time and record.to_time:
                record.total_duration = record.to_time - record.from_time - record.break_time
            else:
                record.total_duration = 0.0

    total_duration = fields.Float('Total Duration', compute='_compute_total_duration', store=True)
