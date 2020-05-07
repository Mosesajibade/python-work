"""
Working with for loops in dictionaries and lists
"""

# Hint! Remember that None is basically setting something as an undefined value. This is helpful when
# you intend on being specific about the scope of a variable and wanting to populate it later

# TODO: create a series of for loops that prints out each day of the week with the high and low of each day
# TODO: in this problem, the high and low of each period of the day is set in the array in the key value pair

ADVANCED_FORECAST = {
    "Sunday": {"morning": [40, 55], "afternoon": [57, 64], "evening": [59, 43]},
    "Monday": {"morning": [38, 50], "afternoon": [52, 66], "evening": [54, 47]},
    "Tuesday": {"morning": [46, 65], "afternoon": [50, 58], "evening": [59, 39]},
    "Wednesday": {"morning": [30, 35], "afternoon": [35, 56], "evening": [48, 29]},
    "Thursday": {"morning": [32, 41], "afternoon": [48, 62], "evening": [60, 37]},
    "Friday": {"morning": [42, 50], "afternoon": [45, 52], "evening": [54, 35]},
    "Saturday": {"morning": [40, 43], "afternoon": [52, 64], "evening": [60, 37]},
}

for day in ADVANCED_FORECAST:
    high = None
    low = None
    time_of_day = ADVANCED_FORECAST[day]
    for time in time_of_day:
        temp_array = time_of_day[time]
        for temp in temp_array:
            if(high == None and low == None):
                high = temp
                low = temp
            elif(temp > high): 
                high = temp
            elif(temp < low):
                low = temp
    print(day, "will give a low of", low, "and a high of", high)


