oper_name = input('Введите имя оператора: ')
pressure_value = input('Введите текущее значение давления: ')
with open('sensor_log.txt', 'a', encoding='utf-8') as file:
    file.write(f'{oper_name}\t{pressure_value}')