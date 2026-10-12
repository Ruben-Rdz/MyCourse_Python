### Try it yourself ### Python Crash course ###
# Date: 10.11.2026

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

results = []
for numbers in range(1,10):
    results.append(numbers**3)

print(results)

print(f"\n")

# number = 0
results = [ number**3 for number in range(1,10) ]
print (results)