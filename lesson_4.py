# списки, кортежи
# list - (список)
# tuple - (кортеж)


new = list(range(1, 4))
print(new)

new = tuple(new)
print(new)
objects = (3,)

print(objects)
print(type(objects))




# objects = [1, 1, 1, 2, 2, 2]
# new = objects[::]
# # new[-1] = 5
# print(objects == new)
# print(objects is new)
#
# print(objects)
# print(new)
# print(id(objects))
# print(id(new))

# new = list(range(1, 4))
# max_ap = 1
# for i in objects:
#     if objects.count(i) > max_ap:
#         max_ap = objects.count(i)
#         print('max', max_ap)
# print(i if objects.count(i) == max_ap else 0)

# objects.sort()

# print(min(objects))
# print(max(objects))

"""изменение"""
# objects[0], objects[3] = objects[3], objects[0]
# objects[objects.index(False)] = 'Bishkek'
# objects[0] = objects[0].title()
# objects[2] += 15
# del objects[-1][1], objects[-1][1]

"""удаление"""
# del objects[4:7]
# objects = [i for i in objects if type(i) != str]
# objects.remove(True)
# objects.remove(4.7)
# objects.pop(0)
# deleted = objects.pop(0)
# print(deleted)

"""добавление"""
# objects.append('bishkek')
# objects.insert(3, 100)
# objects.extend(new)
# objects += new


# print(type(objects))
