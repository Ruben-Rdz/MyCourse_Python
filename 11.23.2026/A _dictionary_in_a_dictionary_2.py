#Python Crash Course
# 6 Dictionaries

# Date: 11.22.2026

# A dictionary in a dictionary


users = {
    'aeinstein' : {
        'first': 'albert',
        'lastname' : 'einsten',
        'location' : 'princeton'
    
    },
    'mcurie' : {
            'first': 'marie',
            'lastname' : 'curie',
            'location' : 'paris'
    },    
}


for key, values in users.items():
    print (f"Username: {key}")
    print (f"Full name: {values['first'].title()} {values['lastname'].title()}")
    print (f"Location: {values['location'].title()}")
    print(f"\n")        


#Username: aeinstein
#Full name: Albert Einstein
#Location: Princeton

#Username: mcurie
#Full name: Marie Curie
#Location: Paris

# That is posible because we have the same sttrcuture in both dictionaries 


