L = []
lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'k', 'a']]

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

# append - добавляет 25
L.append(25)
# append - добавляет 35
L.append(35)
b = [38, 58]
# extend - добавляет все элементы списка b
L.extend(b)
# insert - позволяет вставить элемент в список нумерация с 0
L.insert(1, 45)
# remove(35) - удаляет первый элемент в списке 35 последующий 35 останется
L.remove(35)
# pop - удаляет i элемент, если не указывать то удаляет последний элемент
L.pop(0)
# index - возвращает значение, показывает под каким индексом он находится
L.index(45)
print(L.index(45))
# сout - говорит сколько элементов указаных находится в списке
print(L.count(38))
# sort - сортирует от A до Я
L.sort()
# reverse - переворачивает наоборот наш список
L.reverse()
# сlear - очищает наш список
L.clear()
print(L)
