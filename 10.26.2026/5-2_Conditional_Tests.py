### Try it yourself ### Python Crash course ###
# Date: 09.20.2026

#5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing 
# each test and your prediction for the results of each test. Your code should look 
# something like this:

#    car = 'subaru' 
#    print("Is car == 'subaru'? I predict True.") 
#    print(car == 'subaru') 
#    print("\nIs car == 'audi'? I predict False.") 
#    print(car == 'audi')

# 

company = "vw"
print("If company == 'vw'? I predict True" )
print(company == "vw")

print("\nIf company == 'toyota'? I predict False" )
print(company == "toyota")

##

job = "Tax Accountant"
print("\nIs your job == 'Tax Accountant'? I think is True ")
print(job == "Tax Accountant")

print("\nIs your job == 'Lower'? I think is False")
print(job == "Lower")

###

food = "chilaquiles"
print("\nIs your food == 'chilaquiles'? I beleave is True")
print(food == "chilaquiles")

print("\n Is your food == 'pasta'? I beleave is False")
print(food == "pasta")


# Tests using the lower() method

# To compare to vales that can be different by a Capital leter is posible solve this problem with lower. 

variable = "Chilaquil"

print ("\nIs the same Chilaquil that chilaquiil?")
print ("I bealive that no, almost we add lower method.")

print(variable.lower() == "chilaquil")

print ("\nAnother example")
print ("Audi ist'n same that audi")
brand = "Audi"
print (brand.lower() == "audi")

# Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to

edad = 18
print("\n")
print("La edad debe ser mayor o igual a 18 años")
print ( edad >= 18)

edad_2 =17
print("\n")
print("La edad debe ser mayor o igual a 18 años")
print ( edad_2 >= 18)

# El orden de los signos de mayor o menor que tienen importancia...

print("\n")
print("Para poder ingresar debe ser menor o igual que 19")
print ( edad_2 <= 19)

print("\n")
print("Para poder ingresar debe ser mayor o igual que 19")
print ( edad_2 >= 19)

## We can try with two filtters... with "or" for 2

print (f"\n Age: {edad}")
print (f"Age 2: {edad_2}")

print("edad >= 18 or edad_2 >= 18   - For this example, we try to validate that minimal 1 person will be oldest than 18.")
print(edad >= 18 or edad_2 >= 18  )


print (f"\n Cambiemos las edades")
edad = 12
edad_2= 11

print (f" Age: {edad}")
print (f"Age 2: {edad_2}")

print("edad >= 18 or edad_2 >= 18   - For this example, we try to valite that minimal 1 person will be oldest than 18.")
print(edad >= 18 or edad_2 >= 18  )
print("Any person is oldest than 18 years")


print (f"\n Cambiemos las edades por dos personas de 17")
edad = 17
edad_2= 17

print (f" Age: {edad}")
print (f"Age 2: {edad_2}")

print("edad >= 18 or edad_2 >= 18   - For this example, we try to valite that minimal 1 person will be oldest than 18.")
print(edad >= 18 or edad_2 >= 18  )
print("Any person is oldest than 18 years")


print (f"\n Cambiemos las edades por dos personas de 18 y 19")
edad = 18
edad_2= 19

print (f" Age: {edad}")
print (f"Age 2: {edad_2}")

print("edad >= 18 or edad_2 >= 18   - For this example, we try to valite that minimal 1 person will be oldest than 18.")
print(edad >= 18 or edad_2 >= 18  )
print("Both are more 18 years old")


## Its time to test, with and, for two conditionals 

print (f"\n Sames ages 18 y 19")
edad = 18
edad_2= 19

print (f" Age: {edad}")
print (f"Age 2: {edad_2}")

print("edad >= 18 and edad_2 >= 18   - For this example, we try to validate both ages minimum of 18.")
print(edad >= 18 and edad_2 >= 18  )
print("Both are more 18 years old")


print (f"\nSames ages 12 y 19")
edad = 12
edad_2= 19

print (f"Age: {edad}")
print (f"Age 2: {edad_2}")

print("edad >= 18 and edad_2 >= 18   - For this example, we try to validate both ages minimum of 18.")
print(edad >= 18 and edad_2 >= 18  )
print("1 person is junger")


print (f"\nSames ages 21 y 17")
edad = 21
edad_2= 17

print (f"Age: {edad}")
print (f"Age 2: {edad_2}")

print("edad >= 18 and edad_2 >= 18   - For this example, we try to validate both ages minimum of 18.")
print(edad >= 18 and edad_2 >= 18  )
print("1 person is yunger")



# Test whether an item is in a list

request_list = ["eggs", "#cocas", "lemon", "potatos", "ice cream"]
print ( "\n Huevos listos")
print ( "eggs" in request_list)

print("\nCamararon no!")
print ("camarones" not in request_list)

print ("\nTest Canicas")
if "canicas" not in request_list:
    print (f"Time to request 'Canicas'")

print ("\nTest Cocas")
if "cocas" not in request_list:
    print ("Hay cocas están en el refrí")
else:
    print ("Pide las cocas")
