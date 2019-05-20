# -*- coding: utf-8 -*-

{
    'name' : 'Odoo :Currency Rate',
    'version' : '1.0',
    'depends' : [
        'base',
        'account',
        'purchase',
        'purchase_requisition_for_sales',
        'core_update',
    ],
    'author' : 'Bozz',
    'category': 'Bozz',
    'description': """
        Module Purchase to invoice
            - set currency rate in vendor bill
            - onchange currency rate
    """,
    'website': '',
    'data': [
        'views/account_invoice_view.xml',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'images': [],
}
