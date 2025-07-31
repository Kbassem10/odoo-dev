from odoo import models, fields, api

class UserInfo(models.Model):
    _name = 'custom.userinfo'
    _description = 'User Info Form'

    user_id = fields.Many2one('res.users', string='User', required=True, default=lambda self: self.env.user)
    name = fields.Char(required=True)
    email = fields.Char(required=True)
    age = fields.Integer()
    birthdate = fields.Date()
    register_date = fields.Datetime(default=fields.Datetime.now)
    fav_color = fields.Char()
    fav_number = fields.Integer()

    @api.model
    def create(self, vals):
        vals['user_id'] = self.env.user.id
        return super(UserInfo, self).create(vals)
