try:                                # Исключение
    x = int(input())                # Вводим число x
except ValueError:                  # При данной ошибке
    print("Вы ввели не число")      # Выводим текст ошибки
    x = 0                           # Задаём x значение при ошибке

try:                                # Исключение
    y = int(input())                # Вводим число y
except ValueError:                  # Исключение
    print("Вы ввели не число")      # Выводим текст ошибки
    y = 0                           # Задаём y значение при ошибке
else:
    print("Всё верно")
finally:
    print("Выполнится 100%")
print(y)

try:
    res = x/y
except ZeroDivisionError:
    print("Вы ввели 0")
    res = 0
print(res)
