# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'author': 'ADHOC SA',
    'auto_install': False,
    'installable': True,
    'category': 'Sale',
    'demo_xml': [
    ],
    'depends': [
        'product',
    ],
    'description': """
Product Internal Code
=====================
""",
    'license': 'AGPL-3',
    'name': u'Product Internal Code',
    'test': [],
    'data': [
        'product_view.xml',
        'product_data.xml',
    ],
    'demo': [
        'demo/product.template.csv',
        'demo/product.product.csv'],
    'version': '1.1',
    'website': 'www.adhoc.com.ar',
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
