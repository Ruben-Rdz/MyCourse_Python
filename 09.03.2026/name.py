name = "ada lovalace"
print (name.title())

firs_name = "Ada"
last_name = "Lovalace"
full_name = f"{firs_name} {last_name.lower()}"
print(full_name)


#Pruebas con Strings y methods (title, upper, lower)
firs_name = "Ada"
last_name = "Lovalace"
full_name = f"{firs_name} {last_name}"
print(full_name.title())

firs_name = "Ada"
last_name = "Lovalace"
full_name = f"{firs_name} {last_name}"
print(f"Hello, {full_name.upper()}")


firs_name = "Ada"
last_name = "Lovalace"
full_name = f"{firs_name} {last_name}"
print(f"Hello, {full_name.title()}")

firs_name = "Ada"
last_name = "Lovalace"
full_name = f"{firs_name} {last_name}"
message= f"Hello, {full_name.title()}"
print(message)


# Para usar TAB con patrones de texto
print("Python")
print("\tPython")
print("\nPython\n")

print("Languages:\n\tPython\n\tC\n\tJavaScript") 
#print("Languages:\n\tPython\n\tC\n\tJavaScript") 

#Trying method "rstrip"

favorite_lenguage = "  Python  "
favorite_lenguage = favorite_lenguage.lstrip()
favorite_lenguage = favorite_lenguage.rstrip()
print (favorite_lenguage)

#Test remove prefix method

url = "https://devrodriguez.com.mx"
simple_url = url.removeprefix('https://')
print(url)
print (simple_url)


