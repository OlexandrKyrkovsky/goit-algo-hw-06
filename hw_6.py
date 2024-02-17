from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value,name):
           super().__init__(value)
           self.name=name
    

class Phone(Field):
    def __init__(self, value,phone):
          super().__init__(value)
          self.phone=phone
 

class Record(Name):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(phone)
        

    def remove_phone(self,phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self,phone_old,phone_new):
        self.phones[phone_old]=self.phones[phone_new]


    def find_phone(self,phone):
        return Phone[phone]
        

    # реалізація класу

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



# Я можливо не до кінця зрозумів умови дз , але ви підкажіть якщо що не так. Дякую!!!

