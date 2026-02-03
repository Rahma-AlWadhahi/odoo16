from odoo import models, fields, api


class ITSMTeam(models.Model):
    _name = 'itsm.team'
    _description = 'ITSM Team'

    name = fields.Char(required=True)

    manager_id = fields.Many2one(
        'res.users',
        string='Manager'
    )

    leader_id = fields.Many2one(
            'res.users',
            string='Team Leader',
            required=True,
            tracking=True
        )
    
    member_ids = fields.Many2many(
        'res.users',
        string='Members'
    )

    @api.onchange('leader_id')
    def _onchange_leader(self):
        if self.leader_id and self.leader_id not in self.member_ids:
            self.member_ids = [(4, self.leader_id.id)]

