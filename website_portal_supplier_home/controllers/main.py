# -*- coding: utf-8 -*-
# (c) 2015 Antiun Ingeniería S.L. - Sergio Teruel
# (c) 2015 Antiun Ingeniería S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import http
from openerp.http import request

from openerp.addons.website_portal.controllers.main import WebsiteAccount

class WebsitePortalSupplierHome(WebsiteAccount):

    @http.route(['/my/supplier/home'], type='http', auth="user", website=True)
    def supplier_home(self):
        """ Add main supplier home page """
        return request.website.render('website_portal_supplier_home.home_page')

    @http.route(['/my', '/my/home'], type='http', auth='user', website=True)
    def account(self):
        partner = request.env.user.partner_id
        if partner.customer:
            return super(WebsitePortalSupplierHome, self).account()
        else:
            return self.supplier_home()
