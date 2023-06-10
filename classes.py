# classes

# class Matematik:
#     def topla(self, sayi1, sayi2):
#         return sayi1 +sayi2

#     def cikar(self, sayi1, sayi2):
#         return sayi1 -sayi2

#     def carp(self, sayi1, sayi2):
#         return sayi1 *sayi2

#     def bol(self, sayi1, sayi2):
#         return sayi1 /sayi2


# matematik = Matematik()


# property class methods

# class Person:
#     def __init__(self, first_name=None, last_name=None, age=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age


# person1 = Person("Musa", "Gürgil", 26)
# print(person1.first_name, person1.last_name, person1.age)


# class Worker(Person):
#     def __init__(self, salary=None):
#         self.salary = salary


# class Customer(Person):
#     def __init__(self, creditCardNumber):
#         self.creditCardNumber = creditCardNumber


# ahmet = Worker()
# mehmet = Customer()


# optimization classes
class Person:
    def __init__(self, first_name=None, last_name=None, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


person1 = Person("Musa", "Gürgil", 26)
print(person1.first_name, person1.last_name, person1.age)


class Worker(Person):
    def __init__(self, salary=None, **kwargs):
        super().__init__(**kwargs)
        self.salary = salary


class Customer(Person):
    def __init__(self, credit_card_number=None, **kwargs):
        super().__init__(**kwargs)
        self.credit_card_number = credit_card_number
