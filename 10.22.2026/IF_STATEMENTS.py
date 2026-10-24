#Python Crash Course
#5 IF STATEMENTS

# Date: 10.22.2026

#If.

menu = ('eggs', 'omelete', 'carrot cake', "orange juice", "sandwich")

for food in menu: 
    if food == "eggs":
        print(food.upper())
    else:
        print(food.title())

## If introduction, have the secuence similar to if, requieres a ":" to express 
# }the next code is part of the conditional.

# Conditional test, if the test result positive, python execute the next lines of code. 

# == 
#This equality operator returns True if the values on the left and right side of the
#  operator match, and False if they don’t match.

# car = 'bmw' 
# >>> car == 'bmw' 
# True

# car = 'audi' 
# >>> car == 'bmw' 
# False   

## Ignoring Case When Checking for Equality

# car = 'Audi' 
#>>> car == 'audi' 
# False

## inequality operator (!=)

requested_topping = 'mushrooms' 

print(f"\nRequestd topping: {requested_topping}")
if requested_topping != "anchovies":
    print("Hold the anchovies!\n")


## -- Numerical Comparisons

        #>>> age = 19 
        #>>> age < 21 
        #True 
        #>>> age <= 21 
        #True 
        #>>> age > 21 
        #False 
        #>>> age >= 21 
        #False

# Each mathematical comparison can be used as part of an if statement, which 
# can help you detect the exact conditions of interest.

## --  Using and to Check Multiple Conditions
#        >>> age_0 = 22 
#        >>> age_1 = 18 
#        >>> age_0 >= 21 and age_1 >= 21 
#        False 

#        >>> age_1 = 22 
#        >>> age_0 >= 21 and age_1 >= 21 
#        True

#       (age_0 >= 21) and (age_1 >= 21)

# Considere thht the age 1 change to 22... for that the test páss...

## -- Using or to Check Multiple Conditions

#        >>> age_0 = 22 
#        >>> age_1 = 18 
#        >>> age_0 >= 21 or age_1 >= 21 
#        True 
 
#        >>> age_0 = 18 
#        >>> age_0 >= 21 or age_1 >= 21 
#        False

# If one of two pass, the test result in True



