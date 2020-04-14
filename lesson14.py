class Person:                        # Класс
    name = "Bogdan"                  # Обьект
    age = 24

    def set(self, name, age):        # Создаём функцию метода
        self.name = name
        self.age = age


vlad = Person()                      # Обьект
vlad.set("Vlad", 25)
print(vlad.name + " " + str(vlad.age))

victor = Person()                    # Обьект
victor.set("Victor", 35)
print(victor.name + " " + str(victor.age))
