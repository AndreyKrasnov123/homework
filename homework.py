# Пример использования абстракции
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


dog = Dog("Бася", "Чихуа-хуа")
print(f"{dog.name} собака породы {dog.breed}")

cat = Cat("Муся", "Метис")
print(f"{cat.name} кошка породы {cat.color}")


# Пример использования инкапсуляции (минибанк)


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств на счете")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())
account.withdraw(1500)


# Наследие классов


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


student = Student("Персона с xx хромосаммами", 20, "123456")
print(f"{student.name} студентка с ID {student.student_id}")

teacher = Teacher("Степан", 35, "Математики")
print(f"{teacher.name} учитель {teacher.subject}")
