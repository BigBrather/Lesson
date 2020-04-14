import math             # Импортирование математического модуля
import time             # Импорт модуля os (операционная система)
import os               # Импорт модуля time (время)
import random as r      # Выводит рандомное число as сокращение r используется в коде
import module as m
from module import (hi, add)
try:
    import nomodule
except ImportError:
    print("Модуль nomodule не существует")

print(math.cos(1))      # Выводит cos(1)
print(time.time())      # Выводим время с начала году в секундах
print(os.getcwd())      # Путь файла
print(r.random())       # Рандомное число от 0 до 1
m.hi()
print(m.add(45, 15))
hi()
print(add(35, 15))
