### Try it yourself ### Python Crash course ###
# Date: 11.18.2026

# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already
# taken the poll, print a message thanking them for responding. If they have
#not yet taken the poll, print a message inviting them to take the poll.


favorite_lenguages= {
    'carlos': 'python',
    'pedro': 'c',
    'omar': 'c#',
    'luis': 'java',
    'karla': 'go',
    'ernest': 'go'
}

people = ['luis', 'juan', 'alonso','claudio','luis']

#print(favorite_lenguages.keys())

already = favorite_lenguages.keys()

for person in people:
    print(person.title())
    if person in already:
        print(f"Thank you for your response, {person}")
    else:
        print (f"Please let me {person}, What is your favorite lengague?")