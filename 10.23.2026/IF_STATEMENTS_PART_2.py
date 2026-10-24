#Python Crash Course
#5 IF STATEMENTS

# Date: 10.23.2026

#If.

##  Checking Whether a Value Is in a List

# requested_toppings = ['mushrooms', 'onions', 'pineapple'] 

# 'mushrooms' in requested_toppings
#True 

# 'pepperoni' in requested_toppings 
#False

## The key is the word "in"

## Checking Whether a Value Is Not in a List

banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie'

if user not in banned_users:                        ## --- Not In
    print(f"{user.title()}, you can post a response if you wish.")


## Boolean Expressions

# A Boolean value is either True or False, just like the value of a conditional
# expression after it has been evaluated.

game_active = True 
can_edit = False

car = 'subaru' 
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru') 

print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi')

