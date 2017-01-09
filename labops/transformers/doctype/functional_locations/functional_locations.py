# -*- coding: utf-8 -*-
# Copyright (c) 2015, DGSOL InfoTech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class FunctionalLocations(Document):
	def validate(self):
		self.check_mandatory_fields()

	def check_mandatory_fields(self):
		if (not self.fl_cd):
			frappe.throw(_("Location Code is Mandatory... Provide Customer given value or Type unique value to identify it"), frappe.MandatoryError)

		if ((not self.fl_fl) or (not self.fl_ss)):
			frappe.throw(_("Substation and Fuctional Location is Mandatory... Provide value"), frappe.MandatoryError)
		elif (not self.fl_plant):
			self.fl_loc_desc = generate_fl_loc_desc(self.fl_fl, self.fl_ss)
		else:
			self.fl_loc_desc = generate_fl_loc_desc(self.fl_fl, self.fl_ss, self.fl_plant)


# Supporting Functions for Class FunctionalLocations

def generate_fl_loc_desc(fl, ss, plant=str('')):
	if (not plant):
		return ss.strip().upper() + "_" + fl.strip().upper()
	else:
		return plant.strip().upper() + "_" + ss.strip().upper() + "_" + fl.strip().upper()

