# Copyright (c) 2023, khetangroup@gmail.com and contributors
# For license information, please see license.txt
import frappe

# Define the main function for the report
def execute(filters=None):
    # SQL query to count unique voucher numbers for each document type
    sql_query = """
        SELECT DATE(transaction_date) as date,
               COUNT(DISTINCT name) as purchase_orders,
               0 as sales_orders,
			   0 as purchase_invoice,
               0 as sales_invoices
        FROM `tabPurchase Order`
        
        UNION

        SELECT DATE(transaction_date) as date,
               0 as purchase_orders,
               COUNT(DISTINCT name) as sales_orders,
               0 as purchase_invoices,
               0 as sales_invoices
        FROM `tabSales Order`
        

        UNION

        SELECT DATE(posting_date) as date,
               0 as purchase_orders,
               0 as sales_orders,
               COUNT(DISTINCT name) as purchase_invoices,
               0 as sales_invoices
        FROM `tabPurchase Invoice`
        
        UNION

        SELECT DATE(posting_date) as date,
               0 as purchase_orders,
               0 as sales_orders,
               0 as purchase_invoices,
               COUNT(DISTINCT name) as sales_invoices
        FROM `tabSales Invoice`
     
    """

    # Execute the SQL query with filters
    data = frappe.db.sql(sql_query,  as_dict=True)

    # Prepare the result data
    columns = [{"label": "Date", "fieldname": "date", "fieldtype": "Date"}, 
               {"label": "Purchase Orders", "fieldname": "purchase_orders", "fieldtype": "Int"},
               {"label": "Sales Orders", "fieldname": "sales_orders", "fieldtype": "Int"},
               {"label": "Purchase Invoices", "fieldname": "purchase_invoices", "fieldtype": "Int"},
               {"label": "Sales Invoices", "fieldname": "sales_invoices", "fieldtype": "Int"}]

    return columns, data

