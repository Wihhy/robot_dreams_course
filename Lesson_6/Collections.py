contacts = {'Vova': 1,
            'Lera': 2,
            'Vlad': 3,
            'Anna': 4,
            'Roma': 5}

while True:
    interaction = input('Here is available commands to use:\n'
                        '"add", "delete", "stats", "list", "show".\n')
    match interaction:
        case 'add':
            while True:
                contact_name = input('Type contact name please:\n')
                if not contact_name.isalpha():
                    print('Contact name must contain only letters.')
                    continue
                contact_number = input('Type contact number please:\n')
                if not contact_number.isdigit():
                    print('Contact number must contain only numbers.')
                    continue
                if f'{contact_name}' in contacts:
                    print(f'Contact {contact_name} already exists. Delete first.')
                    break
                else:
                    contacts[f'{contact_name}'] = contact_number
                    print('Success!')
                    break
        case 'delete':
            contact_name = input('Type contact name please:\n')
            if not contact_name.isalpha():
                print('Contact name must contain only letters.')
                continue
            if f'{contact_name}' not in contacts:
                print(f'Contact with name "{contact_name}" not found.')
            else:
                del contacts[contact_name]
                print('Success!')
                continue
        case 'stats':
            print(f'Contact list has {len(contacts)} contacts')
            continue
        case 'list':
            for contact in contacts:
                print(contact)
            continue
        case 'show':
            contact_name = input('Type contact name please:\n')
            if contact_name not in contacts:
                print(f'Contact with name "{contact_name}" not found.')
                continue
            print(f'Contact "{contact_name}" has number {contacts[contact_name]}')
            continue
