"""Example"""

# class Dog:
#     # set instance attributes
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def description(self):
#         return f'{self.name} is {self.age} years old'
    
#     def speak(self, sound):
#         return f'{self.name} says {sound}'

# # create an instance of the Dog class
# my_dog = Dog("Fido", 2, "Terrier")
# your_dog = Dog('Odie', 3, 'Beagle')




# print(my_dog.description())

# print(your_dog.speak('woof'))


"""
#1  Create a Quadratic class that takes the coefficients of a quadratic expression.  Add methods for:
    1. evaluating the expression for a given value
    2. for calculating the discriminant
    3. that finds the x-intercepts
    4. that finds the vertex
    5. that plots the quadratic

"""
# import math
# import matplotlib.pyplot as plt



# class Quadratic:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = self.get_discrim()
#         self.x = self.get_vertex()[0]
#         self.y = self.get_vertex()[1]

#     def get_value(self, x):
#         val = (self.a * (x**2)) + (self.b * x) + self.c
#         return val
    
#     def get_discrim(self):
#         self.d = (self.b**2) - 4*self.a*self.c
#         return self.d

#     def get_zeros(self):
#         if self.d >= 0:
#             sqrt = math.sqrt((self.b**2) - 4*self.a*self.c)
#             x1 = (((-self.b) + sqrt) / (2*(self.a)))
#             x2 = (((-self.b) - sqrt) / (2*(self.a)))
#             if x1 != x2:
#                 return x1, x2
#             else:
#                 return x1
#         else:
#             return None

#     def get_vertex(self):
#         self.x = (-self.b) // 2*self.a
#         self.y = (self.a * (self.x**2)) + (self.b * self.x) + self.c
#         vertex = [self.x, self.y]
#         return vertex
    
#     def plot(self):
#         x_vals = []
#         y_vals = []

#         get_x_vals = range(equation.get_vertex()[0]-10, equation.get_vertex()[0]+10)
#         for i in get_x_vals:
#             x_vals.append(i)

#         for i in x_vals:
#             y_vals.append(self.get_value(i))
        
#         plt.plot(x_vals, y_vals)

#         plt.show()

    


# equation = Quadratic(1, 0, -4)

# equation.plot()

# # print(get_vertex.get_vertex())

