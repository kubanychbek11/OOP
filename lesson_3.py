# циклы: for, while
# item, iterable


# print(len(eng) == len(rus))
# eng = "hjkl;'zxcvbnm,.qwertyuiop[]asdfg "
# rus = "йцукенгшщзхъфывапролджэячсмитьбю "
#
# while True:
#     user_input = input('\nвведите слово: ')
#     for i in user_input:
#         if i in eng:
#             print(rus[eng.index(i)], end='')
#         else:
#             print(eng[rus.index(i)], end='')

# print(rus[eng.index('r')])


# yfcktljdfybt
# штрукшеутсу

# c = 0
#
# while c != 5:
#     c += 1
#     if c == 3:
#         print('мы устали')
#         continue
#     print(c)

# c = 0
#
# while True:
#     print('hello', c)
#     c += 1
#     if c == 100:
#         break

# attempts = int(input('сколько попыток? '))

# for i in range(1, attempts+1):
# while True:
#     password = input('enter password: ')
#     if password == 'exit':
#         break
#
#     if len(password) >= 6 and not password.isdigit() and not password.isalpha():
#         print('ok')
#     else:
#         print(f'no, your password length is {len(password)}\n'
#               f'пароль должен состоять из числ и букв, а также длиннее 5')



# cash = 100
# percents = 0.1
# years = 5
#
# counter = 1
#
# for year in range(1, years+1):
#     cash = round(cash * percents + cash, 1)
#     print(f'year: {counter} - {cash}')
#     counter += 1


# for i in range(1, 4):
#     for k in range(1, 4):
#         print(i, k)

# word = 'аксессуар'
#
# for letter in word:
#     if letter == 'с':
#         print("мы пропускаем 'с'")
#         continue
#     print(letter)

    # if letter == 'е':
    #     print('цикл завершен!')
    #     break
    # print(letter)

    # print(letter.upper(), end=' ')
