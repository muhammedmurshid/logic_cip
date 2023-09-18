from odoo import models, fields, api, _


class CipForm(models.Model):
    _name = 'logic.cip.form'
    _description = 'Cip Form'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    batch_id = fields.Many2one('logic.base.batch', string='Batch', required=True)
    date = fields.Date('Date', required=True)
    type_of_training = fields.Selection([
        ('cip', 'CIP'), ('excel', 'Excel'),
    ], string='Type of Training')
    trainer_one = fields.Char('Trainer')
    trainer_two = fields.Char('Trainer')
    trainer_three = fields.Char('Trainer')
    state = fields.Selection([
        ('draft', 'Draft'), ('scheduled', 'Scheduled'), ('started', 'Started'), ('project', 'Project'),
        ('certificate', 'Certificate'), ('completed', 'Completed'),
    ], default='draft')
    cip_ids = fields.One2many('logic.cip.attendance', 'cip_id', string='Attendance')
    coordinator_id = fields.Many2one('res.users', string='Coordinator', default=lambda self: self.env.user, readonly=1)

    def action_submit(self):

        self.activity_schedule('logic_cip.mail_cip_activity', user_id=self.coordinator_id.id, date_deadline=self.date,
                               note=f'CIP reminder.')
        self.state = 'scheduled'

    def action_start(self):
        students = self.env['logic.students'].search([('batch_id', '=', self.batch_id.id)])
        abc = []
        unlink_commands = [(3, child.id) for child in self.cip_ids]
        self.write({'cip_ids': unlink_commands})

        for i in students:
            res_list = {
                'name': i.name,

            }
            abc.append((0, 0, res_list))
        self.cip_ids = abc
        for rec in self.cip_ids:
            rec.state = 'started'
        self.state = 'started'
        activity = self.env['mail.activity'].search([('res_id', '=', self.id), (
            'activity_type_id', '=', self.env.ref('logic_cip.mail_cip_activity').id)])
        activity.action_feedback('CIP Started')

    def action_project(self):
        for rec in self.cip_ids:
            rec.state = 'project'
        self.state = 'project'

    def action_certificate(self):
        for rec in self.cip_ids:
            rec.state = 'certificate'
        self.state = 'certificate'

    def action_completed(self):
        for rec in self.cip_ids:
            rec.state = 'completed'
        self.state = 'completed'

    def _compute_display_name(self):
        for rec in self:
            if rec.name:
                rec.display_name = rec.name + ' - ' + rec.batch_id.name
            else:
                rec.display_name = rec.batch_id.name + ' - CIP'
