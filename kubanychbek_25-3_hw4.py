data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
del numbers[0]
letters.append(numbers.pop(0))
numbers.insert(3, 2)
numbers.sort()
letters.reverse()
letters[1] = letters[1].title()
letters[-2] = letters[-2].lower()
for i in range(len(numbers)):
    numbers[i] *= numbers[i]
l = tuple(letters)
n = tuple(numbers)
#

print(l)
print(n)
