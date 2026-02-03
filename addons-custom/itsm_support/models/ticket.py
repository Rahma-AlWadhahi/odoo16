from odoo import models, fields, api


class ITSMTicket(models.Model):
    _name = 'itsm.ticket'
    _description = 'ITSM Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _order = 'priority desc, id desc'


    # =====================================================
    # Ticket Number (sequence)
    # =====================================================
    name = fields.Char(
        string="Ticket Number",
        required=True,
        copy=False,
        readonly=True,
        default="New",
        tracking=True,
    )


    # =====================================================
    # Human title
    # =====================================================
    subject = fields.Char(
        string="Title",
        required=True,
        tracking=True,
    )


    description = fields.Text()


    # =====================================================
    # Relations
    # =====================================================
    partner_id = fields.Many2one(
        'res.partner',
        string='Requester',
        default=lambda self: self.env.user.partner_id,
        tracking=True
    )
    partner_email = fields.Char(
        related='partner_id.email',
        store=True,
        readonly=True
    )
    partner_phone = fields.Char(
        related='partner_id.phone',
        store=True,
        readonly=True
    )
    partner_mobile = fields.Char(
        related='partner_id.mobile',
        store=True,
        readonly=True
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


    # =====================================================
    # Priority
    # =====================================================
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Critical')
    ], default='1')


    deadline = fields.Datetime()


    # =====================================================
    # Attachments (Odoo standard way)
    # =====================================================
    attachment_ids = fields.One2many(
        'ir.attachment',
        'res_id',
        string='Attachments',
        domain="[('res_model', '=', 'itsm.ticket')]"
    )


    # =====================================================
    # Portal
    # =====================================================
    access_url = fields.Char(
        'Portal URL',
        compute='_compute_access_url'
    )


    def _compute_access_url(self):
        for rec in self:
            rec.access_url = f'/my/tickets/{rec.id}'


    # =====================================================
    # Defaults
    # =====================================================
    @api.model
    def _default_stage(self):
        stage = self.env['itsm.stage'].search([], limit=1)
        return stage.id if stage else False


    def _group_expand_stage(self, stages, domain, order):
        return self.env['itsm.stage'].search([])


    # =====================================================
    # SEQUENCE (IMPORTANT PART)
    # =====================================================
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('itsm.ticket') or 'New'
        return super().create(vals)
