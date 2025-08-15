# Passing an integer after the ':' will cause that field to be a minimum number of characters wide. 
# This is useful for making columns line up.

table = {'Sonik': 1000, 'Jito': 2000.3443, 'Zatochi': 3000}

for name, dolar in table.items():
    print(f'{name:10} ==> {dolar:.0f}') # .0f - float => int
# {num :.2f} - 2 знака после запятой
# {num :x} - 16 ричная система исчсл (hex)
# {num :b} - 2 ичная система исчсл (bin)
# {num :,} - 1,000 instead of 1000
# round(num, 2) - 1,23



# The = specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

# Для округления вещественных чисел при выводе можно использовать уже известные нам f-строки. 
# Например, выведем квадратный корень из 2 с точностью до двух знаков после запятой:
print(f"{2 ** 0.5:.2f}")


# format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('We are the {1} who say "{0}!"'.format('knights', 'Ni'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]}; Sjoerd: {0[Sjoerd]}; '
      'Dcab: {0[Dcab]}'.format(table))

# таблица квадратов кубов и тд
for x in range(10,30):
    print("{0:2} {1:5} {2:7}".format(x,x*x,x*x*x))

