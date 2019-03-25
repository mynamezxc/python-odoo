# *-* encoding= utf-8 *-*
#  * @Author: Mynamezxc 
#  * @Date: 2019-03-22 16:35:35 
#  * @Last Modified by:   Mynamezxc 
#  * @Last Modified time: 2019-03-22 16:35:35 

{
    "name": "TS24 visitor",
    "summary":
    """
    Create and control all visitor into your company
    """,
    "version": "1.0",
    "author": "TS24 Corp",
    "maintainer": "Mynamezxc (Nguyen Hoang Nguyen)",
    "category": "Visitor",
    "depends": ['base'],
    'data': [
        'views/visitor.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    "qweb": [],
    "installable": True,
    "application": True
}