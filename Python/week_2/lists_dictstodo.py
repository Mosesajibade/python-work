"""
Working with lists and dictionaries to convey a weather forecast
"""

# TODO: create a list with days from Monday through Sunday
days_of_the_week  = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
 
print(days_of_the_week)

# TODO: in the following dictionary, the keys are associated with days of the week while
# TODO: values represent temps the first value of 1 represents sunday's temperature all
# TODO: the way to 7 which represents Saturday
TEMPERATURE_FORECAST = {1: 65, 2: 70, 3: 80, 4: 70, 5: 67, 6: 95, 7: 100}

# TODO: print out Wednesday by accessing it through the list days of week, then print out
print(TEMPERATURE_FORECAST[4])
# TODO: wednesday's temperature by accessing the forecast dictionary
