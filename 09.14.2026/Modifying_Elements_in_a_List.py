#Python Crash Course
#Introducing List

# Date: 09.12.2026

#Modifing Elements i a list. 

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

motorcycles [0] = "Huxvarna"
print(motorcycles)

motorcycles [2] = "CF-China"
print(motorcycles)

#Append Method, is funtionally to add elements to our list. We can start in empty list and add new elements. 

motorcycles.append ("kAWA")
print(motorcycles)

motorcycles.append ("Harley")
print(motorcycles)

# As shown at next, we star with zero elements, and end with 3.
motorcycles_brands = [] 
motorcycles_brands.append('honda') 
motorcycles_brands.append('yamaha') 
motorcycles_brands.append('suzuki') 
print(motorcycles_brands)

#Insert Method, we can add & choose the position in the list

motorcycles_brands = [] 
motorcycles_brands.append('honda') 
motorcycles_brands.append('yamaha') 
motorcycles_brands.append('suzuki') 
motorcycles_brands.insert(0,'CFMoto') 
print(f"Con 'append' agregamos un elemento nuevo en la posicion 0, mira: {motorcycles_brands}\n")

#Removing Elements from a List
#Using the 'del' Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles [0]
print(f"Con 'del' la lista queda con un elemento menos, observa: {motorcycles}")


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles [2]
print(f"Con 'del' la lista queda con un elemento menos, en este ccaso eliminamos el ultimo elemento, observa: {motorcycles}")

#Removing an Item Using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycle_poped = motorcycles.pop()
print(motorcycles)
print(motorcycle_poped)

#Versus del, Pop method is useful when we need remember in memory the element deleted. 

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycle_poped = motorcycles.pop(1)
print(motorcycles)
print(motorcycle_poped)

#As shown, we can choose the element that will be deleted. 

###---------------------------------------------------------------------------------------###
### New day - 09 - 15 - 2026 

#Finaly is time to review the Reove method.

#A simple execise, is assing a valew of the lsi and next delete from the list. 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"from these motorciclye {motorcycles}")
too_expensive_motorcycle = ("yamaha")
motorcycles.remove(too_expensive_motorcycle)
print(f"A {too_expensive_motorcycle.title()} is too expensive for me")

print(f"The list of cheeper motorcycles are {motorcycles}")