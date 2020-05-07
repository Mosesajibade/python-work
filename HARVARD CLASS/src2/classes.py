class Point: # Classes is a way to generate new types in python
    def __init__(self, x, y): #init means when i create the new function what information do i need? self is the point its self then x value and y value. 
        self.x = x #.x is saying i want to attribut to the x value so you can store the x value inside self/point
        self.y = y

p = Point(3, 5) #point is equal to the point or self and 3=x 5=y
print(p.x)
print(p.y)
