t_chui = float(input('Введите температуру воздуха в Чуйской области'))
t_ysykkol = float(input('Введите температуру воздуха в Иссык-Кульской области'))
t_osh = float(input('Введите температуру воздуха в Ошской области'))
t_talas = float(input('Введите температуру воздуха в Таласской области'))
t_naryn = float(input('Введите температуру воздуха в Нарынской области'))
t_batken = float(input('Введите температуру воздуха в Баткенской области'))
t_jalal = float(input('Введите температуру воздуха в Джалал-Абадской области'))
average_t = float(round((t_jalal + t_osh + t_naryn +t_batken + t_chui + t_ysykkol + t_talas) / 7, 1))
print(f'Средний показатель температуры воздуха по КР на сегодня {average_t}°С')

