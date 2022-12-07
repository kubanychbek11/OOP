
word = input('Введите слово')

letter = 'eyuioaуеыаоэяиюqwrtpsdfghjklzxcvbnmйцкнгшщзхфвпрлджчсмтб' \
         'EYUIOAУЕЫАОЭЯИЮQWRTPSDFGHJKLZXCVBNMЙЦКНГШЩЗХФВПРЛДЖЧСМТБ'
vowels = 'eyuioaуеыаоэяиюEYUIOAУЕЫАОЭЯИЮ'
consonants = 'qwrtpsdfghjklzxcvbnmйцкнгшщзхфвпрлджчсмтбQWRTPSDFGHJ' \
             'KLZXCVBNMЙЦКНГШЩЗХФВПРЛДЖЧСМТБ'

let = 0
vow = 0
cons = 0

for i in word:

     if i in letter:
        let = let + 1
     if i in vowels:
            vow = vow + 1
     if i in consonants:
                cons = cons + 1

percent_vow = round((vow / let) * 100, 2)
percent_cons = round((cons / let) * 100, 2)


print(f'Слово: {word}')
print(f'Количество букв: {let}')
print(f'Согласных букв: {vow}')
print(f'гласных букв: {cons}')
print(f'Гласные/Согласные: {percent_vow}%/{percent_cons}%')

