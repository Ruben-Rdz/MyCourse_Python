# 


print ("\nAdding more complex and control.") 

avialable_toppings = ["mushrooms", "green peppers", "extra cheese"]

requested_toppings = ["mushrooms","french fries", "green peppers" ]

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in avialable_toppings:
            print(f"Adding {requested_topping}")
        else:
            print(f"sorry we are out of {requested_topping}")
    print("Finished making your pizza!")
else:
    print(f"\nAre you sure you want a plain pizza?")

    