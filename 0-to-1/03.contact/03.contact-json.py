import json
from pathlib import Path

data_folder = Path("data/")
file_to_open = data_folder / "contact.json"


def add_contact(contact, filename):
    with open(filename, "w") as f:
        json.dump(contact, f, indent=2)
        
print(f"Adding contacts...")        
name = input("Name please ")
phone = input("mobile no. ")
email = input("Email ")
contact = {
    "user": [
        {
            "Name": name,
            "Phone": phone,
            "Email": email
        }
    ]
}

new_contact = []
if Path(file_to_open).is_file():
    # print("file exist")
    with open(file_to_open) as f:
        contact_record = json.load(f)
    
    contact_record.append(contact)
    add_contact(contact_record, file_to_open)
else:
    # print("file not found")
    new_contact.append(contact)
    add_contact(new_contact, file_to_open)