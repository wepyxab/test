color = input()
match color:
    case 'красный' | 'жёлтый':
        print('Стоп.')
    case 'зелёный':
        print('Можно ехать.')
    case _:
        print('Некорректное значение.')
