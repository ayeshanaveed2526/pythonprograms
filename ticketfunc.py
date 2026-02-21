# Write a function ticket_amount(ticket_price, quantity) that:
# Takes price of one ticket and number of tickets as parameters
# Returns the total payable amount
# Call the function with sample inputs and print the total
ticket_price = 15.00
number_of_tickets = 4
def ticket_amount(ticket_price, number_of_tickets):
    total_amount = ticket_price * number_of_tickets
    return total_amount
print("Total payable amount:", ticket_amount(ticket_price, number_of_tickets))