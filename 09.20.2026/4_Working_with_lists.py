### Try it yourself ### Python Crash course ###
# Date: 09.20.2026

# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.


# I start this Hw with all the services that I seen in AWS. 

services =["ECS","EC2","IAM","IG", "S3","CloudFormation","DynamoDB","RDS"]
print(services)

#To add at the end new value
services.append("Cloudtrail")
print(services)
print(services[8])


#To add a new value in specific position

services.insert(2,"Event Bridge")
print(services)

#To reduce the list, we can operate with some methods pop (We can save the value in a variable), delete (by index) or remove (by value)
# If we known the valeu is easy delete.
services.remove("S3")
print(services)

# We can save the value to delete with pop.
services.pop(2)
print(services)

# Delete by index 
del services[1]
print(services)

#We can count the elments of our list 
print(len(services))

#We can change the order, temporary and permanently

# To change temporary, sort is the first method to order alphabethical 
list_prueba = sorted(services)
print(f"list sorted: {list_prueba}")

# For sorted is posible add a paraametter to chance the order.
list_prueba = sorted(services, reverse=True )
print(f"list sorted with reverse: {list_prueba}")

#Change the order permanently No alphabetically, order by add and reverse
services.reverse()
print(services)

#Change the order permt Alphabetically
services.sort()
print(services)

services.sort(reverse=True)
print(services)

# Trying error with list  / 09.20.2026

print(f"\n")
print(f"\n")
print(f"\n")
print(f"\n ")
print(services)
print(len (services))
print(services[6]) # If we put more than 6 positions in this line we obtain a index error. 

# 4 Work with lists

#FOR FOR FOR 
for service in services:
    print(service)

# Its important be on the way with the convention names, to reduce the complications 

for service in services:
    print(f"Thats a great service: {service}")
    print(f"Solve a lot of problems in bussiness solutions, {service}\n")
print(f"In general that are the principal services, I'm learning these.\n")

