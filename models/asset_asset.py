# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# -- Purpose: Quan ly tai san
# -- Create date: 1/12/2022
# -- Author: Ngo Quoc Su
# -- Update date
# -- Update by
# -- Update content

# imports of python lib

# imports of odoo
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression

# imports of odoo modules


class AssetCategory(models.Model):
    # private attributes
    _name = 'asset.asset'
    _rec_name = 'asset_name'
    _order = 'create_date desc'

    # default_method: _default_<field_name>, _selection_<field_name>

    # fields
    asset_code = fields.Char('Mã tài sản', required=1)
    asset_name = fields.Char('Tên tài sản', required=1)
    asset_type = fields.Selection([('TSCDHH', 'Tài sản cố định hữu hình'), ('TSCDVH', 'Tài sản cố định vô hình')],
                                  string='Loại tài sản', required=1)
    asset_category_id = fields.Many2one('asset.category', 'Danh mục tài sản', required=1)
    asset_origin = fields.Char('Xuất xứ')
    asset_year_of_manufacture = fields.Char('Năm sản xuất')
    asset_year_put_into_use = fields.Char('Năm đưa vào sử dụng')
    asset_use_room = fields.Char('Phòng sử dụng')
    asset_user = fields.Char('Người sử dụng')
    asset_amount = fields.Char('Số lượng/Diện tích (m vuông)')
    asset_price = fields.Integer('Nguyên giá')
    asset_current = fields.Char('Số lượng hiện có')
    asset_used = fields.Char('Số lượng sử dụng')
    asset_remaining = fields.Char('Số lượng còn lại')
    asset_note = fields.Char('Ghi chú')

    # compute and search methods: _compute_<field_name>, _search_<field_name>

    # constrains and onchange methods: _onchange_<field_name>, _check_<constraint_name>
    # constrains nếu sử dụng search là phải có sudo() để không sót ir.rule, các hàm raise cũng phải kiểm tra
    @api.constrains('asset_code')
    def _check_code_unique(self):
        asset_code_counts = self.search_count([('asset_code', '=', self.asset_code),
                                               ('id', '!=', self.id)
                                               ])
        if asset_code_counts > 0:
            raise ValidationError("Mã tài sản đã có")
    # CRUD methods (odoo methods: read, create, write, unlink, copy)
    @api.model
    def create(self, vals):
        # before insert data to database
        res = super(AssetCategory, self).create(vals)
        # after insert data to database, now res is representation for orm record
        return res

    def write(self, vals):
        # before update data to database, orm record with old data
        res = super(AssetCategory, self).write(vals)
        # after update data to database, orm record with new data
        return res

    def unlink(self):
        # before delete data in database
        return super(AssetCategory, self).unlink()

    # action methods: button in view

    # business methods: @api.model
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('asset_code', operator, name), ('asset_name', operator, name)]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ['&'] + domain
        obj = self.search(domain + args, limit=limit)
        return obj.name_get()


    @api.model
    def name_get(self):
        res = []
        for field in self:
            res.append((field.id,  '[{}] - {}'.format(field.asset_category_id.name, field.asset_category_id.code)))
        return res

