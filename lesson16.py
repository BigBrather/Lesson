class Person:                        # Класс
    # _ Инкапсуляция __ Инкапсуляция говорит о том, что нерекомендуется использоватся в других классах и обьектах
    name = "Bogdan"
    age = 24

    # Конструктор это когда при создании обьекта задаём какие-то характеристики

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # _ Инкапсуляция __ Инкапсуляция говорит о том, что нерекомендуется использоватся в других классах и обьектах

    def set(self, name, age, course):        # Создаём функцию метода
        self.name = name
        self.age = age
        self.course = course


class Student(Person):
    course = 1


igor = Student("Igor", 19)
# igor._Person__set(" Igor", 19)       # Обход инкапсуляции
igor.set("Igor", 23, 5)
print("Name: ", igor.name, ", age - ", igor.age, ", course -", igor.course)

vlad = Person("Vlad", 25)                      # Обьект
# vlad._Person__set("Vlad", 25)
print(vlad.name + " " + str(vlad.age))

victor = Person("Victor", 35)                    # Обьект
# victor._Person__set("Victor", 35)
print(victor.name + " " + str(victor.age))

print('2'+'2')                       # Полиморфизм
