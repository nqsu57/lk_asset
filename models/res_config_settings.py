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


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # default_method: _default_<field_name>, _selection_<field_name>

    # fields

    # compute and search methods: _compute_<field_name>, _search_<field_name>

    # constrains and onchange methods: _onchange_<field_name>, _check_<constraint_name>

    # CRUD methods (odoo methods: read, create, write, unlink, copy)

    # action methods: button in view
    def set_values(self):
        """ Store configuration values, usually we store configuration data to res.company (odoo use multiple company).
            Or we can store data to ir.config_parameter (table with key-value pairs) or other model
        """
        super(ResConfigSettings, self).set_values()

    # business methods: @api.model
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        # get values and display
        return res
