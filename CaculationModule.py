#Define constants
tax = .6

def calculateTotalCost(total_cost):
    """
    Function: calculateTotalCost
    1. take total cost of all items
    2. return the results rounded to a maximum of two decimal places
    """

    return round(total_cost * tax , 2)




def calculateTax(total_cost):
    """
    Calculate the total after taxes
    will take total_cost and return the total (float)
    """
    
    sales_tax = calculateTotalCost(total_cost)
    return round(total_cost + sales_tax, 2)

    
