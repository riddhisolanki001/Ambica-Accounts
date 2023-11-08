// Copyright (c) 2023, Riddhi and contributors
// For license information, please see license.txt

frappe.query_reports["Ratio Anlysis"] = {


	"filters": [
		{
			fieldname:"company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company")
		},
		{
			fieldname:"date",
			label: __("Date"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
			
		},
		{
			fieldname:"fiscal_year",
			label: __("Fiscal Year"),
			fieldtype: "Link",
			options:'Fiscal Year',
			
			
		},
	]

}