def square(x): # def is define a new function 
    return x * x # what ever x is it will multiply by its self

# for i in range(10): # numbers 0-9
#     print("{} squared is {}".format(i, square(i))) # .format is used to plug in numbers into the string
#                                                    # its a kind of syntex  the i a place holder for i and the square i is a place holder for square of i. 
#                                                 # .format is also how to call your function on the top. 


def main(): # this just made this function the main function  (ORIGINAL FUNCTION IS ON TOP)
    for i in range(10):
     print("{} squared is {}".format(i, square(i)))



if __name__ == "__main__": # thsi means every time i decide to run the modules.py it will only run the main function
    main()