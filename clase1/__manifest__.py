# -*- coding: utf-8 -*-
{
    'name': "clase1",

    'summary': """
        Mi primera clase""",

    'description': """
        Para aprender cosas nuevas
    """,

    'author': "Stephania",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Clase'
    'version': '3.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/vista_clase.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
     #   'demo/demo.xml',
    ],
}
