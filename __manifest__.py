# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "LK Asset",  # {tên module}
    'sequence': 121,
    'category': "Asset",  # {tên category. Có thể tự điền hoặc copy từ module khác của odoo}
    'description': """
{mô tả module}.
========================================
""",
    'depends': ['lk_base', 'attachment_indexation'],  # Thêm các module khác cần kế thừa. Luôn kế thừa 2 module này
    'data': [
        # thêm file xml hoặc csv vào đây ngoại trừ file xml trong thư mục static/src/xml/.
        # Luôn thêm menu_views.xml (file quy định menu của chức năng) vào cuối. Ví dụ:
        'security/ir.model.access.csv',
        'data/res.lang.csv',
        'views/web_custom.xml',
        'views/web_custom_templates.xml',
        'views/asset_category_views.xml',
        # luôn để file menu ở cuối cùng
        'views/menu_views.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'external_dependencies': {
        'python': [],  # thư viện python cần sử dụng
    },
    'installable': True,
    'application': True,
}
