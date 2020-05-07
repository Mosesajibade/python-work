"""
Lets do a basic math problem
"""

# TODO: perform all of the following mathematical operations and print the results in between

# TODO: set a constant tax rate of 20%
CONSTANT_TAX_RATE = .2


# TODO: ask a user what their revenue was for the quarter

revenue = print(input("what is your revenue for last quarter?"))

# TODO: deduct the tax rate from the revenue and print the profit as well as the tax amount
revenue = 200

tax_amount = revenue * CONSTANT_TAX_RATE 
print(tax_amount)

profit = revenue - tax_amount
print(profit)


# TODO: split that profit evenly amongst 7 share holders

shares = profit / 7 

# TODO: print out what each shareholder will receive from the profit

print(shares)

# !! extra credit: print the remainder of the total profit divided by 6

remainder = shares % 6 
print(remainder)