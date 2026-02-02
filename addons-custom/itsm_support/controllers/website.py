from odoo import http
from odoo.http import request
import base64


class ITSMWebsite(http.Controller):

    # -------------------------
    # Show form
    # -------------------------
    @http.route('/support', type='http', auth='public', website=True)
    def support_form(self, **kw):
        teams = request.env['itsm.team'].sudo().search([])
        return request.render(
            'itsm_support.support_form_template',
            {'teams': teams}
        )


    # -------------------------
    # CREATE TICKET (MISSING)
    # -------------------------
    @http.route(
        '/support/create',
        type='http',
        auth='public',
        website=True,
        methods=['POST'],
        csrf=True
    )
    def support_create(self, **post):

        name = post.get('name')
        email = post.get('email')
        subject = post.get('subject')
        description = post.get('description')
        team_id = post.get('team_id')

        partner = request.env['res.partner'].sudo().search(
            [('email', '=', email)], limit=1
        )

        if not partner:
            partner = request.env['res.partner'].sudo().create({
                'name': name,
                'email': email,
            })

        subject = post.get('subject')

        ticket = request.env['itsm.ticket'].sudo().create({
            'subject': subject,        # ⭐ REQUIRED
            'description': description,
            'partner_id': partner.id,
            'team_id': int(team_id) if team_id else False,
        })


        # attachment
        file = request.httprequest.files.get('attachment')
        if file:
            request.env['ir.attachment'].sudo().create({
                'name': file.filename,
                'datas': base64.b64encode(file.read()),
                'res_model': 'itsm.ticket',
                'res_id': ticket.id,
            })

        return request.redirect('/support/thanks')


    # -------------------------
    # Thank you page
    # -------------------------
    @http.route('/support/thanks', type='http', auth='public', website=True)
    def support_thanks(self, **kw):
        return request.render('itsm_support.support_thanks_template')
