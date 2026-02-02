from odoo import models, fields, api


class ITSMTicket(models.Model):
    _name = 'itsm.ticket'
    _description = 'ITSM Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _order = 'priority desc, id desc'

    name = fields.Char(required=True, tracking=True)

    description = fields.Text()

    partner_id = fields.Many2one(
        'res.partner',
        string='Requester',
        default=lambda self: self.env.user.partner_id,
        tracking=True
    )


    team_id = fields.Many2one(
        'itsm.team',
        tracking=True
    )

    user_id = fields.Many2one(
        'res.users',
        string='Assigned To',
        tracking=True
    )

    stage_id = fields.Many2one(
        'itsm.stage',
        default=lambda self: self._default_stage(),
        group_expand='_group_expand_stage',
        tracking=True
    )

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Critical')
    ], default='1')

    deadline = fields.Datetime()

    attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Attachments'
    )

    # ---------------------
    access_url = fields.Char('Portal URL', compute='_compute_access_url')

    def _compute_access_url(self):
        for rec in self:
            rec.access_url = f'/my/tickets/{rec.id}'

    @api.model
    def _default_stage(self):
        return self.env['itsm.stage'].search([], limit=1)

    def _group_expand_stage(self, stages, domain, order):
        return self.env['itsm.stage'].search([])
