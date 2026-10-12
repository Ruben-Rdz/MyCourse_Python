### Try it yourself ### Python Crash course ###
# Date: 10.11.2026

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts atone and ends at
# one million. Also, use the sum() function to see how quickly Python can add a million numbers.ng to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.


list = []
for numbers in range(1,1000001):
    list.append(numbers)

print(list)
print(min(list))
print(max(list))
print(sum(list))
