def func(x, a):                  # Функция def
    res = x + a                  # сумируем два значения
    return res                   # возвращаем


print(func('Hello', ' World'))   # Можно выводить любые значения


def func(x):
    def add(a):
        return x + a
    return add


test = func(100)
print(test(200))


def func():
    pass


print(func())


def func(r, w, y=2):
    res = r + w
    res *= y
    return res


print(func(2, 4, 3))


def func(*args):
    return args


print(func(2, 4, 3, 'Hy'))


def func(**args):
    return args


print(func(a=10, b=56, c=22, d=65))
print(func(short='dict', longer='dictionary'))


def func(**args):
    return args


print(func(short='dict', longer='dictionary'))

# add = lambda x, y: x * y


def add(x, y): return x * y


print(add(2, 5))
print(add('q', 5))

print((lambda x, y: x * y)(2, 6))

fun = lambda *args: args
print(fun(2, 5, 78, 56))
