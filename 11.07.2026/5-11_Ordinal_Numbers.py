### Try it yourself ### Python Crash course ###
# Date: 11.07.2026

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list,
#such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# Store the numbers 1 through 9 in a list.
# Loop through the list.

#Use an if-elif-else chain inside the loop to print the proper ordinal ending
#for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th
#9th", and each result should be on a separate line.


list_numers = [1,2,3,4,5,6,7,8,9]

for no in list_numers:
    if no == 1:
        print(f"{no}st")
    elif no == 2:
        print(f"{no}nd")
    elif no == 3:
        print(f"{no}rd")
    else:
        print(f"{no}th")