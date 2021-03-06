# -*- coding: utf-8 -*-
{
    'name': "netlinks Product",

    'summary': """
        To add more features to product module""",

    'description': """
        To add more features to product module
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'application': True,
    'sequence': 0,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/menus.xml',
        'views/product_template_views.xml',
        'views/product_group_template_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
