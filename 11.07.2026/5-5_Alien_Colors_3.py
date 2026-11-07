### Try it yourself ### Python Crash course ###
# Date: 11.07.2026

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if elif-else chain.

#If the alien is green, print a message that the player earned 5 points.

#If the alien is yellow, print a message that the player earned 10 points.

#If the alien is red, print a message that the player earned 15 points.

#Write three versions of this program, making sure  each message is printed
#for the appropriate color alien.

# Passes the test

print(f"\nFirst test ")
alien_color = "green"

if alien_color == "green":
    print("The player has earned 5 points.")
elif alien_color == "yelow":
    print("The player has earned 10 points.")
else:
    print("The player has earned 15 points.")


# Testing yelow

print(f"\nSecond test ")
alien_color = "yelow"

if alien_color == "green":
    print("The player has earned 5 points.")
elif alien_color == "yelow":
    print("The player has earned 10 points.")
else:
    print("The player has earned 15 points.")


# Testing red

print(f"\nThird test ")
alien_color = "red"

if alien_color == "green":
    print("The player has earned 5 points.")
elif alien_color == "yelow":
    print("The player has earned 10 points.")
else:
    print("The player has earned 15 points.")
