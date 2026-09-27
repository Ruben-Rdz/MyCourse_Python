### Try it yourself ### Python Crash course ###
# Date: 09.15.2026

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# 
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message 
# to that person letting them know you’re sorry you can’t invite them to dinner.
#
# Print a message to each of the two people still on your list, letting themknow they’re still invited.
#
#Use del to remove the last two names from your list, so you have an emptylist. Print your list to make sure you actually have an empty list at the end of your program.

guest = ['ana', 'luis', 'juan', 'carlos']
print(guest)

print(f"Hola {guest[0].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[1].title()}, despues de tanto tiempo, espero puedas acompañarnos a comer en casa.")
print(f"Hola {guest[2].title()}, espero este muy bien, ¿Qué opinas de venir a comer la siguinte semana?")
print(f"Hola {guest[3].title()}, te espero la siguinte semana en casa para que platiquemos y comamos")

no_assist = guest.pop(2)
print (f" Dear {no_assist.title} can't assist to the dinner next week.")

new_guest = "adrian"
guest.append(new_guest)
print(f"The final list of guest are the next: \n{guest}\n")
print(f"Hola {guest[0].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[1].title()}, despues de tanto tiempo, espero puedas acompañarnos a comer en casa.")
print(f"Hola {guest[2].title()}, espero este muy bien, ¿Qué opinas de venir a comer la siguinte semana?")
print(f"Hola {guest[3].title()}, te espero la siguinte semana para comer y platicar")

print("Dear all guest, I will introduce a new 3 friends, we have already a new restaurant\n")

guest.insert(0,"pedro")
guest.insert(3,"ernesto")
guest.append("claudia")
print(guest)

print(f"Hola {guest[0].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[1].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[2].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[3].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[4].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[5].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[6].title()}, te invito el día jueves a comer en mi casa")

message="Dear, sorry but we have a trouble with the dinner table, for next times I will appreciate your assistence"
print (message)

guest_popped1 = (guest.pop())
print(f"Dear {guest_popped1.title()}, I sorry for the mistake, currently the dinner was canceled.")

guest_popped1 = (guest.pop())
print(f"Dear {guest_popped1.title()}, I sorry for the mistake, currently the dinner was canceled.")

guest_popped1 = (guest.pop())
print(f"Dear {guest_popped1.title()}, I sorry for the mistake, currently the dinner was canceled.")

guest_popped1 = (guest.pop())
print(f"Dear {guest_popped1.title()}, I sorry for the mistake, currently the dinner was canceled.")

guest_popped1 = (guest.pop())
print(f"Dear {guest_popped1.title()}, I sorry for the mistake, currently the dinner was canceled.")

print(guest)
print(f"Dear {guest[0]}, You are still invited to the diner of the next week, .")
print(f"Dear {guest[1]}, You are still invited to the diner of the next week, .")

del guest['0'] 
del guest[0] 
print(guest)