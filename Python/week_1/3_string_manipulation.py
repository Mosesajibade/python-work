"""
Personality questionnaire
"""

# TODO: ask a user to input their full name and test it by entering lower case letters for your name
first_name = input("what is your full name?")
print(first_name)
# TODO: write a program that asks a user 6 unique questions about them and see if it works!

birth_year = input("what year were you born?")
athlete = input("who is your favorite athelete?")
last_name = input("what is your last name?")
favorite_color = input("what is your favorite color?")

print(birth_year + "and" + athlete + last_name + favorite_color)


# TODO: use input functions however you would like (i.e. print question then get input, or include
# TODO: the question within the input variable.)

# TODO: print out the results in a neat format and make sure to capitalize the user's name with the
# TODO: title function
first_name = input("what is your first name?")
print(first_name.lower())
