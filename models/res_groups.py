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


class ResGroups(models.Model):
    # private attributes
    _inherit = 'res.groups'

    # default_method: _default_<field_name>, _selection_<field_name>

    # fields
    """ We need override / add these fields:
        - is_manager: role of user likes: manager, employee
        - btn_: 
            + using in get_custom_button function: user export data
            + add new odoo group: (ex: approve group to allow user approve data or see custom data in xml)
    Example:
        is_manager = fields.Selection([('manager', 'Manager'), ('factory', 'Factory Admin'), 
                                       ('super', 'IT Superuser')], 'Role', default='manager')
        btn_approve = fields.Boolean('Approve Right')
        btn_survey_export = fields.Boolean("Export Data")
    """
    is_manager = fields.Selection([('staff', 'Cán bộ'), ('manager', 'Quản lý')], 'Vai trò', default='staff')

    # compute and search methods: _compute_<field_name>, _search_<field_name>

    # constrains and onchange methods: _onchange_<field_name>, _check_<constraint_name>

    # CRUD methods (odoo methods: read, create, write, unlink, copy)
    @api.model
    def create(self, vals):
        # before insert data to database
        res = super(ResGroups, self).create(vals)
        # after insert data to database, now res is representation for orm record
        return res

    def write(self, vals):
        # before update data to database, orm record with old data
        res = super(ResGroups, self).write(vals)
        # if use other group, we need reset role
        # if '' in vals:
        #     self.reset_role(self)
        # after update data to database, orm record with new data
        return res

    def unlink(self):
        # before delete data in database
        return super(ResGroups, self).unlink()

    # action methods: button in view

    # business methods: @api.model
    # @api.model
    # def reset_role(self, group):
    #     """ Modify in this module """
    #     pass

    # @api.model
    # def set_ir_rule(self, group):
    #     """ Modify in this module """
    #     pass
