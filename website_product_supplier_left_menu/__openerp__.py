# -*- coding: utf-8 -*-
# (c) 2015 Antiun Ingeniería S.L. - Sergio Teruel
# (c) 2015 Antiun Ingeniería S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "Website Product Supplier Left Menu",
    'summary': "New layout to show products options into left menu",
    'category': 'Website',
    'version': '8.0.1.0.0',
    'depends': [
        'website_product_supplier',
        'website_portal_left_menu',
    ],
    'data': [
        'views/website_product_supplier.xml',
        'views/website_portal_left_menu_layout.xml',
    ],
    'qweb': [
    ],
    'js': [
    ],
    'author': 'Antiun Ingeniería S.L., '
              'Incaser Informatica S.L., ',
    'website': 'http://www.antiun.com',
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': True,
}
