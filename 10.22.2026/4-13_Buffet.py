### Try it yourself ### Python Crash course ###
# Date: 09.20.2026

#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers. Try to modify one of the items, and make sure that Python rejects the change.


menu = ('pizza', 'falafel', 'carrot cake', "orange juice", "sandwich")
print(f"The original menu is:")
for food in menu: 
    print(food)

# If we try to modify the menu replacing the existing item, we can obain a fatal error called " not suppoprt item assigment"
# menu[1] = "crema"
# TypeError: 'tuple' object does not support item assignment

menu = ('chocomilk', 'omelete', 'carrot cake', "orange juice", "sandwich")

print(f"\nThe new menu is:")
for food in menu: 
    print(food)


