# *-* encoding= utf-8 *-*
#  * @Author: Mynamezxc 
#  * @Date: 2019-03-22 16:35:35 
#  * @Last Modified by:   Mynamezxc 
#  * @Last Modified time: 2019-03-22 16:35:35 
from odoo import api, fields, models

class Category(models.Model):
    _name        = "ts24_module.category"
    _description = "Category of posts"
    _rec_name    = "name"

    name         = fields.Char("Category name", translate=True, size=300)
    description  = fields.Text("Description", help="Write your description for this category")

class Author(models.Model):
    _name        = "ts24_module.author"
    _description = "Author of post"
    _rec_name    = "signature"

    name         = fields.Char("Name", translate=True, size=200)
    signature    = fields.Char("Signature", translate=True, size=200)
    post_list    = fields.One2many("Posts", comodel_name="ts24_module.post")

class Post(models.Model):
    _name        = "ts24_module.post"
    _description = "Add, edit, delete your Posts"

    name         = fields.Char("Visitor name", required=True)
    description  = fields.Text("Description")
    author       = fields.Many2one("Author", comodel_name="ts24_module.author")
    category     = fields.Many2one("Category", comodel_name="ts24_module.category")
    post_type = fields.Selection(string="Type of post", selection=[
        ("normal", "Normal"),
        ("single_page", "Single page"),
        ("form_page", "Form page")
    ])
    content      = fields.Html("Content", required=True)
