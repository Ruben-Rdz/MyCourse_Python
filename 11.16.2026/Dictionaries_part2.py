#Python Crash Course
# 6 Dictionaries

# Date: 11.16.2026

# We can store information into dictionary, is posible assing values according to the group. 

favorite_lenguages= {
    'carlos': 'python',
    'pedro': 'c',
    'omar': 'c#',
    'luis': 'java',
    'karla': 'go'
}
lenguage = favorite_lenguages['carlos'].title()
print(f"favorite lenguage of Carlos is {lenguage}")
print(f"Carlo's favorite lenguege is {lenguage}")

# Its a good practice assing the valueu to a niew varible called lenguage. 

## print(favorite_lenguages['alba'])

# if we request a value that doesnt exist qw obtain a error 

# we can use the method "get()"
#   requieres 2 arguements 


# print(favorite_lenguages.get('alba', 'Alba ist already mention his favorite lenguage'))

print(favorite_lenguages.get('alba',))

## If we desire is posible is posible obtain "none"

