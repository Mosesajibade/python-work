"""
Creating classes for your classmates
"""

# TODO: Create a class for an Employee, and include basic data
# TODO: like hours worked, salary, first name, last name, age, and title
class Employee:
    def __init__(self, first_name, last_name, hours_worked, age, salary): #these are the basic informations we want to get 
        self.first_name = first_name
        self.last_name = last_name
        self.hours_worked = hours_worked
        self.age = age
        self.salary = salary
    def __str__(self): # this will create a list of items taht we want to be printed. and join them into a string
        s = [
                '---------', #the lines here are just for readability 
                f"First Name : { self.first_name}", #the f stands for f string lateralas. and the squiggly brackets are used for replacement fields
                f"Last Name : {self.last_name}",
                f"Hours Worked : {self.hours_worked}", 
                f"Age : {self.age}",
                f"Salary : {self.salary}"
             ]
        return print('\n'.join(s)) #to close the function 

    def complete_form(n_users): # this will ask the questions with the helper fucntion ask(user)

        value = [Employee(ask_user("Enter First Name: ").title(),
                        ask_user("Enter Last Name: ").title(),
                        ask_user("Enter Hours Worked: ", type=int),
                        ask_user("Enter Age: ", type=int),
                        ask_user("Enter Salary: ", type=int),
                        )
                for question in range(n_users)
                ]
        print(value) #this will print out the employees objects we arranged up top then return will undo the return. 
        return(value) 
    def ask_user(message='', type=str): # this is an helper funtion that helps get the class in employees inputs 
        user_input = ''
        while not user_input: # this is to make sure names like ( spaces and tabs ) are not allowed. and error messages will 
                            # show and the question will repeat until it is inserted as a string or interger depednind on the type 
            try:
                user_input = type(input(message).strip())
            except ValueError: # if we recieve a error value, it will repeat the question until it gets the desired input. 
                continue
        return user_input
    if __name__ == '__main__':

        USERS = complete_form(2) # we use this to see how many employees we want. 
        for a in range(len(USERS)): # we call the original string 
            USERS[a].__str__()



# TODO: Create a function inside the class and print out a formatted
# TODO: set of strings explaining the details from the employee. Use the f shorthand
# TODO: for formatting that was used in the previous example.

# TODO: Then, call that function to print out those strings with a class
# TODO: of Employee set equal to a variable employeeOne

