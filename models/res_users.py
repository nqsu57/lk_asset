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


class ResUsers(models.Model):
    # private attributes
    _inherit = 'res.users'

    # default_method: _default_<field_name>, _selection_<field_name>

    # fields

    # compute and search methods: _compute_<field_name>, _search_<field_name>

    # constrains and onchange methods: _onchange_<field_name>, _check_<constraint_name>

    # CRUD methods (odoo methods: read, create, write, unlink, copy)
    @api.model
    def create(self, vals):
        # before insert data to database
        res = super(ResUsers, self).create(vals)
        # after insert data to database, now res is representation for orm record
        return res

    def write(self, vals):
        # before update data to database, orm record with old data
        res = super(ResUsers, self).write(vals)
        # after update data to database, orm record with new data
        return res

    def unlink(self):
        # before delete data in database
        return super(ResUsers, self).unlink()

    # action methods: button in view

    # business methods: @api.model
