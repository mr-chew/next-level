import json
from pathlib import Path

data_folder = Path("data/")
file_to_open = data_folder / "contact.json"


def add_contact(contact, filename):
    with open(filename, "a") as f:
        json.dump(contact, f, indent=2)
        
print(f"Adding contacts...")        
name = input("Name please ")
phone = input("mobile no. ")
email = input("Email ")
contact = {
    "employees" : [
        {
            "Name": name,
            "Phone": phone,
            "Email": email
        }
    ]
}

add_contact(contact, "03.contact.json")