// Copyright (c) 2016, DGSOL InfoTech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transformers', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		cur_frm.set_query("tr_location", function() {
			return {
				"filters": {
					"fl_customer": frm.doc.tr_customer
				}
			}
		})
	}
});

