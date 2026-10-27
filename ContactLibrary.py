class ContactLibrary:
    """
    this is for store contact data of users.
    """
    contact_list =[]
    def __init__(self,name,phone):
        self.name = name.strip()
        self.phone = phone.strip()
        ContactLibrary.contact_list.append(self)

    def show_contact(self):
        return f"Name : {self.name}, Number : {self.phone}."

    @classmethod
    def display_all_contact(cls):
        if len(cls.contact_list) == 0:
            return "No contact found."
        else:
            for contact in cls.contact_list:
                print(contact.show_contact())
            return None

    @classmethod
    def search_contact (cls, search_name):
        for contact in cls.contact_list:
            if contact.name.lower().strip() == search_name.lower().strip():
                return contact.__dict__
        return f"{search_name} not found."

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) >= 10 and phone_number.isdigit():
            return True
        else:
            return False

n_contacts = int(input("Enter number of contacts you will add:"))
for i in range(int(n_contacts)):
    name = input("Enter contact name:")
    phone_number = input("Enter contact phone number:")
    if ContactLibrary.validate_phone_number(phone_number):
        ContactLibrary(name,phone_number)
    else:
        print("Invalid phone number.")

ContactLibrary.display_all_contact()