#Python Crash Course
#Introducing List

# Date: 10.05.2026

## Using the range() Function

##  If we put 2 arguments, is posible print from fist place to 2nd to end 1 - 5
for value in range(1,6):
    print (value)

## We can use only one argument

for value in range(6):
    print (f"\n {value}")

# We can organice an rango into a list. 

list_range = list(range(6))
print (list_range)
print (f"\n ")

# Now, we can give 3 arguments to generate more complicated list. See...

numbers_by2 = list(range(2,11,2))
print(numbers_by2)

# Remember this start by the fisrt number given
numbers_by2 = list(range(1,11,2))
print(numbers_by2)



# Creating a list with a for, with the methot append.

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# This can be more effective: 

squares = []
for value in range(1,11): 
    squares.append(value ** 2)

print(squares)

## Working with stadistical funtions 

print(max(squares))
print(min(squares))
print(sum(squares))