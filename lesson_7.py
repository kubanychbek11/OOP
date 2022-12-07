# лямбда, исключения
# lambda arguments: expression

# print(first_word('python bishkek'))

# assert 2+2, 'неправильно'


# season = 'autumn'
#
# while True:
#     user = input('введите сезон: ')
#     if user != season:
#         raise Exception('неправильный сезон')
#     else:
#         print('ok')

"""ДОП ДЗ"""

words = ['python', 'bishkek', 'geektech']
while True:
    actual_word = words[0]
    attempts = len(actual_word)
    index1 = 0
    while attempts != 0:
        letter = input('введите букву: ')
        if letter == actual_word[index1]:
            print('угадали')
        else:
            break

    # try:
    #     user_input = int(input("угадайте слово: "))
    # except:
    #     print('неправильный индекс, вводить только числа!')
    # finally:
    #     word = 'geektech'
    #     print('проверка завершена!')


# try:
#     code
# except:
#     message
#     print(10/0)
# except:
#     print('на ноль не делим!')

# if ZeroDivisionError:
#     print('на ноль не де!')
# else:
#     print(10/0)

# name = 'azat'
# print(name[9])
# print(name + 25)
# print({2:5}['fgh'])


# current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
# sorted_list = lambda x: (sorted(i) for i in x)
# print(sorted_list)
# second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
# result = second_largest(current_list, sorted_list)
# print(result)

# new = [sorted(i) for i in current_list]
# print(new)
# for i in new:
#     print(i[len(i) - 2])


# print(result)

# a = lambda a, b: a + b
# print(a(2, 3))
#
# def b(a, b):
#     return a + b
# print(b(3, 2))

# numbers = list(range(1, 10+1))
# print(numbers)

# filtered_numbers = list(filter(lambda x: x < 6, numbers))
# filtered_numbers = [i*2 for i in numbers if i < 6]
# print(filtered_numbers)


# mapped_list = list(map(lambda x: x * 2, numbers))
# mapped_list = [i*3 for i in numbers]
# print(mapped_list)


# def up_letter(word: str):
#     return word.title()
#
# def last_up(word: str) -> str:
#     return word[:-1] + word[-1].upper()
#
# def show_words(sequence, func):
#     for word in sequence:
#         print(func(word))

# show_words(['python', 'bishkek', 'geektech'], last_up)
# show_words(['python', 'bishkek', 'geektech'], lambda word: word[:-1] + word[-1].upper())
