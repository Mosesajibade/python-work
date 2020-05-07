"""
Working with functions and scope
"""

# TODO: create a function that takes a dictionary as an argument and returns
# TODO: the iteration number, the key, and the value in a readable way
# TODO: (i.e. "iteration number 1 returns the key firstKey and the value firstValue")

# here is an example dictionary
EXAMPLE_DICTIONARY = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}

# TODO: place the function below
 
RONALDO_STATS = {"game1": 24, "game2": 30, "game3": 36, "game4": 15}
def dictionary_reader(dictionary):
    

    for game in dictionary:
        print("in" , game , "ronaldo make" , str(dictionary[game]) , "completed passes")

dictionary_reader(RONALDO_STATS)
        