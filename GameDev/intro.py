import random
import math

####   Loop exercises ####
"""Ex. 1"""
# name = 'Stephen'

# for i in range(1,11):
#     print(name)
# print("Done")

"""Ex. 2"""
# for i in range(1,21):
#     print('Red')
#     print('Gold')

##  or  ##

# for i in range(1,21):
#     print("""Red
# Gold""")

"""Ex. 3"""
# list = range(1,101)

# for item in list:
#     if item % 2 == 0:
#         print(item)

"""Ex. 4"""
# count = 2
# while count != 102:
#     print(count)
#     count += 2

"""Ex. 5"""
# count = 10
# while count >= 0:
#     print(count)
#     if count == 0:
#         print("Blast off!")
#     count -= 1

"""Ex. 6"""
# int = random.randint(1,11)
# print(int)

"""Ex. 7"""
# int = random.uniform(1,10)
# print(int)

"""Ex. 8"""
# sum = 0
# pos_nums = 0
# neg_nums = 0
# zeros = 0
# for i in range(7):
#     user_nums = float(input("Provide a Number:"))
#     sum += user_nums
#     if user_nums < 0:
#         neg_nums += 1
#     elif user_nums > 0:
#         pos_nums += 1
#     else:
#         zeros += 1
# print(f"The sum is:{sum}\nThe count of positive entries is:{pos_nums}\nThe count of negative entries is:{neg_nums}\nThe count of zeros is:{zeros}")

"""Ex. 9"""
# heads = 0
# tails = 0
# for i in range(1, 51):
#     num = random.randrange(1,3)
#     if num == 1:
#         print("Heads")
#         heads += 1
#     else:
#         print("Tails")
#         tails += 1
#     print(f"The coin has flipped heads {heads} time(s), and \n tails {tails} time(s)")


###   Conditionals   ###
"""Ex. 1"""
# correct = 0

# q_one = input("What is 9^2?:")
# if q_one == "81" or q_one == " 81" or q_one == " 81 ":
#     print("Correct!")
#     correct += 1
# else:
#     print("Incorrect; the correct answer was 81.")

# print()

# q_two = input("What is the square root of 64?:")
# if q_two == "8" or q_two == " 8" or q_two == " 8 ":
#     print("Correct!")
#     correct += 1
# else:
#     print("Incorrect; the correct answer was 8.")

# print()

# q_three = input("What 2 numbers multiply to 9 and add to 6?:")
# if q_three == "3 and 3" or q_three == "3, 3" or q_three == "3 & 3" or q_three == "3,3":
#     print("Correct!")
#     correct += 1
# else:
#     print("Incorrect; the correct answer was 3 and 3.")

# print()

# q_four = input("What year was arithmetic first available in the United States?:")
# if q_four == "1821" or q_four == " 1821" or q_four == " 1821 ":
#     print("Correct!")
#     correct += 1
# else:
#     print("Incorrect; the correct answer was 1821.")

# print()

# q_five = input("What is 45/5?:")
# if q_five == "9" or q_five == " 9" or q_five == " 9 ":
#     print("Correct!")
#     correct += 1
# else:
#     print("Incorrect; the correct answer was 9.")

# print()

# q_six = input("What day of the week comes after Sunday?:")
# if q_six == "Monday" or q_six == "monday" or q_six == " Monday " or q_six == " Monday" or q_six == " monday " or q_six == " monday":
#     print("Correct!")
#     correct += 1
# else:
#     print("Incorrect; the correct answer was Monday.")

# print()

# q_seven = input("""How many days are there in a week?
# a. 4
# b. 6
# c. 8
# d. none of the above
#     answer:""")
# if q_seven == "d" or q_seven == " d" or q_seven == " d " or q_seven == "D" or q_seven == " D" or q_seven == " D " or q_seven == "d." or q_seven == " d." or q_seven == " d. " or q_seven == "D." or q_seven == " D." or q_seven == " D. ":
#     print("Correct!")
#     correct += 1
# else:
#     print("Incorrect the correct answer was d. none of the above.")

# print()

# percentage = (correct/7) * 100
# print(f"""You got {correct} answers correct. 
# That's {percentage}% of your answers.""")

###  Input/Math/Operators  ###
"""Ex. 1"""
# user_temp = float(input("Enter a temperature in Fahrenheit:"))
# celsius = round(((user_temp - 32) / 1.8), 1)
# print(f"The temperature in Celsius: {celsius}")

"""Ex. 2"""
# height = float(input("""Area of a trapezoid
# Enter the height of the trapezoid: """))
# base_one = float(input("Enter the length of the bottom base: "))
# base_two = float(input("Enter the length of the top base: "))

# area = (1/2) * (base_one + base_two) * height

# print(f"The area is: {area}")

"""Ex.3"""
# print("Quadratic Formula Calculator")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# sqrt = math.sqrt((b**2) - 4*a*c)
# x1 = (((-b) + sqrt) / (2*(a)))
# x2 = (((-b) - sqrt) / (2*(a)))
# if x1 != x2:
#     print(f"x = {x1}, x = {x2}")
# else:
#     print(f"x = {x1}")
