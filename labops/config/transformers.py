from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Transformers"),
			"items": [
				{
					"type": "doctype",
					"name": "Functional Locations",
					"description": _("List of Functional Locations."),
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
