contacts_list = [
    {
        "name": "sai tarun",
        "phone_number": 9152322222,
        "email": "saitarun@gmail.com",
    },
    {
        "name": "Rahul",
        "phone_number": 9876543210,
        "email": "rahul@gmail.com",
    },
]


def add_contact(name, phone_number, email):
    contacts_list.append(
        {
            "name": name,
            "phone_number": phone_number,
            "email": email,
        }
    )


def search_contact(name, contacts_list):
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            return contact

    return None


def update_contact(name, phone_number, contact_list):
    contact = search_contact(name, contact_list)

    if contact is None:
        return "no contacts found"

    contact["phone_number"] = phone_number

    return "contact updated successfully"


def delete_contact(name, contact_list):
    contact = search_contact(name, contacts_list)

    if contact is None:
        return "no contacts found"

    contact_list.remove(contact)

    return "contact deleted successfully"


print(search_contact("sai tarun", contacts_list))

print(update_contact("sai tarun", 9154545553, contacts_list))

print(delete_contact("sai tarun", contacts_list))
