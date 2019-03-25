# *-* encoding= utf-8 *-*
#  * @Author: Mynamezxc 
#  * @Date: 2019-03-22 16:35:35 
#  * @Last Modified by:   Mynamezxc 
#  * @Last Modified time: 2019-03-22 16:35:35 

from odoo import api, fields, models

class visitor(models.Model):
    _name        = "ts24_module.visitor"
    _description = "Visitor time block"

    name         = fields.Char(string="Visitor name", required=True)
    card_id      = fields.Char(string="Visit code", required=True)
    checkin_time = fields.Datetime(string="Visited at", required=True)
    leave_time   = fields.Datetime(string="Leaved at")
    is_customer  = fields.Boolean(string="This visitor is customer")