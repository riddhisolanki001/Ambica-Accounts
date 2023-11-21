import frappe


# @frappe.whitelist()
# def cheque_number():
#     query = "SELECT from_no, last_no FROM `tabCheque Book` WHERE last_no >= from_no ORDER BY `creation` DESC LIMIT 1;"

#     # Fetch the record using the query
#     result = frappe.db.sql(query, as_dict=True)
#     x="SELECT name, reference_no FROM `tabPayment Entry` WHERE status = 0 AND docstatus = 1 ORDER BY creation DESC LIMIT 1;"
    
#     if result:
#         last_record = result[0]
#         frappe.errprint(last_record)
#         return frappe._dict(last_record) 
#     else:
#         frappe.errprint("No records found.")
#         return None
# @frappe.whitelist()
# def cheque_number():
#     # Fetch the last record from 'tabCheque Book'
#     cheque_book_query = """
#         SELECT name, from_no, last_no
#         FROM `tabCheque Book`
#         WHERE last_no >= from_no
#         ORDER BY `creation` DESC
#         LIMIT 1;
#     """
#     cheque_book_result = frappe.db.sql(cheque_book_query, as_dict=True)

#     if cheque_book_result:
#         last_cheque_record = cheque_book_result[0]

#         # Fetch the last record from 'tabPayment Entry'
#         payment_entry_query = """
#             SELECT name, reference_no
#             FROM `tabPayment Entry`
#             WHERE status = 0 AND docstatus = 1
#             ORDER BY creation DESC
#             LIMIT 1;
#         """
#         payment_entry_result = frappe.db.sql(payment_entry_query, as_dict=True)

#         if payment_entry_result and last_cheque_record:
#             last_payment_record = payment_entry_result[0]
#             frappe.msgprint(str(last_payment_record))
#             new_last_no = int(last_payment_record['reference_no']) + 1

#             # Update 'tabCheque Book' with the new_last_no value
#             # frappe.db.set_value('Cheque Book', last_cheque_record['name'], 'last_no', new_last_no)

#             # Return the last record from 'tabCheque Book'
#             return new_last_no
#         else:
#             frappe.errprint("No records found in 'tabPayment Entry'.")
#             return None
#     else:
#         frappe.errprint("No records found in 'tabCheque Book'.")
#         return None
@frappe.whitelist()
def cheque_number():
    # Fetch the last record from 'tabCheque Book'
    cheque_book_query = """
        SELECT name, from_no, last_no
        FROM `tabCheque Book`
        WHERE last_no >= from_no
        ORDER BY `creation` DESC
        LIMIT 1;
    """
    cheque_book_result = frappe.db.sql(cheque_book_query, as_dict=True)

    if cheque_book_result:
        last_cheque_record = cheque_book_result[0]

        # Fetch the last record from 'tabPayment Entry'
        payment_entry_query = """
            SELECT name, reference_no
            FROM `tabPayment Entry`
            WHERE status = 0 AND docstatus = 1
            ORDER BY creation DESC
            LIMIT 1;
        """
        payment_entry_result = frappe.db.sql(payment_entry_query, as_dict=True)

        if payment_entry_result and last_cheque_record:
            last_payment_record = payment_entry_result[0]

            # Check if the value of 'reference_no' is equal to 'last_no'
            if last_payment_record['reference_no'] == last_cheque_record['last_no']:
                frappe.msgprint("Value of 'reference_no' is equal to 'last_no'. Breaking the condition.")
                return None

            frappe.msgprint(str(last_payment_record))
            new_last_no = int(last_payment_record['reference_no']) + 1

            # Update 'tabCheque Book' with the new_last_no value
            # frappe.db.set_value('Cheque Book', last_cheque_record['name'], 'last_no', new_last_no)

            # Return the last record from 'tabCheque Book'
            return new_last_no
        else:
            frappe.errprint("No records found in 'tabPayment Entry'.")
            return None
    else:
        frappe.errprint("No records found in 'tabCheque Book'.")
        return None

# @frappe.whitelist()
# def cheque_number():
#     # Fetch the last record from 'tabCheque Book'
#     cheque_book_query = """
#         SELECT name, from_no, last_no
#         FROM `tabCheque Book`
#         WHERE last_no <= from_no
#         ;
#     """
#     cheque_book_result = frappe.db.sql(cheque_book_query, as_dict=True)

#     print("Cheque Book Result:", cheque_book_result)

#     if cheque_book_result:
#         last_cheque_record = cheque_book_result[0]

#         # Fetch the last record from 'tabPayment Entry'
#         payment_entry_query = """
#             SELECT name, reference_no
#             FROM `tabPayment Entry`
#             WHERE status = 0 AND docstatus = 1
#             ORDER BY creation DESC
#             LIMIT 1;
#         """
#         payment_entry_result = frappe.db.sql(payment_entry_query, as_dict=True)

#         print("Payment Entry Result:", payment_entry_result)

#         if payment_entry_result and last_cheque_record:
#             last_payment_record = payment_entry_result[0]
#             frappe.msgprint(str(last_payment_record))
#             new_last_no = int(last_payment_record['reference_no']) + 1

#             # Update 'tabCheque Book' with the new_last_no value
#             # frappe.db.set_value('Cheque Book', last_cheque_record['name'], 'last_no', new_last_no)

#             # Return the last record from 'tabCheque Book'
#             return new_last_no
#         else:
#             frappe.errprint("No records found in 'tabPayment Entry'.")
#             return None
#     else:
#         frappe.errprint("No records found in 'tabCheque Book'.")
#         return None

