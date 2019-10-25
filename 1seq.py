# list.append(x), list.copy() , list.remove(), list.insert() , list.sort()
#
# dict.items(), dict.copy(), dict.keys(), dict.values(), dict.keys()
#
# set.copy(),  set.remove(), set.add(), set.difference(), set.intersection()
#
# len(S), S.replace(',', ':'), S.split(','), S.isdigit(), S.isalpha()
#


list_variable = []
count = 0
count_variable = int(input("Введите количество элементов:  "))
# while count <= (count_variable - 1):
for i in range(count_variable):
    x = int(input("Введите " + (str(i+1)) + " элемент:  "))
    list_variable.append(x)
    count += 1
print(*list_variable)

