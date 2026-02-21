# Write a function calculate_total(price_list) that:
# Takes a list of item prices as parameter
# Returns the total cost
# Call the function with a sample list of prices and print the total
def totalprice(pricelist):
    total = sum(pricelist)
    return total
pricelist = [10.99, 5.49, 3.50, 12.00]
print("Total cost:", totalprice(pricelist))