# @frappe.whitelist()
# def cheque_number():
#     # Fetch the last record from 'tabCheque Book'
#     cheque_book_query = """
#         SELECT name, from_no, last_no
#         FROM `tabCheque Book`
#         WHERE last_no >= from_no;
#     """
#     cheque_book_result = frappe.db.sql(cheque_book_query, as_dict=True)

#     print("Cheque Book Result:", cheque_book_result)

#     if cheque_book_result:
#         last_cheque_record = cheque_book_result[0]

#         # Fetch the last record from 'tabPayment Entry'
#         payment_entry_query = """
#             SELECT name, reference_no
#             FROM `tabPayment Entry`
#             WHERE status = 0 AND docstatus = 1
#             ORDER BY creation DESC
#             LIMIT 1;
#         """
#         payment_entry_result = frappe.db.sql(payment_entry_query, as_dict=True)

#         print("Payment Entry Result:", payment_entry_result)

#         if payment_entry_result and last_cheque_record:
#             last_payment_record = payment_entry_result[0]
#             frappe.msgprint(str(last_payment_record))
#             new_last_no = int(last_payment_record['reference_no']) + 1

#             # Update 'tabCheque Book' with the new_last_no value
#             # frappe.db.set_value('Cheque Book', last_cheque_record['name'], 'last_no', new_last_no)

#             # Return the last record from 'tabCheque Book'
#             return new_last_no
#         else:
#             frappe.errprint("No records found in 'tabPayment Entry'.")
#             frappe.msgprint("No records found in 'tabPayment Entry'. This is the else block message.")
#             return None
#     else:
#         frappe.errprint("No records found in 'tabCheque Book'.")
#         frappe.msgprint("No records found in 'tabCheque Book'. This is the else block message.")
#         return None

# import frappe

# @frappe.whitelist()
# def cheque_number(self):
#     # Fetch the last record from tabCheque Book
#     cheque_book_query = "SELECT from_no, last_no FROM `tabCheque Book` WHERE last_no >= from_no ORDER BY `creation` DESC LIMIT 1;"
#     cheque_book_result = frappe.db.sql(cheque_book_query, as_dict=True)

#     if cheque_book_result:
#         cheque_book_record = cheque_book_result[0]
#         frappe.errprint(cheque_book_record)
#         last_no = cheque_book_record.get('last_no')

#         # Increment the last_no value by 1
#         next_cheque_number = last_no + 1

#         # Update the last_no value in the tabCheque Book
#         frappe.db.set_value('Cheque Book', cheque_book_record['name'], 'last_no', next_cheque_number)

#         # Fetch the last reference number from tabPayment Entry
#         payment_entry_query = "SELECT reference_no FROM `tabPayment Entry` WHERE status = 0 AND docstatus = 1 ORDER BY creation DESC LIMIT 1;"
#         payment_entry_result = frappe.db.sql(payment_entry_query, as_dict=True)

#         if payment_entry_result:
#             last_reference_no = payment_entry_result[0].get('reference_no')

#             # Increment the reference number
#             next_reference_no = int(last_reference_no) + 1

#             # Create a new payment entry with the incremented reference number
#             new_payment_entry = frappe.get_doc({
#                 'doctype': 'Payment Entry',
#                 'reference_no': next_reference_no,
#                 # Add other fields as needed
#             })
# def cheque_number():
#     # Specify the upper and lower bounds for the range
#     from_no = 100
#     to_no = 200

#     # Fetch the records from 'tabCheque Book' where last_no is between from_no and to_no
#     cheque_book_query = """
#         SELECT name, from_no, last_no
#         FROM `tabCheque Book`
#         WHERE last_no BETWEEN %s AND %s
#         ORDER BY `creation` DESC
#         LIMIT 1;
#     """
#     cheque_book_result = frappe.db.sql(cheque_book_query, (from_no, to_no), as_dict=True)

#     print("Cheque Book Result:", cheque_book_result)

#     if cheque_book_result:
#         last_cheque_record = cheque_book_result[0]

#         # Fetch the last record from 'tabPayment Entry'
#         payment_entry_query = """
#             SELECT name, reference_no
#             FROM `tabPayment Entry`
#             WHERE status = 0 AND docstatus = 1
#             ORDER BY creation DESC
#             LIMIT 1;
#         """
#         payment_entry_result = frappe.db.sql(payment_entry_query, as_dict=True)

#         print("Payment Entry Result:", payment_entry_result)

#         if payment_entry_result :
#             last_payment_record = payment_entry_result[0]
#             frappe.msgprint(str(last_payment_record))
#             new_last_no = int(last_payment_record['reference_no']) + 1

#             # Update 'tabCheque Book' with the new_last_no value
#             # frappe.db.set_value('Cheque Book', last_cheque_record['name'], 'last_no', new_last_no)

#             # Return the last record from 'tabCheque Book'
#             return new_last_no
#         else:
#             frappe.errprint("No records found in 'tabPayment Entry'.")
#             frappe.msgprint("No records found in 'tabPayment Entry'. This is the else block message.")
#             return None
#     else:
#         frappe.errprint("No records found in 'tabCheque Book'.")
#         frappe.msgprint("No records found in 'tabCheque Book'. This is the else block message.")
#         return None
#             new_payment_entry.insert()

#             return {
#                 'next_cheque_number': next_cheque_number,
#                 'next_reference_no': next_reference_no,
#             }
#         else:
#             frappe.errprint("No records found in tabPayment Entry.")
#             return None
#     else:
#         frappe.errprint("No records found in tabCheque Book.")
#         return None
