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
    'karla': 'go',
    'ernesr': 'go'
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


# --------   11.20.2026 ----------

# Looping Through a Dictionary’s Keys in a Particular Order

print(f"\n Now we can use the method sort to apply order at our ditionary")
for name in sorted(favorite_lenguages):
    print(f"{name}, thank you for take the survey!")

# Looping Through All Values in a Dictionary

print (f"\nWe can list only the values of our survey")
for leng in favorite_lenguages.values():
    print(f"{leng.title()}")

# So if we want print only once lenguage we can use method "set"

print (f"\nWe can list only the values of our survey (once by lenguage)")
for leng in set(favorite_lenguages.values()):
    print(f"{leng.title()}")






