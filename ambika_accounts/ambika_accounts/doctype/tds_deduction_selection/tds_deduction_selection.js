// Copyright (c) 2023, Riddhi and contributors
// For license information, please see license.txt

frappe.ui.form.on("TDS deduction selection", {
	retrive(frm) {
        var from_date = frm.doc.from_date
        var to_date =  frm.doc.to_date
        var category = frm.doc.category
        var category_name = frm.doc.category_name
        console.log(from_date)
        console.log(to_date)
        console.log(category)
        
      frappe.call({
    method: 'ambika_accounts.ambika_accounts.doctype.tds_deduction_selection.tds_deduction_selection.tds_account',
    args: {
        'category': category,
        'category_name': category_name
    },
    callback: function (r) {
        // Handle the response if needed
        console.log(r.message[5]);
        if (frm.doc.tds_deduction && frm.doc.tds_deduction.length === 0) {
       frm.add_child("tds_deduction", {
                        'sub_category': r.message[5],
                        'tds_rate': r.message[4],
                        'base_amount': r.message[7],
                        'tds_amount':r.message[3]
                    });
                    frm.refresh_field('tds_deduction');
        frm.add_child("tds_deduction", {
                        'sub_category': r.message[6],
                        'tds_rate': r.message[2],
                        'base_amount': r.message[0],
                        'tds_amount':r.message[1]
                    });
                    frm.refresh_field('tds_deduction');
                }
                }
})
        }
});