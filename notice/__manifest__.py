{
    'name': 'Legal Notice',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Module to manage legal notices',
    'description': """
        This module allows you to manage legal notices including recording details and tracking progress.
    """,
    'author': 'Mughal',
    'sequence': -100,
    'category': 'Extra Tools',
    'depends': ['base', 'mail'],  # Include 'mail' for tracking
    'data': [
        'security/ir.model.access.csv',
        'views/legal_notice_views.xml',
        'views/legal.xml',
        # Add other data files or XML files if needed
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
}
