import json

class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        "Initialization of the object with certain initial values"

    def to_json(self):
        '''Serialize the object custom object'''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)  

"Creating instances of the Contact class"
c1 = Contact("Lucy Smile", '7777', '1, Smile st.') 
c2 = Contact("Thomas Cook", '1123', '2, Cook avn.')

"Adding instances to the contacts list"
contacts = [c1, c2]

"Serialization of contact list"
serialized_contacts = [contact.to_json() for contact in contacts]

"Writing serialized data to a file"
filename = "contact.json"
with open(filename, 'w') as file:
    json.dump(serialized_contacts, file)

"Deserialization of data from a file"
with open(filename, 'r') as file:
    loaded_contacts = json.load(file)

"Creating a result list from deserialized data"
result = [json.loads(contact) for contact in loaded_contacts]

print(result)
