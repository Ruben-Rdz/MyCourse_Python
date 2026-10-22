#Python Crash Course
#Introducing List

# Date: 10.22.2026

#Tuples.

## Parentheses vs squere brackets

dimensions = (10,20)

print(f"Printing manually each value:")
print(dimensions[0])
print(dimensions[1])
print(dimensions)
print(f"\n")


# dimensions[0]=100  -- tHis can't be load beacuase is a tuple, pyhthon can't 
# assing an value in a tuple 

for dimension in dimensions:
        print(f"In a loop, similar to list, we can print each element of a tuple: {dimension}")

# Interesting, we can't modify an valew but we can change the complete tuple. 

print(f"The original tuple is {dimensions}")

print(f"We redefine the scale with 150, 180")

dimensions = (150,150)

print(f"The new tuple is {dimensions}")
