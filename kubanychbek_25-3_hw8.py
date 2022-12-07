left = 0
right = 100
middle = 50
try_counter = 0

with open('results.txt', 'w', encoding='UTF-8') as file:
    while True:
        print(f"Загаданное число {middle}?")
        file.write(f'{middle}, ')
        answer = input()
        try_counter += 1
        if answer == '>':
            left = middle
            middle = (left + right) // 2
        elif answer == '<':
            right = middle
            middle = (left + right) // 2
        elif answer.lower() == 'да':
            file.write(f"\nКоличество попыток: {try_counter}")
            file.write(f"\nЗагаданное число: {middle}")
            break
        else:
            print('Неправильный ввод. Вводите да,< или >')
