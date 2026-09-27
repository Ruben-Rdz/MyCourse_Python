### Try it yourself ### Python Crash course ###
# Date: 09.15.2026

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.Modify your list, replacing the name of the guest 
# who can’t make it with the name of the new person you are inviting.

#Print a second set of invitation messages, one for each person who is still in your list.

guest = ['ana', 'luis', 'juan', 'carlos']
print(guest)

print(f"Hola {guest[0].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[1].title()}, despues de tanto tiempo, espero puedas acompañarnos a comer en casa.")
print(f"Hola {guest[2].title()}, espero este muy bien, ¿Qué opinas de venir a comer la siguinte semana?")
print(f"Hola {guest[3].title()}, te espero la siguinte semana en casa para que platiquemos y comamos")

no_assist = guest.pop(2)
print (f" Dear {no_assist.title} can't assist to the dinner next week.")

new_guest = "Adrian"
guest.append(new_guest)
print(f"The final list of guest are the next: \n{guest}\n")
print(f"Hola {guest[0].title()}, te invito el día jueves a comer en mi casa")
print(f"Hola {guest[1].title()}, despues de tanto tiempo, espero puedas acompañarnos a comer en casa.")
print(f"Hola {guest[2].title()}, espero este muy bien, ¿Qué opinas de venir a comer la siguinte semana?")
print(f"Hola {guest[3].title()}, te espero la siguinte semana en casa para que platiquemos y comamos")
