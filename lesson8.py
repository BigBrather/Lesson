d = dict([(23, 24), (56, 87)])
print(d)

c = dict(short='dict', longer='dictionary')
c['short'] = 234
print(c)

b = dict.fromkeys(['a', 'b', 'c'], 1)
print(b)

s = {a: a**2 for a in range(7)}
print(s)

person = {'name': {'last_name': 'Большаков', 'first_name': 'Богдан', 'middle_name': 'Валерьевич'}, 'address': [
    'г. Севастополь', 'ул. Дмитрия Ульянова д. 2/2', 'кв. 61'], 'phone': {'home_phone': '2-22-02', 'mobile_phone': '7-978-714-54-63', 'mobile_phone': 'Нет'}}
print(person['name']['first_name'])
print(person['address'][1])

# person.clear()
# print(person)
print(person.values())
