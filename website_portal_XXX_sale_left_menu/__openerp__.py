# -*- coding: utf-8 -*-
# (c) 2015 Antiun Ingeniería S.L. - Sergio Teruel
# (c) 2015 Antiun Ingeniería S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "Website Portal Menu Left",
    'summary': "New layout to show left menu",
    'category': 'Website',
    'version': '8.0.1.0.0',
    'depends': [
        'website',
    ],
    'external_dependencies': {},
    'data': [
        'views/layout.xml',
        'views/pages.xml',
        'data/left_menu.xml',
        'views/website_product_supplier_view.xml',
        'views/website_portal_purchase_view.xml',
    ],
    'qweb': [
    ],
    'js': [
    ],
    'author': 'Antiun Ingeniería S.L., '
              'Incaser Informatica S.L., ',
    'website': 'http://www.antiun.com',
    'license': 'AGPL-3',
    'demo': [],
    'test': [],
    'installable': True,
    # 'auto_install':False,
    # 'application':False,
}
