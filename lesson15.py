class Person:                        # Класс
    # _ Инкапсуляция __ Инкапсуляция говорит о том, что нерекомендуется использоватся в других классах и обьектах
    name = "Bogdan"
    age = 24

    def __set(self, name, age):        # Создаём функцию метода
        self.name = name
        self.age = age


class Student(Person):
    course = 1


igor = Student()
igor._Person__set("Igor", 19)        # Обход инкапсуляции
igor.course = 4
print(igor.course)

vlad = Person()                      # Обьект
vlad._Person__set("Vlad", 25)
print(vlad.name + " " + str(vlad.age))

victor = Person()                    # Обьект
victor._Person__set("Victor", 35)
print(victor.name + " " + str(victor.age))

print('2'+'2')                       # Полиморфизм
