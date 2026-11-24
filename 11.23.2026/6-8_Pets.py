### Try it yourself ### Python Crash course ###
# Date: 11.16.2026

# 6-8. Pets: Make several dictionaries, where each dictionary represents a
# different pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your
# list and as you do, print everything you know about each pet.

pet_1 = {
    'name' : 'puchis',
    'animal' : 'dog',
    'age' : 12,
    'color' : 'gray',
    'size' : 'small',
    'owner' : 'alfonso'
}

pet_2 = {
    'name' : 'sandy',
    'animal' : 'chip',
    'age' : 1,
    'color' : 'brown',
    'size' : 'tiny',
    'owner' : 'esteban'

}

pet_3 = {
    'name' : 'wicho',
    'animal' : 'hamster',
    'age' : 3,
    'color' : 'white',
    'size' : 'tiny',
    'owner' : 'luis'
}

pet_4 = {
    'name' : 'pluto',
    'animal' : 'dog',
    'age' : 2,
    'color' : 'yellow',
    'size' : 'big',
    'owner' : 'carlo'
}

pets = [ pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"\nOwner: {pet['owner'].title()}")
    print(f"Name: {pet['name'].title()}")
    print(f"Type of animal: {pet['animal'].title()}")
    print(f"Age: {pet['age']}")
    print(f"Color: {pet['color'].title()}")
    print(f"Size: {pet['size'].title()}")