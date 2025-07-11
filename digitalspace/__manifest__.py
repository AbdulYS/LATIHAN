# -*- coding: utf-8 -*-
{
    'name': "Digital Space",

    'summary': """
        Addons Training""",

    'description': """
        Module training technical odoo16 community
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/course.xml',
        'views/menu.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/teacher_level.xml',
        'views/user.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
