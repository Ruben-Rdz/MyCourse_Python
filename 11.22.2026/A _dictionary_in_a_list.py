#Python Crash Course
# 6 Dictionaries

# Date: 11.22.2026

# Ad dictionary in a list


pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra-cheese'],

}

print(f"You ordered a{pizza['crust']}-crust pizza"  \
        "with the following toppings:")

for toppings in pizza['toppings']:
    print(toppings)

# You ordered a thick-crust pizza with the following toppings:
# mushrooms
# extra cheese

# ---------------------------------------------------------------------- #

favorite_lenguage = {
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust','go'],
    'phill' : ['python','haskell'],
}

#for name, lenguage in favorite_lenguage.items():
#    print(f"{name.title()}'s favorite lenguages are:")
#    for leng in lenguage:
#        print(leng.title())

for name, lenguage in favorite_lenguage.items():
    if len(lenguage) > 1 :
        print(f"{name.title()}'s favorite lenguages are:")
        for leng in lenguage:
            print(leng.title())
    else:
        for leng in lenguage:
            print(f"{name.title()}'s favorite lenguages is {leng.title()}")
        
           
    


#    Jen's favorite languages are:
#    Python
#    Rust
#    Sarah's favorite languages are:
#    C
#    Edward's favorite languages are:
#    Rust
#    Go
#    Phil's favorite languages are:
#    Python
#    Haskell





