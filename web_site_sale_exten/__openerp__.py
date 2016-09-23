{
    'name': 'eCommerce Extension to Display Stock Info',
    'category': 'Website',
    'summary': 'Sell Your Products Online with Product Stock Info',
    'website': 'http://www.credativ.in',
    'version': '1.0',
    'description': """
OpenERP E-Commerce
==================

        """,
    'author': 'Murali Krishna Reddy',
    'depends': ['website_sale','stock'],
    'images':['images/websale1.png'],
    'data': [
        'views/templates.xml',
    ],
    'demo': [
    ],
    #'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
