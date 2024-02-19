from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value, name):
           super().__init__(value)
           self.name=name
    

class Phone(Field):
    def __init__(self, value,phone):
          super().__init__(value)
          self.phone=phone
 

class Record(Name):
    def __init__(self, name):
        self.name =name
        self.phones = []


    def add_phone(self,phone):
        self.phones.append(phone)
        

    def remove_phone(self,phone):
        if phone in self.phones:
            self.phones.remove(phone)


    def edit_phone(self,phone_old,phone_new):
        self.phones[phone_old]=phone_new


    def find_phone(self,phone):
        if phone in self.phones:
            return phone
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    book={}      
    def add_record(self,Record):
        self.data=Record

    def find(self,name):
        print(self.data[name])
		
    def delete(self,Record):
        if Record in self.data:
            self.data.pop(Record)



# # Створення нової адресної книги
book = AddressBook()

#     # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

#     # Додавання запису John до адресної книги
book.add_record(john_record)

#     # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

#     # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

#     # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane
book.delete("Jane")

