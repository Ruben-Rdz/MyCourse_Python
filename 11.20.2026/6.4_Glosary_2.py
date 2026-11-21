### Try it yourself ### Python Crash course ###
# Date: 11.18.2026

# 6-3. Glossary: A Python dictionary can be used to model an actual
# dictionary. However, to avoid confusion, let’s call it a glossary.
# 
# Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.

# Print each word and its meaning as neatly formatted output. You might print
# the word followed by a colon and then its meaning, or print the word on one
# line and then print its meaning indented on a second line. Use the newline
# character (\n) to insert a blank line between each word-meaning pair in your
# output.



glosary = {
    'api' : 'Application programming interface',
    'tcp' : 'Transmission Control Protocol',
    'udp' : 'User Datagram Protocol',
    'osi' : 'Open Systems Interconnection',
    'web socket' : 'Procolo basado en TCP, permite la comunicación '
    'bidireccional en tiempo real, cliente servidor a través de una '
    'conexión persistente.'

}

print(f" API - {glosary['api']}")
# print(glosary['api'])

print(f"\n TCP - {glosary['tcp']}")

print(f"\n UDP - {glosary['udp']}")

print(f"\n OSI - {glosary['osi']}")

print(f"\n Web socket - {glosary['web socket']}")

# ------  OTHER WAY .items() Method ------


for k,v in glosary.items():
    print(f"\nkey: {k}")
    print(f"value: {v}")

# 11.20.2026
# In this excersice, initially we print each word of the glosary, but next we learn how write with key-values into loo (for) and method items()



