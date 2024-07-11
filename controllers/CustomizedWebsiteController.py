from odoo import http
from odoo.http import request

class CustomizedWebsiteController(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        return request.render('vaults.homepage_template')

    @http.route('/company', type='http', auth='public', website=True)
    def companypage(self, **kwargs):
        return request.render('vaults.company_template')