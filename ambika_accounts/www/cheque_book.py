import frappe

# @frappe.whitelist()
# def cheque_number():
#     # Fetch the last 'tabCheque Book' record
#     last_cheque_record = frappe.get_last_doc('Cheque Book')
#     last_payment_record = frappe.get_last_doc('Payment Entry')
#     print("/n/n/n/n/n/n/n")
#     print(last_cheque_record.last_no)
#     print(int(last_payment_record.reference_no)+1)

#     if last_cheque_record.last_no == str(int(last_payment_record.reference_no)+1):
#         frappe.msgprint(f"Last Payment Record hiiiii: {str(last_cheque_record.reference_no)}")
         
#     else:
#         frappe.msgprint(f"Last Payment Record: {str(last_payment_record)}")
#         new_last_no = int(last_payment_record.reference_no) + 1
#         return new_last_no

@frappe.whitelist()
# def cheque_number():
#     # Fetch the last 'tabCheque Book' record
#     last_cheque_record = frappe.get_last_doc('Cheque Book')
#     last_payment_record = frappe.get_last_doc('Payment Entry')

#     print("\n\n\n\n\n\n\n")
#     print(last_cheque_record.last_no)
#     x=int(last_payment_record.reference_no) + 1
#     print(x)

#     if last_cheque_record.last_no == str(x):
#         frappe.msgprint(f"Last Payment Record: {str(last_cheque_record.reference_no)}")
        
#     else:
#         frappe.msgprint(f"Last Payment Record: {str(last_payment_record)}")
#         new_last_no = int(last_payment_record.reference_no) + 1
#         frappe.msgprint(f"New Last Number: {new_last_no}")

  
#     return new_last_no
def cheque_number():
    # Fetch the last 'tabCheque Book' record
    last_cheque_record = frappe.get_last_doc('Cheque Book')
    last_payment_record = frappe.get_last_doc('Payment Entry')

    print("\n\n\n\n\n\n\n")
    print(last_cheque_record.last_no)
    x = last_payment_record.reference_no
    print(x)

    new_last_no = None 

    if last_cheque_record.last_no == str(x):
        frappe.msgprint(f"Last Payment Record: {str(last_cheque_record.reference_no)}")
        
    else:
        frappe.msgprint(f"Last Payment Record: {str(last_payment_record)}")
        new_last_no = int(last_payment_record.reference_no) + 1
        frappe.msgprint(f"New Last Number: {new_last_no}")

    return new_last_no

# @frappe.whitelist()
# def cheque_number():
#     # Fetch the last 'tabCheque Book' record
#     last_cheque_record = frappe.get_last_doc('Cheque Book')
#     last_payment_record = frappe.get_last_doc('Payment Entry')

#     print("\n\n\n\n\n\n\n")
#     print(last_cheque_record.last_no)
#     x = int(last_payment_record.reference_no) + 1

#     # Initialize new_last_no to x
#     new_last_no = x

#     if last_cheque_record.last_no == str(x):
#         frappe.msgprint(f"Last Payment Record: {str(last_cheque_record.reference_no)}")
#     else:
#         frappe.msgprint(f"Last Payment Record: {str(last_payment_record)}")
#         # Modify new_last_no in the else block if needed
#         new_last_no = int(last_payment_record.reference_no) + 1
#         frappe.msgprint(f"New Last Number: {new_last_no}")

#     # Move the return statement outside the if-else block
#     return new_last_no

# import frappe
# from frappe import _
# from frappe.model.document import Document


# @frappe.whitelist()
# def cheque_number():
#     # Fetch the last 'Cheque Book' record
#     last_cheque_record = frappe.get_last_doc('Cheque Book')
#     print(last_cheque_record.last_no)
    
#     # print(last_number)
#     last_payment_record = frappe.get_last_doc('Payment Entry')
#     # Fetch the last 'Payment Entry' record
#     # last_reference = frappe.db.get_value('Payment Entry', 'ACC-PAY-2023-00023','reference_no')
#     # print(last_reference)

#     if last_cheque_record.last_no == last_payment_record.reference_no:
#         frappe.msgprint(f"Last Payment Record: ")

#     #     frappe.msgprint(f"Last Payment Record: ")
#     #     return  # This will exit the function if the condition is true
#     # elif last_number != last_reference:
#     #     # frappe.msgprint(f"Last Payment Record: {str(last_payment_record.reference_no)}")
#     #     new_last_no = int(last_payment_record.reference_no) + 1
#     #     frappe.msgprint(f"New Last Number: {new_last_no}")
#     # return new_last_no

