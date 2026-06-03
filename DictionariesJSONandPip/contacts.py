
contacts = {
    'number': 4,
    'students': 
        [
            {'name': 'Sarah Holderness', 'email':'sarah@example.com'},
            {'name': 'Honey Langhoff-Doherty', 'email':'honey@example.com'},
            {'name': 'Cy Doherty', 'email':'cy@example.com'},
            {'name': 'Allyson Langhoff', 'email':'allyson@example.com'}
        ]
}

print('Student emails:')

for student in contacts['students']:
    print(student['email'])