# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# -- Purpose:
# -- Create date:
# -- Author:
# -- Update date
# -- Update by
# -- Update content

# imports of python lib

# imports of odoo
from odoo import api, fields, models, _

# imports of odoo modules


class BaseModel(models.AbstractModel):
    # private attributes
    _inherit = 'base'

    # default_method: _default_<field_name>, _selection_<field_name>

    # fields

    # compute and search methods: _compute_<field_name>, _search_<field_name>

    # constrains and onchange methods: _onchange_<field_name>, _check_<constraint_name>

    # CRUD methods (odoo methods: read, create, write, unlink, copy)
    @api.model
    def create(self, vals):
        # before insert data to database
        res = super(BaseModel, self).create(vals)
        # after insert data to database, now res is representation for orm record
        return res

    def write(self, vals):
        # before update data to database, orm record with old data
        res = super(BaseModel, self).write(vals)
        # after update data to database, orm record with new data
        return res

    def unlink(self):
        # before delete data in database
        return super(BaseModel, self).unlink()

    # action methods: button in view

    # business methods: @api.model
    # list of object function needed to set security
    @api.model
    def get_available_function_lst(self):
        """ List of object function (menu) needed to set security.
            Ex: [{'name': _('Dashboard'), 'type': 'view', 'menu_id': 'lk_eep.eep_menu', 'model': '', 'value': ''},
                {'name': _('Lang'), 'type': 'model', 'menu_id': 'lk_eep.res_menu', 'model': 'res.lang', 'value': ''}]
            Params:
                - Type:
                    + View: only allow user see menu or not (report, dashboard)
                    + Model: read, create, update, delete rights
                - Model: model need to check (create, update, delete), work with type = model
                - Value: if one model but has many menu, so we will check based on value (unique name per model).
                        Using with get_available_function.
        """
        return [{'name': _('Người dùng'), 'type': 'model', 'menu_id': 'lk_asset.menu_res_users', 'model': 'res.users',
                 'value': ''},
                {'name': _('Phân quyền'), 'type': 'model', 'menu_id': 'lk_asset.menu_res_groups', 'model': 'res.groups',
                 'value': ''},
                {'name': _('Nhật ký hệ thống'), 'type': 'view', 'menu_id': 'lk_asset.menu_system_log',
                 'model': 'system.log', 'value': ''},
                {'name': _('Sao lưu dữ liệu'), 'type': 'model', 'menu_id': 'lk_asset.menu_backup', 'model': 'db.backup',
                 'value': ''}]

    # list of menu not needed to log: system.log, notification
    # Ex: ['lk_eep.system_log_menu']
    @api.model
    def get_not_log_lst(self):
        return ['lk_asset.menu_system_log']

    # list of menu not needed to check security: system.log, notification
    # Ex: ['lk_eep.system_log_menu']
    @api.model
    def get_not_security_lst(self):
        return ['lk_asset.menu_system_log']

    # list of action not needed to check access through url like wizard, custom button on tree view
    # Ex: ['lk_eep.action_eep_add_user']
    @api.model
    def get_not_check_lst(self):
        return []
