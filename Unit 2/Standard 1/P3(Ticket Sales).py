'''
A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

'''

def total_sales(ticket_sales):
    # sum = 0
    # for v in ticket_sales.values():
    #     sum += v
    # return sum
    return sum(ticket_sales.values())


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))