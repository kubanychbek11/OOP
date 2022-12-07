# Логический тип данных, условные конструкции и операторы.
# print('hello world')
# bool - boolean (логический тип данных) True, False
# or, and, not -  логические операторы

shoes_black = '34-38'
first = int(shoes_black[:2])
second = int(shoes_black[3:])

# print((second-first) // 2 + 1),

# [start:stop:step]
# word = 'стоматолог'
# cut = word[4:]
# print(word)
# print(cut)

# print(word[::-1])
# print(word[1:6])


# print(word[0])
# print(word[-3])


# print(word.endswith('n'))
# print(word.startswith('p'))
# print('o' in word)
# print(word.count('o'))

# in, is
# password = 'q123апруке'
#
# if len(password) >= 6 and not password.isdigit() and not password.isalpha():
#     print('ok')
# else:
#     print(f'no, your password length is {len(password)}\n'
#           f'пароль должен состоять из числ и букв, а также длиннее 5')


# print(len(password))


# if len(password)


# print(bool(1))
# print(bool(0))

# print(bool('0'))
# print(bool(''))

# оператор назначения
# a = 5
# a = a + 2
# a += 2
# print(a)

# print(2 == 3-1)
# print(2 != 2)
# print(4 > 7)
# print(5 < 9)
# print(2 >= 1)
# print(2 > 1 or 2 == 1)
# print(2 >= 2)
# print(2 > 1 and 4 < 2)
# print(1 < 2 > 4)

# password = '123456'
#
# input_password = input('введите пароль: ')
#
# if input_password == password:
#     print('ok')
# else:
#     print('вы забыли пароль')


# time = 'утро'
#
# if time == 'morning' or time == "утро":
#     print('good morning')
# elif time == 'day' or time == "день":
#     print('good afternoon')
# elif time == 'evening' or time == "вечер":
#     print('good evening')
# else:
#     print('hello')
