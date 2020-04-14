a = (43, 56, 45.23, 'd')     # кортеж  43, 56, 45.23, 'd' - это тоже
b = [43, 56, 45.23, 'd']

print(a.__sizeof__())        # размер
print(b.__sizeof__())        # размер


c = tuple("Hello World")      # tuple кортеж
print(c)

d = ("Hi", "No", 645)
print(d)
print(d.count(645))
