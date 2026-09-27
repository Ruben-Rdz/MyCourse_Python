#Python Crash Course
#Introducing List

# Date: 09.16.2026

#Modifing Elements i a list. 
#Ordering a List

# Sort method. 

cars = ["bmw","toyota", "nissan", "vw"]
print (cars)

print("\nWe can use sort method to do a order in our list.")
cars.sort()
print(cars)

print("\nAditionally, if we add 'reverse=True' we can organize the list in contrary order")
cars.sort(reverse=True)
print(cars)

#Second method to order list is "Sorted".
# Temporary 
print("\n\n\n Let's gonna try another method to do it:      'SORTED(list)'")
cars = ["bmw","toyota", "nissan", "vw"]
print("\n Here is the original list:")
print(cars)

print("\n Here is the temporary list:")
print(sorted(cars))

print("\n Again, here is the original list:")
print(cars)

##Printing a List in Reverse Order - NO Alphabethically!

print("\n\n\n Let's gonna try another method to do it:      'REVERSE.list'")
cars = ["bmw","toyota", "nissan", "vw"]
print("\n Here is the original list: ")
print(cars)

print("\n With reverse.list we change the order : ")
cars.reverse()
print(cars)

#Method Len - to determine Length
print("\n With len is posible determine the length of our list: ")

cars = ["bmw","toyota", "nissan", "vw"]
total_brands = len(cars)
print(total_brands)