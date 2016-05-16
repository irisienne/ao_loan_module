# -*- coding: utf-8 -*-
{
    'name': 'agilorg loan managment',
    'version': '1.0.0',
    'category': 'lone managment',
    'sequence': 3,
    'author': 'rahma',
    'description': """
    """,
    'depends' : ['hr', 'payroll_AgilOrg'],
    'data': [
        'sequences/hr_loan_sequence.xml',
        'views/hr_loan_view.xml',
        'views/workflow.xml',
#        'views/board_hr_loan_statistical_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
