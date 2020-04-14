num = input("Введите ваше имя: ")

if num == "Bogdan":                      # if - если , 1 = True , 0 = False
    print("True\n")                      # \n - переход на новую строку
    print("All is okay!\n")                # == - равно , != - не равно
else:
    print("What is this?\n")


num = input("Введите число: ")

if int(num) > 10:
    print("Вы ввели число больше 10")
elif int(num) < -10:
    print("Вы ввели число меньше -10")
else:
    print("Вы ввели число в диопазоне от 10 до -10")


name = input()
A = 'Yes' if name != "Test" else 'No'
print(A)
