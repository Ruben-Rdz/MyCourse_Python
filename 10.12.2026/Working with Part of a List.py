#Python Crash Course
#Introducing List

# Date: 10.12.2026

#Working with slices in Python.

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

#We can change the slice of 

print(f"Try print from 2nd to 3rd: {players[1:3]}")

#We can omit the firs valew

print(f"Omiting the initial value {players[:3]}")

#Similar syntax if we need the las 3 positions 

print(f"Last three {players[2:]}")

#Other way to obtain the last three

print(f"Last three by other way{players[-3:]}")


# Working with slices in for loop

print(f"\nMy last three elements are:")
for player in players[-3:]:
    print(player.title())



## How can we copy a list? 

my_friends = players[:]

print(f"\nFriend list: {my_friends}")

print(f"Players list: {players}")


#Now we have 2 list, we cn operate both per separate.

my_friends.append("luis")
players.append("pedro")

print(f"\n After changes in separated lists")

print(f"Friend list: {my_friends}")

print(f"Players list: {players}")
