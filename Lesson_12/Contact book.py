import json

while True:
    interaction = input('Here is available commands to use:\n'
                        '"add", "delete", "stats", "list", "show".\n')
    with open(file='contacts.json') as contacts_json:
        contacts_dict = json.load(contacts_json)
    match interaction:
        case 'add':
            contact_name = input('Type contact name please:\n')
            if not contact_name.isalpha():
                print('Contact name must contain only letters.')
                continue
            contact_number = input('Type contact number please:\n')
            if not contact_number.isdigit():
                print('Contact number must contain only numbers.')
                continue
            if f'{contact_name}' in contacts_dict:
                print(f'Contact {contact_name} already exists. Delete first.')
                break
            else:
                contacts_dict[f'{contact_name}'] = contact_number
                with open("contacts.json", "w") as outfile:
                    json.dump(contacts_dict, outfile)
                print('Success!')
                continue
        case 'delete':
            contact_name = input('Type contact name please:\n')
            if not contact_name.isalpha():
                print('Contact name must contain only letters.')
                continue
            if contact_name.lower() not in contacts_dict:
                print(f'Contact with name "{contact_name}" not found.')
            else:
                del contacts_dict[contact_name]
                with open("contacts.json", "w") as outfile:
                    json.dump(contacts_dict, outfile)
                print('Success!')
                continue
        case 'stats':
            print(f'Contact list has {len(contacts_dict)} contacts')
            continue
        case 'list':
            for contact in contacts_dict:
                print(contact)
            continue
        case 'show':
            contact_name = input('Type contact name please:\n')
            if contact_name.lower() not in contacts_dict:
                print(f'Contact with name "{contact_name}" not found.')
                continue
            print(f'Contact "{contact_name}" has number {contacts_dict[contact_name]}')
            continue
