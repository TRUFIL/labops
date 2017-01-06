# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Laboratory Operations",
			"color": "#3498db",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Lab Operations")
		},
		{
			"module_name": "Sample Management",
			"color": "yellow",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Sample Management")
		},
		{
			"module_name": "Transformers",
			"color": "yellow",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Transformers")
		}
	]
