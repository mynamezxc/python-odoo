# *-* encoding= utf-8 *-*
#  * @Author: Mynamezxc 
#  * @Date: 2019-03-22 16:35:35 
#  * @Last Modified by:   Mynamezxc 
#  * @Last Modified time: 2019-03-22 16:35:35 

{
    "name": "TS24 post manager",
    "summary":
    """
    Create and control post, post category, author
    """,
    "version": "1.0",
    "author": "TS24 Corp",
    "maintainer": "Mynamezxc (Nguyen Hoang Nguyen)",
    "category": "Post",
    "depends": ['base'],
    'data': [
        'views/view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    "qweb": [],
    "installable": True,
    "application": True
}