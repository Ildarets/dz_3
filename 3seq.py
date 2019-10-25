# coding=utf-8
my_set_1 = set()
my_set_2 = set()
variables_1 = input(" Введите первый список чисел, через запятую:  ")
variables_2 = input(" Введите второй список чисел, через запятую:  ")
list_var_1 = variables_1.split(',')
list_var_2 = variables_2.split(',')
set_var = set()

for i in list_var_1:
    x = int(i)
    my_set_1.add(x)

for i in list_var_2:
    x = int(i)
    my_set_2.add(x)

set_var = my_set_1.difference(my_set_2)
r = ''
for i in set_var:
   r += str(i) + ', '
print (r)