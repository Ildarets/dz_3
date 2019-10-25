variables = input(" Ввете первый список чисел, через запятую:  ")

list_var = variables.split(',')
result = []
for i in list_var:
    if list_var.count(i) == 1:
        result.append(i)

print(*result)

