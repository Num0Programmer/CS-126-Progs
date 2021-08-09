##############################################################################
# CS 126 Lab 7: Contacts
# Contributor Name(s): Asa Henry | Minh Nguyen
# Contributor Email(s): ajh728@nau.edu |
##############################################################################

def new_contact_store():
    contact_store = []
    return contact_store

def add_new_contact(contacts, first_name, last_name, email, phone_number, birthday):
    # Creates a new list element that is a dictionary of fields for a contact
    contacts.append(
        {'first': first_name, 'last': last_name, 'email': email,
        'phone number': phone_number, 'birthday': birthday}
        )
    return contacts

def remove_contact(contacts, first_name, last_name):
    # Iterates over the list of contacts
    for i in range(len(contacts)):
        # Matches the current contact to that of the first_name and 
        # last_name fields
        for contact in contacts:
            if contact['first'] == first_name and contact['last'] == last_name:
                contacts.pop(i) # Removes the contact (dictionary) at 
                                # the list indedx of i
    return contacts

def has_contact(contacts, first_name, last_name):
    for contact in contacts:
        return contact['first'] == first_name and contact['last'] == last_name

def get_contact_string(contacts, first_name, last_name):
    for contact in contacts:
        if contact['first'] == first_name and contact['last'] == last_name:
            return (f"""
                    Name: {first_name} {last_name}
                    Email: {contact['email']}
                    Phone Number: {contact['phone number']}
                    Birthday: {contact['birthday']}
                    """
                    )

def update_contact_first_name(contacts, first_name, last_name,
                              new_field_value):
    for contact in contacts:
        if contact['first'] == first_name and contact['last'] == last_name:
            contact['first'] = new_field_value
    return contacts

def update_contact_last_name(contacts, first_name, last_name, 
                             new_field_value):
    for contact in contacts:
        if contact['first'] == first_name and contact['last'] == last_name:
            contact['last'] = new_field_value
    return contacts

def update_contact_email(contacts, first_name, last_name, 
                         new_field_value):
    for contact in contacts:
        if contact['first'] == first_name and contact['last'] == last_name:
            contact['email'] = new_field_value
    return contacts

def update_contact_phone_number(contacts, first_name, last_name, 
                                new_field_value):
    for contact in contacts:
        if contact['first'] == first_name and contact['last'] == last_name:
            contact['phone number'] = new_field_value
    return contacts

def update_contact_birthday(contacts, first_name, last_name,
                            new_field_value):
    for contact in contacts:
        if contact['first'] == first_name and contact['last'] == last_name:
            contact['birthday'] = new_field_value
    return contacts





