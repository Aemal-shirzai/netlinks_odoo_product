# -*- coding: utf-8 -*-
# from odoo import http


# class Netlinks(http.Controller):
#     @http.route('/netlinks/netlinks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/netlinks/netlinks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('netlinks.listing', {
#             'root': '/netlinks/netlinks',
#             'objects': http.request.env['netlinks.netlinks'].search([]),
#         })

#     @http.route('/netlinks/netlinks/objects/<model("netlinks.netlinks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('netlinks.object', {
#             'object': obj
#         })
