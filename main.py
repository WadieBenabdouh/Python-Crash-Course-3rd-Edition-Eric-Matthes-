
invited_guests = ["wild boar", "my bike", "Phoenix", "Screwdriver", "T90 Shtora"]
print(invited_guests)

absent_guest = invited_guests[0]
print(f'absent guest is : {invited_guests[0]}')
invited_guests.remove(absent_guest)
invited_guests.append("Timon")

print(f'\t{invited_guests[0]}, welcome to the party, we have insects.')
print(f'\t{invited_guests[1]}, welcome my darling. ')
print(f'\t{invited_guests[2]}, welcome, don\'t scare me like that time.')
print(f'\t{invited_guests[3]}, welcome boss.')
print(f'\t{invited_guests[4]}, welcome red scary eyes.')

print(invited_guests)

# we found an extra table
more_guests = ["RedBlack Shoes", "Black Panther Cat", "One Orange Brain cell Cat"]
invited_guests.insert(0, more_guests[0])
invited_guests.insert(3, more_guests[1])
invited_guests.insert(7, more_guests[2])
print(invited_guests)

# we found an extra table, but it supports 2 invitees only, one has to go.
print(f'sorry {invited_guests[7]}, no place for you now, next time for sure!')
invited_guests.pop(7)
print(f'you guys are still invited: \n\t{invited_guests[0]}. \n\t{invited_guests[3]}. ')
more_guests.clear()
# no more queue.
print(more_guests)
