from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class ITSMPotal(CustomerPortal):

    # ---------------------------------------
    # List tickets
    # ---------------------------------------
    @http.route(['/my/tickets'], type='http', auth='user', website=True)
    def portal_my_tickets(self, **kw):

        tickets = request.env['itsm.ticket'].search([
            ('partner_id', '=', request.env.user.partner_id.id)
        ])

        values = {
            'tickets': tickets,
        }

        return request.render(
            'itsm_support.portal_my_tickets',
            values
        )

    # ---------------------------------------
    # Ticket detail
    # ---------------------------------------
    @http.route(['/my/tickets/<int:ticket_id>'], type='http', auth='user', website=True)
    def portal_ticket_detail(self, ticket_id, **kw):

        ticket = request.env['itsm.ticket'].browse(ticket_id)

        if ticket.partner_id != request.env.user.partner_id:
            return request.redirect('/my')

        return request.render(
            'itsm_support.portal_ticket_detail',
            {'ticket': ticket}
        )
