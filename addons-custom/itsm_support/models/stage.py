from odoo import models, fields


class ITSMStage(models.Model):
    _name = 'itsm.stage'
    _description = 'Ticket Stage'
    _order = 'sequence'

    color = fields.Selection([
        ('secondary','Gray'),
        ('primary','Blue'),
        ('warning','Orange'),
        ('info','Cyan'),
        ('success','Green'),
        ('danger','Red'),
    ], default='secondary')

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    fold = fields.Boolean(string='Folded in Kanban')
