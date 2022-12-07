ten = list(range(1, 10+1))
evens = list(filter(lambda x: x % 2 == 0, ten))
print(evens)
evens_2 = list(map(lambda x: x * x, evens))
print(evens_2)
def function(lst=(list(ten))):
 while True:

    index = input('введите индекс')
    if index == 'exit':

      break
    else:
        try:

            index_1 = int(index)
            print(ten[index_1])
        except:

                print(f'Неверный индекс или данного индекса не существуетб введите цифры от {ten}')
function()
