### Try it yourself ### Python Crash course ###
# Date: 09.15.2026

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.

# - Store the locations in a list. Make sure the list is not in alphabetical order.

future_travels= ["bacalar","monterrey", "atlanta", "canada", "japon", "panama"]
print(future_travels)

# - Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.

print(sorted(future_travels))

# - Show that your list is still in its original order by printing it.

print (future_travels)

# - Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.

print(sorted( future_travels , reverse=True))
## Remember, the sorted method accept an attribute called reverse but go in 2nd position.

# - Show that your list is still in its original order by printing it again.

print (f"\nThe list original persist with the same order {future_travels}")

# - Use reverse() to change the order of your list. Print the list to show that its order has changed.

print ("Its time to change to reverse order")
future_travels.reverse()
print(future_travels)

# - Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

print ("Go, we can order at start time")
future_travels.reverse()
print(future_travels)

# - Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

print("\nNow, we can re-order defenitivelly")
future_travels.sort()
print(future_travels)

# - Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

print("\nNow, we can re-order defenitivelly but in reverse")
future_travels.sort(reverse=True)
print(future_travels)
