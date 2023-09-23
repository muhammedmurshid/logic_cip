{
    'name': "CIP",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'mail', 'logic_payments', 'faculty'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/cip_form.xml',
        'data/activity.xml',
        'views/excel_faculty_payment.xml',
        'views/payment_source.xml',
    ],

    'demo': [],
    'summary': "cip/excel_module",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}
