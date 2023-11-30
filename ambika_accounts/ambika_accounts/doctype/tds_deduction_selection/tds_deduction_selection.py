# Copyright (c) 2023, Riddhi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document



class TDSdeductionselection(Document):
	pass

@frappe.whitelist(allow_guest=True)
def tds_account(category,category_name):
    print(category)
    # get category based on selected category .......................
    tds_category = frappe.get_all(
		"Tax Withholding Category", {"category_name": category_name}, "name"
	)
    category_list = [account_info.get("name") for account_info in tds_category]
    first_value=category_list[0]
    second_value = category_list[1]
    print(first_value)
    print(second_value)
    
    
    #get accounts of selected category ......................
    tds_accounts = frappe.get_all(
		"Tax Withholding Account", 
  		filters={"parent":["in",first_value,second_value]},
    	fields=["account"]
	)
    account_list = [account_info.get("account") for account_info in tds_accounts]
    print(account_list)
    
    # get Invoices with First Category Link in it ..............
    first_category= frappe.get_all(
		"Purchase Invoice",
		filters ={"tax_withholding_category": ["in", first_value]},
		fields=['name']

	)
    first_category_invoice_list = [account_info.get("name") for account_info in first_category]
    print(first_category_invoice_list)
    
    
    #get Invoices with Second Category Link in it ...............
    second_category = frappe.get_all(
		"Purchase Invoice",
		filters ={"tax_withholding_category": ["in", second_value]},
		fields=['name']

	)
    second_category_invoice_list = [account_info.get("name") for account_info in second_category]
    print(second_category_invoice_list)
    
    
    
     #get invoices of first category with tds deduction and get base_total ..............
    first_category_purchase_tax = frappe.get_all(
		"Purchase Taxes and Charges",        
		filters={
			"account_head": ["in", account_list],
			"parent":["in",first_category_invoice_list]
    },
      fields=["parent",'rate','tax_amount']
	)
    first_category_transaction = [account_info.get("parent") for account_info in first_category_purchase_tax]
    first_category_rate = [account_info.get("rate") for account_info in first_category_purchase_tax]
    first_category_amount = [account_info.get("tax_amount") for account_info in first_category_purchase_tax]
    print(first_category_transaction)
    print(first_category_rate)
    print(first_category_amount)
    
    
    
    #get base_total of invoices of second category tds deduction 
    first_total = frappe.get_all(
		"Purchase Invoice",
		filters = {
			"name":["in",first_category_transaction]
		},
		fields=["base_total"]
	)
    first_base_total = [account_info.get("base_total") for account_info in first_total]
    first_total_amount = sum(first_base_total)
    
    print(first_total_amount)
    
    
  
    #get invoices of second category with tds deduction and get base_total ..............
    second_category_purchase_tax = frappe.get_all(
		"Purchase Taxes and Charges",        
		filters={
			"account_head": ["in", account_list],
			"parent":["in",second_category_invoice_list]
        },
        fields=["parent",'rate','tax_amount']
	)
    second_category_transaction = [account_info.get("parent") for account_info in second_category_purchase_tax]
    second_category_rate = [account_info.get("rate") for account_info in second_category_purchase_tax]
    second_category_amount = [account_info.get("tax_amount") for account_info in second_category_purchase_tax]
    print(second_category_transaction)
    print(second_category_rate)
    print(second_category_amount)
    
    get_account_second_category = frappe.get_all(
      "Purchase Invoice",
      filters={
        "name":["in",second_category_transaction]
        
      },
      fields=['credit_to','name',]
    )
    print(get_account_second_category)
    
    get_account_first_category = frappe.get_all(
      "Purchase Invoice",
      filters={
        "name":["in",first_category_transaction]
        
      },
      fields=['credit_to','name',]
    )
    get_account_name_second= [account_info.get("credit_to") for account_info in get_account_first_category]
    print(get_account_name_second)
    
    
    
    #get base_total of invoices of second category tds deduction 
    second_total = frappe.get_all(
		"Purchase Invoice",
		filters = {
			"name":["in",second_category_transaction]
		},
		fields=["base_total"]
	)
    second_base_total = [account_info.get("base_total") for account_info in second_total]
    second_total_amount = sum(second_base_total)
    print(second_total_amount)
    
    
    #set in deduction table for first category and second category
    
    if second_category_purchase_tax and first_category_purchase_tax :
          return second_total_amount,second_category_amount,second_category_rate,first_category_amount,first_category_rate,first_value,second_value,first_total_amount
          
                
    
    
   
    
    
    
    
    
    
   