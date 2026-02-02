from odoo import models, fields


class ITSMTeam(models.Model):
    _name = 'itsm.team'
    _description = 'ITSM Team'

    name = fields.Char(required=True)

    manager_id = fields.Many2one(
        'res.users',
        string='Manager'
    )

    member_ids = fields.Many2many(
        'res.users',
        string='Members'
    )
