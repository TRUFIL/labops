# -*- coding: utf-8 -*-
# Copyright (c) 2015, DGSOL InfoTech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Transformers(Document):
	def validate(self):
		self.check_mandatory_fields()
		self.generate_tr_model()

	def check_mandatory_fields(self):
		if (self.tr_category == "DRUM"):
			self.tr_hv = self.tr_lv = self.tr_lv2 = self.tr_rating = self.tr_rating2 = 0
			self.tr_no_of_phases = ""
		else:
			if (not self.tr_serial_no):
				frappe.throw(_("Serial No is Mandatory... Provide value"), frappe.MandatoryError)
			
			if (not self.tr_rating):
				frappe.throw(_("Primary Rating is Mandatory... Provide value"), frappe.MandatoryError)

			if ((not self.tr_hv)):
				frappe.throw(_("Primary HV is Mandatory... Provide values"), frappe.MandatoryError)

			if (not self.tr_no_of_phases):
				frappe.throw(_("Please select No of phases..."), frappe.MandatoryError)

	def generate_tr_model(self):
		if (self.tr_category == 'DRUM'):
			self.tr_model = "DRUM"
		else:
			if (self.tr_rating // 1000 > 0):
				rating = str(round((self.tr_rating / 1000), 3)) + " MVA"
			else:
				rating = str(self.tr_rating) + " kVA"

			if (self.tr_lv):
				vratio = str(self.tr_hv) + "/" + str(self.tr_lv) + " Volts"
			else:
				vratio = str(self.tr_hv) + " Volts"

			self.tr_model = (rating + "_" + vratio + "_" + self.tr_no_of_phases)
