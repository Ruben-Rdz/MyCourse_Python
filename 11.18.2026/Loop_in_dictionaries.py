#Python Crash Course
# 6 Dictionaries

# Date: 11.18.2026

# Looping Through All Key-Value Pairs
glosary = {
    'api' : 'Application programming interface',
    'tcp' : 'Transmission Control Protocol',
    'udp' : 'User Datagram Protocol',
    'osi' : 'Open Systems Interconnection',
    'web socket' : 'Procolo basado en TCP, permite la comunicación '
    'bidireccional en tiempo real, cliente servidor a través de una '
    'conexión persistente.'

}

# ------  .items() Method ------


for k,v in glosary.items():
    print(f"\nkey: {k}")
    print(f"value: {v}")

# +++++++++++++++++++++++++++++++++++++++++++++++



favorite_lenguages= {
    'carlos': 'python',
    'pedro': 'c',
    'omar': 'c#',
    'luis': 'java',
    'karla': 'go'
}

for k,v in favorite_lenguages.items():
    print(f"\n{k.title()}'s favorite lenguage is {v}")

# This is very usefull to reduce the time if our dictionary contains a large number of items.

## Looping Through All the Keys in a Dictionary

### ----- .keys() Method ------

favorite_lenguages= {
    'carlos': 'python',
    'pedro': 'c',
    'omar': 'c#',
    'luis': 'java',
    'karla': 'go'
}

print(f"\nPrint each name of our firends")
for k in favorite_lenguages.keys():
    print(f"{k.title()}")



# Combining diferents methods and search 


friends = ['pedro', 'luis']

print(f"\n Now we can loop into a list and review if exist in another list")
for name in favorite_lenguages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        lenguage = favorite_lenguages[name].title()
        print(f"    {name.title()} I see you love {lenguage}!")


# We can use "not in" to validete if a key exist

if 'erin' not in favorite_lenguages.keys():
    print(f"\n Please Erin take the poll")












