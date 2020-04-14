i = 1000
while i > 100:                    # while - пока
    print(i)
    i /= 2

for j in 'Hello, Bogdan!':
    if j == 'w':
        break                     # continue - пропускает, break - выходит из цикла
    print(j*2, end='')
else:
    print("\nБуквы а нет в слове")
