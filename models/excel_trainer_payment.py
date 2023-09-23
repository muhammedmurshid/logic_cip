from odoo import models, fields, api, _


class ExcelFacultyPayment(models.Model):
    _name = 'excel.faculty.payment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Excel Faculty Payment'

    excel_payment = fields.Float('Excel Payment')
    faculty_id = fields.Many2one('res.users', string='Faculty')

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = rec.faculty_id.name + ' - ' + str(rec.excel_payment)
