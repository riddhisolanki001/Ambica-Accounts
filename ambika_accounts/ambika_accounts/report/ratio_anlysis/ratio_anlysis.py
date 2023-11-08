import frappe
import frappe
from frappe import _

from erpnext.accounts.utils import get_balance_on,get_fiscal_year

def execute(filters=None):
    filters = frappe._dict(filters or {})
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    columns = [
 
        {
            "label": _("Ratio"),  # Added column for the ratio
            "fieldtype": "Data",
            "fieldname": "ratio",
            "width": 100,
        },
        {
            "label": _("Purpose"),  # Added column for the ratio
            "fieldtype": "Data",
            "fieldname": "purpose",
            "width": 100,
        },
        {
            "label": _("Defination"),  # Added column for the ratio
            "fieldtype": "Data",
            "fieldname": "defination",
            "width": 100,
        },
        {
            "label": _("Balance"),  # Added column for the ratio
            "fieldtype": "Float",
            "fieldname": "balance",
            "width": 100,
        }
    ]
    return columns

def get_data(filters):

    fiscal_year = get_fiscal_year(fiscal_year=filters.get("fiscal_year"))
    print(fiscal_year)
    # Filter accounts based on your specific conditions (e.g., account type, account name, etc.)
    accounts = [{"name": "1100-1600 - Current Assets - SD"}, {"name": "2100-2400 - Current Liabilities - SD",}]
    current_assets_balance = get_balance_on(accounts[0]["name"],fiscal_year=filters.fiscal_year)
    current_liabilities_balance = get_balance_on(accounts[1]["name"],fiscal_year=filters.fiscal_year)
    print(current_assets_balance)
    print( current_liabilities_balance)

    # Calculate the ratio and add it to the data
    if current_liabilities_balance != 0:
        ratio = current_assets_balance / current_liabilities_balance
    else:
        ratio = None
        
    data = [
         {
            'ratio': 'Current Ratio',
            'purpose': 'The current ratio indicates a company’s overall liquidity position. It is widely used by banks in making decisions regarding the advancing of working capital credit to their clients.',
            'defination': 'Current Assets / Current Liability',
            'balance':ratio
        }
    ]

    # Append the ratio to the data list
    print(ratio)
    

    return data
