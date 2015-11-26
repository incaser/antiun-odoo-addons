# -*- coding: utf-8 -*-
# (c) 2015 Antiun Ingeniería S.L. - Sergio Teruel
# (c) 2015 Antiun Ingeniería S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "Website Portal Supplier Home",
    'summary': "Show custom home page by supplier",
    'category': 'Website',
    'version': '8.0.1.0.0',
    'depends': [
        'website_portal',
        # 'website_portal_purchase',
    ],
    'data': [
        # 'data/left_menu.xml',
        'views/pages.xml',
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
}