#Python Crash Course
# 6 Dictionaries

# Date: 11.21.2026

# A List of Dictionaries

aliens = []    # Empty dictionary

for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens 
for alien in aliens[:5]:
    print(alien)

# Print the number of aliens
print(f"The number total of aliens is {len(aliens)}")

# Changing the fist 3 aliens to ywlloe
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens 
for alien in aliens[:5]:
    print(alien)

# In general is posible use this for - Non realistic 

print("\n ----- Nesting -----")
print("List of dictionaries")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print (alien)

