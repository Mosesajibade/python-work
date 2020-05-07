def isPrime(n):
    truth_val = True
    for o in range(2,n): #missing range function; avoid double-assigning variable in for loop and range function; re-name for loop variable
        if (n % o == 0): #argument in if statement should start with arbitrary number THEN for range variable 
            print("if block is prime", o,n)
            truth_val = False
            print("Condition is satisfied") #this is an exmple of logging to check if the function is at least being tested.
            break
    return truth_val 


def num_analyzer(n): #argument needed in function definition
    while (n > 0):
        print("analyzing",n)
        if (n % 2 == 0): #argument for if must be in parentheses
            print (n, "is an even number")
        if (n % 2 != 0): #argument for if must be in parentheses; make sure the arguments you pass are correct. 
            print (n, "is an odd number")
        if (isPrime(n)):  #arg for if must be in parentheses; True is not needed 
            print(n, "is a prime number")

        n -= 1

num_analyzer(5)