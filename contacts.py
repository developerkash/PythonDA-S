# ctrl + j to open terminal
# run command pip install analytics/requirements.txt

contacts = {
    'police': 112,
    'emergency': 101,
}

while True:
    name = input("search any contact: ")
    # closing the program
    if len(name) == 0:
        print("bye")
        break

    # searching the contact
    if name in contacts:
        print(f'{name} : {contacts[name]}')
    elif name == 'all':
        for name, number in contacts.items():
            print(f'{name} : {number}')
        print('---') 
        
    # adding the contact
    else:
        print(f'{name} not found')
        ch = input("Do you want to add this contact? (y/n): ")
        if ch == 'y':
            number = int(input("Enter the number: "))
            contacts[name] = number
            print(f'{name} added successfully')
        else:
            print('---')
        