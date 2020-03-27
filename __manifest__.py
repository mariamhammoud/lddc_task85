{
    'name': "Vendor Sequence",
    'version': '13.0.1.0.0',
    'summary': """Unique Customer Code""",
    'description': """
       Each customer have unique number code, Odoo 13, Odoo
    """,
    'author': 'Mariam Hammoud',
    'company': 'Azkatech',
    'website': "https://website.com/",
    'category': 'Sales',
    'depends': ['base','sale'],
    'data': [
        'views/res_partner_fom.xml',
        'views/form_settings_with_vendor_reference.xml',
        #'security/ir.model.access.csv',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False
}
