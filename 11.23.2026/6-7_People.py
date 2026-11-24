### Try it yourself ### Python Crash course ###
# Date: 11.16.2026

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person_data_1 = {
    'first_name': 'Melissa',
    'last_name': 'Juárez',
    'age': 25,
    'city': 'Mexico City',
}

person_data_2 = {
    'first_name': 'Pedro',
    'last_name': 'Sanchez',
    'age': 45,
    'city': 'Mexico City',
}

person_data_3 = {
    'first_name': 'Luis',
    'last_name': 'Olivares',
    'age': 29,
    'city': 'Peru',
}

people = [ person_data_1, person_data_2, person_data_3 ]

for person in people:
    print(f"Hi {person['first_name']}, you are {person['age']} years old and lives in {person['city']}" )

#    for k,v in person.items():
#        print(f"Hi {v}")

