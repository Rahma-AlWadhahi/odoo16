{
    'name': 'ITSM Support',
    'version': '16.0.1.0.0',
    'summary': 'Simple ITSM / Ticket system',
    'category': 'Services',
    'author': 'Rahma Al-Wadhahi',
    'depends': ['base', 'mail', 'portal', 'website'],
    'data': [
        'security/itsm_groups.xml',
        'security/itsm_security.xml',
        'security/ir.model.access.csv',
        'security/itsm_rules.xml',
        'data/sequence.xml',
        'data/stage_data.xml',

        'views/portal_templates.xml',
        'views/website_templates.xml',
        'views/ticket_views.xml',
        'views/team_views.xml',
        'views/stage_views.xml',
        'views/menus.xml',

    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
