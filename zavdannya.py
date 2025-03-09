from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def TenCharValid(self):
        regcode = "+38"
        if len(self.value) == 10:
            return regcode + self.value
        else:
            return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        valid_phone = Phone(phone).TenCharValid()
        self.phones.append(Phone(valid_phone))
    
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = Phone(new_phone).TenCharValid()
                return
        print(f"Phone {old_phone} not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def edit_phone(self, name, old_number, new_number):
        record = self.find(name)
        if record:
            record.edit_phone(old_number, new_number)
        else:
            print(f"Contact: {name} not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact: {name} not found")

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())




# Створення нової адресної книги
contacts = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
contacts.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
contacts.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(contacts)

    # Знаходження та редагування телефону для John
john = contacts.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
contacts.delete("Jane")
