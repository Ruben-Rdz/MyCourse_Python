### Try it yourself ### Python Crash course ###
# Date: 09.15.2026

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list

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
