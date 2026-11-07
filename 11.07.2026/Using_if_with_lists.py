#Python Crash Course
#5 IF ELSE STATEMENTS

# Date: 11.07.2026

# When is neccesary review the components of a list, we can 
# mix a for and if

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print ("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}")
print("Finished making your pizza")

# Very curefully, we can change the order... 
# First we check the list contains ingredients.

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print (f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print(f"\nAre you sure you want a plain pizza?")

#If doesnt exist any item in toppings the if keep to 
# else and question to customer...

# 
print ("\nAdding more complex and control.") 

avialable_toppings = ["mushrooms", "green peppers", "extra cheese"]

requested_toppings = ["mushrooms", "green peppers", "french fries"]

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in avialable_toppings:
            print(f"Adding {requested_topping}")
        else:
            print(f"sorry we are out of {requested_topping}")
        print("Finished making your pizza!")
else:
    print(f"\nAre you sure you want a plain pizza?")