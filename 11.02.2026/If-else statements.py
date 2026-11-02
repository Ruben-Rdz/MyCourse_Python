#Python Crash Course
#5 IF ELSE STATEMENTS

# Date: 11.02.2026


age = 19

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print (f"\n Cuando tenemos 3 opciones podemos usar if-elif-else")

age = 12
if age <= 4:
    print("Your admision cost is $0")
elif age < 18:
    print("Your admision cost is $25")
else:
    print("Your admision cost is $40")


# Be more efficient

if age <=4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print (f"\nYour admision cost is ${price}")


# We can use the elif block as we need.

age = 65 

if age <=4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print (f"\nYour admision cost is ${price}")

# To be more strict and sospiciues with your ariables 
# If we change the else for an elif we can omit the else.

age = 65 

if age <=4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >=65:
    price = 20
print (f"\nYour admision cost is ${price}")


