#Python Crash Course
# 6 Dictionaries

# Date: 11.15.2026

# Now we can review dictionaries, in some words it's a conception of key - value. 
# Its are definied by "{}" similar to define a variable or a list.

alien_0 = {'color': 'green' , 'points': 5}

print (alien_0["color"])
print (alien_0["points"])

# At this time, basically the string "color" is a key and his valew is "green"

# To access the valew we put the variable and the key in brackets.

# We can add more key-values at the elements 

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

###  Starting with an Empty Dictionary

alien_1 ={}
alien_1['color'] = 'blue'
alien_1['points'] = 10
alien_1['x_position'] = 10
alien_1['y_position'] = 40

print(alien_1)


# We can tranform values into dictionary.
# our alien change to red

alien_1['color'] = 'red'
print(alien_1)

alien_1['speed'] = 'medium'

if alien_1 ['speed'] == 'slow':
    x_increment = 1
elif alien_1 ['speed'] == 'medium':
    x_increment = 2
elif alien_1 ['speed'] == 'fast':
    x_increment = 3

alien_1 ['x_position'] = alien_1['x_position'] + x_increment

print(alien_1)

# We can delete a key, Python automatically delete the valuew 


del alien_0 ['points']

print(alien_0)

