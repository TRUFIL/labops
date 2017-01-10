from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "Functional Locations",
					"description": _("List of Functional Locations."),
				},
				{
					"type": "doctype",
					"name": "Transformers",
					"description": _("List of Transformers."),
				},
			]
		},
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Transformer Types",
					"description": _("List of Transformer Types."),
				},
			]
		},
	]
